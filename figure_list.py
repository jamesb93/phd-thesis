from pathlib import Path
import re
import json

print('---- Extracting Figures And Formatting List ----')

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

specials = {
    "IMAGE 4.2.1" : "A visual depiction of the interconnected Fourses oscillators.",
    "IMAGE 4.2.3" : "The highest data point in weather data being located through simulated annealing.",
    "IMAGE 4.2.4" : "The travelling salesman problem being solved by simulated annealing.",
    "IMAGE 4.4.4" : "HDBSCAN minimum spanning tree visualisation.",
}

def special_checker(figure_number: str, unedited_text: str) -> str:
    if figure_number in specials:
        return specials[figure_number]
    return unedited_text  

def clean_url(url):
    url = url.replace('id=', '')
    url = url.replace("'", '')
    url = url.replace('"', '')
    return url

data = {}
routes = [x for x in Path("src/routes").rglob('*.svx')]
sections = {
    x.parent.stem : x 
    for x in routes if x.parent.stem in lookup
}

list_of_figures = {
    "audio" : [],
    "code" : [],
    "demo" : [],
    "image" : [],
    "video" : [],
}

for section, path in sections.items():
    with open(path, 'r') as f:
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
                    list_of_figures["demo"].append(
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
                list_of_figures["audio"].append(
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
            if tag_open == True and 'title' in line:
                title = line
            if tag_open == True and 'caption' in line:
                caption = line
            if tag_open == True and line[:2] == 'id':
                url = line
            if '/>' in line and tag_open:
                tag_open = False
                url = clean_url(url)
                url = f'{route_link[section]}#{url}'
                title = title.replace('title=', '')
                title = title[1:-1]
                caption = caption.replace('caption=', '')
                caption = caption[1:-1]
                list_of_figures["audio"].append(
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
                list_of_figures["video"].append(
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

                caption = special_checker(figure, caption)

                list_of_figures["image"].append(
                    [figure, caption, url]
                )
        # CODE
        for line in content:
            line = line.lstrip().rstrip()
            if '<Code2' in line:
                tag_open = True
            if tag_open and line[:6] == 'figure':
                figure = line
            if tag_open and line[:7] == 'caption':
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
                list_of_figures["code"].append(
                    [figure, caption, url]
                )

sorter = lambda x:int(
    x[0]
    .split(' ')
    [1]
    .replace('.', '')
)

for item in list_of_figures.values():
    item.sort(key=sorter)


with open("src/lib/data/list-of-interactive-elements.json", "w+") as f:
    json.dump(list_of_figures, f)

            