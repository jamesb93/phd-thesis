from pathlib import Path
import json

print('---- Extracting Structure Of Thesis ----')

def get_heading(line):
    line = line.rstrip()
    line = line.replace('#', '')
    line = line.lstrip()
    return line

def get_url(line):
    line = line.rstrip()
    line = line.replace('#', '')
    line = line.lstrip()
    line = line.lower()
    line = line.replace(' ', '-')
    line = line.replace('.', '')
    if line.startswith('--'):
        line = line.replace('--', '')
    line = line.replace('/', '')
    return line

files = [x for x in Path("src/routes").rglob("*.svx")]
ignores = ['test', 'directory', 'index', 'acknowledgements']
svx = [x for x in files if x.stem not in ignores]
route_lookup = {
    'routes' : '',
    'projects' : '/projects',
    'tech' : '/tech'
}

hierarchy = {
    'howto' : 'ii',
    'submission-materials': 'iv',
    'list-of-interactive-elements' : 'v',
    'introduction' : '1',
    'preoccupations' : '2',
    'content-awareness' : '3',
    'stitch-strata' : '4.1',
    'annealing-strategies' : '4.2',
    'refracted-touch' : '4.3',
    'reconstruction-error' : '4.4',
    'interferences' : '4.5',
    'mosh' : '5.1',
    'ftis' : '5.2',
    'reacoma' : '5.3',
    'conclusion' : '',
    'copyright' : '',
    'references' : ''
}

structure = {}


for page in svx:
    c = {
        1 : 0,
        2 : 0,
        3 : 0,
        4 : 0,
        5 : 0
    }
    route = route_lookup[page.parent.name]
    path = f'{route}/{page.stem}'
    prefix = hierarchy[page.stem]
    print(page.stem, prefix)
    structure[path] = []
    with open(page) as text:
        lines = text.readlines();
        for line in lines:
            if line.startswith('#'):
                heading = get_heading(line)
                url = get_url(line)
                indent = line.count('#')
                print(heading, indent)

                calculated_heading = ''
                
                c[indent] += 1
                if indent == 1:
                    calculated_heading = f'{prefix} {heading}'
                elif indent == 2:
                    calculated_heading = f'{prefix}.{c[2]} {heading}'
                elif indent == 3:
                    calculated_heading = f'{prefix}.{c[2]}.{c[3]} {heading}'
                elif indent == 4:
                    calculated_heading = f'{prefix}.{c[2]}.{c[3]}.{c[4]} {heading}'
                elif indent == 5:                    
                    calculated_heading = f'{prefix}.{c[2]}.{c[3]}.{c[4]}.{c[5]} {heading}'
                for i in range(indent+1, 5):
                    c[i] = 0

                structure[path].append(
                    {
                        'heading' : calculated_heading,
                        'indent' : indent,
                        'url' : url
                    }
                )
                

with open('static/structure.json', 'w') as output:
    json.dump(structure, output)
