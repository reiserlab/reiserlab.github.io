#!/usr/bin/env python3
"""Merge figure records (media/figures/_added_*.yaml) into data/publications.yaml and media/credits.yaml.

Each record: id, figure, figure_caption, source, license, quality. Run from the repo root:
    uv run tools/merge_figures.py media/figures/_added_older.yaml
The record file is deleted once merged.
"""
import re, sys, yaml
from pathlib import Path

def q(text: str) -> str:
    return '"' + str(text).replace('\\', '\\\\').replace('"', '\\"') + '"'

def main(paths):
    pubs_path = Path("data/publications.yaml"); s = pubs_path.read_text()
    pubs = {p["id"]: p for p in yaml.safe_load(s)}
    credits = []
    for path in map(Path, paths):
        for rec in yaml.safe_load(path.read_text()):
            pid = rec["id"]
            if pid not in pubs:
                print("unknown id, skipped:", pid); continue
            if not (Path("media/figures") / rec["figure"]).exists():
                print("missing file, skipped:", rec["figure"]); continue
            m = re.search(rf"(- id: {re.escape(pid)}\n(?:  .*\n)*?)(  pillars:)", s)
            if not m:
                print("no pillars anchor, skipped:", pid); continue
            block = re.sub(r"  figure(_caption)?: .*\n", "", m.group(1))
            s = s.replace(m.group(0), block + f"  figure: {rec['figure']}\n  figure_caption: {q(rec['figure_caption'])}\n" + m.group(2), 1)
            p = pubs[pid]
            credits.append(
                f"- file: media/figures/{rec['figure']}\n"
                f"  source: {q(p['title'] + ' (' + str(p['year']) + '), ' + rec['figure_caption'].split(',')[0] + (', doi:' + p['doi'] if p.get('doi') else ''))}\n"
                f"  origin: {q(rec.get('source', ''))}\n"
                f"  creator: {p['authors'].split(',')[0]} et al.\n"
                f"  license: {q(rec.get('license', ''))}\n"
                f"  quality: {rec.get('quality', '')}\n")
            print("merged", pid)
        path.unlink()
    pubs_path.write_text(s); yaml.safe_load(s)
    with open("media/credits.yaml", "a") as fh:
        fh.write("\n# Added by tools/merge_figures.py\n" + "".join(credits))
    yaml.safe_load(open("media/credits.yaml"))

if __name__ == "__main__":
    main(sys.argv[1:])
