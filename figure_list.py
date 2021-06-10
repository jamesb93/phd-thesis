from pathlib import Path
import re
import json
from typing import List

lookup = [
    'introduction',
    'preoccupations',
    'content-awareness',
    'stitch-strata',
    'annealing-strategies',
    'refracted-touch',
    'reconstruction-error',
    'interferences',
    'mosh',
    'ftis',
    'reacoma',
]

data = {}
routes = [x for x in Path("src/routes").rglob('*.svx')]
sections = {
    x.stem : x 
    for x in routes if x.stem in lookup
}

list_of_figures = {"data" : []}

for section in lookup:
    with open(sections[section], 'r') as f:
        content = f.readlines()

        # DEMO
        tag_open = False
        title = ''
        caption = ''
        demos = [
            'Agglom', 
            'Points', 
            'Bricolage', 
            'KDTree', 
            'MaxwaveStart', 
            'NMF', 
            'Sys', 
            'X86', 
            'HPSS', 
            'Sage', 
            'Z12'
        ]
        for line in content:
            line = line.lstrip().rstrip()
            for demo in demos:
                if f'<{demo}' in line:
                    tag_open = True
                if tag_open == True and 'title' in line:
                    title = line
                if tag_open == True and 'caption' in line:
                    caption = line
                if '/>' in line and tag_open == True:
                    tag_open = False
                    title = title.replace('title=', '')
                    title = title[1:-1]
                    caption = caption.replace('caption=', '')
                    caption = caption[1:-1]
                    list_of_figures["data"].append(
                        [caption, title]
                    )

        # AUDIO
        ## Album
        tag_open = False
        title = ''
        figure = ''

        for line in content:
            line = line.lstrip().rstrip()
            if '<Album' in line:
                tag_open = True
            if tag_open == True and 'figure' in line:
                figure = line
            if tag_open == True and 'title' in line:
                title = line
            if '/>' in line and tag_open == True:
                tag_open = False
                title = title.replace('title=', '')
                title = title[1:-1]
                figure = figure.replace('figure=', '')
                figure = figure[1:-1]
                list_of_figures["data"].append(
                    [figure, title]
                )

        ## Waveform
        tag_open = False
        title = ''
        caption = ''

        for line in content:
            line = line.lstrip().rstrip()
            if '<Waveform' in line:
                tag_open = True
            if tag_open == True and 'title' in line:
                title = line
            if tag_open == True and 'caption' in line:
                caption = line
            if '/>' in line and tag_open == True:
                tag_open = False
                title = title.replace('title=', '')
                title = title[1:-1]
                caption = caption.replace('caption=', '')
                caption = caption[1:-1]
                list_of_figures["data"].append(
                    [caption, title]
                )

        # VideoMedia2
        tag_open = False
        figure = ''
        caption = ''

        for line in content:
            line = line.lstrip().rstrip()
            if '<VideoMedia2' in line:
                tag_open = True
            if tag_open == True and 'figure' in line:
                figure = line
            if tag_open == True and 'caption' in line:
                caption = line
            if '/>' in line and tag_open == True:
                tag_open = False
                figure = figure.replace('figure=', '')
                figure = figure[1:-1]
                caption = caption.replace('caption=', '')
                caption = caption[1:-1]
                list_of_figures["data"].append(
                    [figure, caption]
                )

        # IMAGE
        tag_open = False
        figure = ''
        caption = ''

        for line in content:
            line = line.lstrip().rstrip()
            if '<ImageMedia2' in line:
                tag_open = True
            if tag_open == True and 'figure' in line:
                figure = line
            if tag_open == True and 'caption' in line:
                caption = line
            if '/>' in line and tag_open == True:
                tag_open = False
                figure = figure.replace('figure=', '')
                figure = figure[1:-1]
                caption = caption.replace('caption=', '')
                caption = caption[1:-1]
                list_of_figures["data"].append(
                    [figure, caption]
                )
        # CODE
        for line in content:
            line = line.lstrip().rstrip()
            if '<Code2' in line:
                tag_open = True
            if tag_open == True and 'figure' in line:
                figure = line
            if tag_open == True and 'caption' in line:
                caption = line
            if '>' in line and tag_open == True:
                tag_open = False
                figure = figure.replace('figure=', '')
                figure = figure[1:-1]
                caption = caption.replace('caption=', '')
                caption = caption[1:-1]
                list_of_figures["data"].append(
                    [figure, caption]
                )

list_of_figures['data'].sort(
    key = lambda x:
    int(
    x[0]
    .split(' ')
    [1]
    .replace('.', '')
    )
)

with open("static/list-of-figures.json", "w+") as f:
    json.dump(list_of_figures, f, indent=4)

            