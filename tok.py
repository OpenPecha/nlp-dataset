from pathlib import Path

from third_party.Botok.botok import Text

infile = Path("input/articletest.txt")
raw = infile.read_text(encoding="utf-8")

t = Text(raw).tokenize_sentences_plaintext

outfile = Path("output") / infile.name

outfile.write_text(t, encoding="utf-8")
