from pydub import AudioSegment
from pathlib import Path
import json



files = [x for x in Path("static").rglob('*.mp3')]

d = {}

for i, x in enumerate(files):
    print( i / len(files) )
    au = AudioSegment.from_mp3(str(x))  
    seconds = au.duration_seconds

    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)

    time_string = f'{int(m)}:{int(s)}'

    d[str(x.name)] = time_string

with open("static/durations.json", "w+") as f:
    json.dump(d, f, indent=4)
