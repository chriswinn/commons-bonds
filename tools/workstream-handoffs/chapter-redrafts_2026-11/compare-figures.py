#!/usr/bin/env python3
"""Compare the figures, years, quotations and capitalized names carried by chapter versions.

Usage: compare-figures.py A.md B.md [C.md ...]
Prints, for each kind of token, what every version shares and what each version has that
another lacks. HTML comments are stripped first, so status headers and hidden notes don't count.
Also prints word and paragraph counts. Reusable for every chapter in the two-drafts process.
"""
import re
import sys


def load(path):
    text = open(path, encoding="utf-8").read()
    text = re.sub(r"<!--.*?-->", "", text, flags=re.S)
    return text


def numbers(text):
    # digits with optional $ / commas / decimals / percent words; years are split out below
    toks = re.findall(r"\$?\d[\d,]*(?:\.\d+)?(?:/\d+)?", text)
    return {t.rstrip(",") for t in toks}


def quotes(text):
    return set(re.findall(r"[\"“]([^\"”]{2,200})[\"”]", text))


def names(text):
    # runs of capitalized words not at a sentence start (rough; for eyeballing drift)
    out = set()
    for m in re.finditer(r"(?<![.!?:]\s)(?<!^)(?<!\n)\b([A-Z][\w.’'/-]+(?:\s+(?:of|the|and|for|de|to)?\s*[A-Z][\w.’'/-]+)*)", text):
        out.add(m.group(1).strip())
    return out


def paragraphs(text):
    paras = [p for p in re.split(r"\n\s*\n", text) if p.strip()]
    return [p for p in paras if not p.lstrip().startswith(("#", "---", "*By"))]


def main(paths):
    data = {}
    for p in paths:
        t = load(p)
        data[p] = dict(num=numbers(t), quo=quotes(t), nam=names(t),
                       words=len(re.findall(r"\b[\w’'$%.,-]+\b", t)), paras=len(paragraphs(t)))
    labels = {p: chr(ord("A") + i) for i, p in enumerate(paths)}
    for p in paths:
        print(f"{labels[p]} = {p}: {data[p]['words']} words, {data[p]['paras']} paragraphs")
    for kind, title in (("num", "NUMBERS"), ("quo", "QUOTED STRINGS"), ("nam", "CAPITALIZED NAMES")):
        print(f"\n== {title} ==")
        common = set.intersection(*(data[p][kind] for p in paths))
        print(f"shared by all: {len(common)}")
        for p in paths:
            for q in paths:
                if p == q:
                    continue
                only = sorted(data[p][kind] - data[q][kind])
                if only:
                    print(f"  in {labels[p]} not {labels[q]}: {only}")


if __name__ == "__main__":
    main(sys.argv[1:])
