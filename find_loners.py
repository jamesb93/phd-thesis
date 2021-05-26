from pathlib import Path

lossy = [x for x in Path("static").rglob('*.mp3')]

for x in lossy:
    companion = x.with_suffix('.wav')
    if not companion.exists():
        print(x.parent, x.name)