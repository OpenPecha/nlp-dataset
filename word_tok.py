from pathlib import Path
import json

from third_party.Botok.botok import WordTokenizer


def segment(tok, raw):
    # tok: WordTokenizer instance
    # raw: string containing newline-delimited sentences
    # output: list of sentences where each sentence is a list of token-POS pairs
    #         tokens for which a POS is not applicable have `None` as value, others have a string
    #         all NO_POS and NON_WORD have been turned into OTHER
    lines = raw.split("\n")
    segmented = []
    for l in lines:
        seg = tok.tokenize(l)

        seg_line = []
        for token in seg:
            if not token.chunk_type == "TEXT":
                seg_line.append([token.text, None])
            else:
                pos = token.pos
                if isinstance(pos, list):
                    pos = pos[0]

                if pos == "NO_POS" or pos == "NON_WORD":
                    pos = "OTHER"

                seg_line.append([token.text, pos])
        segmented.append(seg_line)
    return segmented


t = WordTokenizer()

in_path = Path("output/sentences")
in_files = list(in_path.rglob("*.txt"))[:1]  # remove [:1] for production


for f in in_files:

    outpath = Path(  "output/words") / f.parts[-2]
    outpath.mkdir(exist_ok=True)
    outfile = outpath / (f.stem + ".json")
    if not outfile.exists():
        raw = f.read_text(encoding="utf-8")
        segmented = segment(t, raw)

        json_object = json.dumps(segmented, indent=4, ensure_ascii=False)
        with open(outfile, "w", encoding="utf-8") as out:
            out.write(json_object)
