# pip install pdfminer.six

from pdfminer.high_level import extract_text
from urllib.request import urlretrieve

url = "https://arxiv.org/pdf/2107.13586.pdf"
urlretrieve(url, "paper.pdf")

text = extract_text("paper.pdf")
print(text[:1000], "...\n\n[обрезано]")
