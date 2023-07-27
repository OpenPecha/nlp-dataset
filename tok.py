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
        out.append(unit)
    return sep.join(out)


inpath = Path("input/")
infiles = list(inpath.rglob("*.txt"))
for f in infiles:
    raw = f.read_text(encoding="utf-8")

    outpath = Path(  "output/sentences") / f.parts[-2]
    outpath.mkdir(exist_ok=True)
    outfile = outpath / f.name
    if not outfile.is_file():
        print(outfile)
        t = Text(raw).custom_pipeline("basic_cleanup", sent_tok, "dummy", plaintext_sent_par)
        print()
        outfile.write_text(t, encoding="utf-8")
