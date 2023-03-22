from pydub import AudioSegment
from pathlib import Path
import json
from concurrent.futures import ThreadPoolExecutor, as_completed
from multiprocessing import Manager

from rich.progress import Progress



if __name__ == "__main__":
    files = [x for x in Path("static").rglob('*.mp3')]

    d = Manager().dict()

    def get_time(f):
        au = AudioSegment.from_mp3(str(f))  
        seconds = au.duration_seconds

        m, s = divmod(seconds, 60)
        h, m = divmod(m, 60)

        time_string = f'{int(m)}:{int(s)}'

        d[str(f.name)] = time_string

    with Progress() as progress:
        task = progress.add_task('Parsing', total=len(files))
        with ThreadPoolExecutor() as pool:
            futures = [pool.submit(get_time, f) for f in files]
            for result in as_completed(futures):
                progress.update(task, advance=1)

    with open("src/lib/data/durations.json", "w+") as f:
        json.dump(dict(d), f)
