from pathlib import Path

from third_party.Botok.botok import Text, sentence_tokenizer, WordTokenizer


infile = Path("input/articletest.txt")
raw = infile.read_text(encoding="utf-8")


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


t = Text(raw).custom_pipeline("basic_cleanup", sent_tok, "dummy", plaintext_sent_par)


outfile = Path("output") / infile.name

outfile.write_text(t, encoding="utf-8")
