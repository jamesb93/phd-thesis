from pathlib import Path
import json

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

structure = {}

for page in svx:
    route = route_lookup[page.parent.name]
    path = f'{route}/{page.stem}'
    structure[path] = []
    with open(page) as text:
        lines = text.readlines();
        for line in lines:
            if line.startswith('#'):
                heading = get_heading(line)
                url = get_url(line)
                indent = line.count('#')
                structure[path].append(
                    {
                        'heading' : heading,
                        'indent' : indent,
                        'url' : url
                    }
                )
                

with open('static/structure.json', 'w') as output:
    json.dump(structure, output)
