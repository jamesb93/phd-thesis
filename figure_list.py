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

route_link = {
    'introduction' : '/introduction',
    'preoccupations' : '/preoccupations',
    'content-awareness' : '/content-awareness',
    'stitch-strata' : '/projects/stitch-strata',
    'annealing-strategies' : '/projects/annealing-strategies',
    'refracted-touch' : '/projects/refracted-touch',
    'reconstruction-error' : '/projects/reconstruction-error',
    'interferences' : '/projects/interferences',
    'mosh' : '/tech/mosh',
    'ftis' : '/tech/ftis',
    'reacoma' : '/tech/reacoma'
}

def clean_url(url):
    url = url.replace('id=', '')
    url = url.replace("'", '')
    url = url.replace('"', '')
    return url

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

        title = ''
        caption = ''
        figure = ''
        url = ''

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
                if tag_open and line[:2] == 'id':
                    url = line
                if '/>' in line and tag_open == True:
                    tag_open = False
                    url = clean_url(url)
                    url = f'{route_link[section]}#{url}'
                    title = title.replace('title=', '')
                    title = title[1:-1]
                    caption = caption.replace('caption=', '')
                    caption = caption[1:-1]
                    list_of_figures["data"].append(
                        [caption, title, url]
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
            if tag_open and line[:2] == 'id':
                url = line
            if '/>' in line and tag_open == True:
                tag_open = False
                url = clean_url(url)
                url = f'{route_link[section]}#{url}'
                title = title.replace('title=', '')
                title = title[1:-1]
                figure = figure.replace('figure=', '')
                figure = figure[1:-1]
                list_of_figures["data"].append(
                    [figure, title, url]
                )

        ## Waveform
        tag_open = False
        title = ''
        caption = ''

        for line in content:
            line = line.lstrip().rstrip()
            if '<Waveform' in line:
                tag_open = True
            if tag_open and 'title' in line:
                title = line
            if tag_open and 'caption' in line:
                caption = line
            if tag_open and line[:2] == 'id':
                url = line
            if '/>' in line and tag_open:
                tag_open = False
                url = clean_url(url)
                url = f'{route_link[section]}#{url}'
                title = title.replace('title=', '')
                title = title[1:-1]
                caption = caption.replace('caption=', '')
                caption = caption[1:-1]
                list_of_figures["data"].append(
                    [caption, title, url]
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
            if tag_open and line[:2] == 'id':
                url = line
            if '/>' in line and tag_open == True:
                tag_open = False
                url = clean_url(url)
                url = f'{route_link[section]}#{url}'
                figure = figure.replace('figure=', '')
                figure = figure[1:-1]
                caption = caption.replace('caption=', '')
                caption = caption[1:-1]
                list_of_figures["data"].append(
                    [figure, caption, url]
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
            if tag_open and line[:2] == 'id':
                url = line
            if '/>' in line and tag_open == True:
                tag_open = False
                url = clean_url(url)
                url = f'{route_link[section]}#{url}'
                figure = figure.replace('figure=', '')
                figure = figure[1:-1]
                caption = caption.replace('caption=', '')
                caption = caption[1:-1]
                list_of_figures["data"].append(
                    [figure, caption, url]
                )
        # CODE
        for line in content:
            line = line.lstrip().rstrip()
            if '<Code2' in line:
                tag_open = True
            if tag_open and line[:6] == 'figure':
                figure = line
            if tag_open and line[:6] == 'caption':
                caption = line
            if tag_open and line[:2] == 'id':
                url = line
            if '>' in line and tag_open == True:
                tag_open = False
                url = clean_url(url)
                url = f'{route_link[section]}#{url}'
                figure = figure.replace('figure=', '')
                figure = figure[1:-1]
                caption = caption.replace('caption=', '')
                caption = caption[1:-1]
                list_of_figures["data"].append(
                    [figure, caption, url]
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

            