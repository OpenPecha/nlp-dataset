from pathlib import Path

from third_party.Botok.botok import Text, sentence_tokenizer, WordTokenizer


def sent_tok(raw):
    w = WordTokenizer()
    tokens = w.tokenize(raw, spaces_as_punct=True)
    return sentence_tokenizer(tokens)


def plaintext_sent_par(units, sep="\n") -> str:
    out = []
    for u in units:
        unit = "".join([word.text for word in u['tokens']]).strip()
        while out and unit and len(units) >= 2 and (unit[0] == " " or unit[0] == "།"):
            out[-1] += unit[0]
            if len(unit) >= 2:
                unit = unit[1:]
            else:
                unit = ""
        out.append(unit)
    return sep.join(out)


inpath = Path("input/")
infiles = list(inpath.rglob("*.txt"))
for f in infiles:
    raw = f.read_text(encoding="utf-8").replace(" ", " ").replace("​", " ").replace("། ། ", "། །")

    outpath = Path(  "output/sentences") / f.parts[-2]
    outpath.mkdir(exist_ok=True)
    outfile = outpath / f.name
    if not outfile.is_file():
        print(outfile)
        t = Text(raw).custom_pipeline("basic_cleanup", sent_tok, "dummy", plaintext_sent_par)
        print()
        outfile.write_text(t, encoding="utf-8")
