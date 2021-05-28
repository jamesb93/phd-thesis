fd -e dat -x rm {}
cd static
fd -e mp3 --exclude pieces -x audiowaveform -i {} -o {.}.dat -b 8 -z 32
cd pieces
fd -e mp3 -x audiowaveform -i {} -o {.}.dat --split-channels -b 8 -z 128 
