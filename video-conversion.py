import subprocess
from pathlib import Path

videos = [x for x in Path("static").rglob('*.mov')]

for x in videos:
    print(str(x))
    first_pass = f"ffmpeg -i {str(x)} -c:v libvpx-vp9 -b:v 0 -crf 23 -pass 1 -an -f null /dev/null"
    second_pass = f"ffmpeg -i {str(x)} -c:v libvpx-vp9 -b:v 0 -crf 23 -ac 2 -pass 2 -c:a libopus {str(x.with_suffix('.webm'))} -y"
    subprocess.call(first_pass.split(' '))
    subprocess.call(second_pass.split(' '))
    quit()