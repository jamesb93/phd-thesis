# https://trac.ffmpeg.org/wiki/Encode/VP9
# Uses a two pass encoder to get high quality stereo WEBM's for compatability with most browsers.

import subprocess
from pathlib import Path

videos = [x for x in Path("static").rglob('*.mov')]

for i, x in enumerate(videos):
    print(i)
    first_pass = f"ffmpeg -i {str(x)} -hide_banner -loglevel error -c:v libvpx-vp9 -b:v 0 -crf 23 -pass 1 -an -f null /dev/null"
    second_pass = f"ffmpeg -i {str(x)} -hide_banner -loglevel error -c:v libvpx-vp9 -b:v 0 -crf 23 -ac 2 -pass 2 -c:a libopus {str(x.with_suffix('.webm'))} -y"
    subprocess.call(first_pass.split(' '))
    subprocess.call(second_pass.split(' '))