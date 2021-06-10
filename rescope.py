import re
from pathlib import Path

lookup = {
    'introduction' : '1.',
    'preoccupations' : '2.',
    'content-awareness' : '3.',
    'stitch-strata' : '4.1.',
    'annealing-strategies' : '4.2.',
    'refracted-touch' : '4.3.',
    'reconstruction-error' : '4.4.',
    'interferences' : '4.5.',
    'mosh' : '5.1.',
    'ftis' : '5.2.',
    'reacoma' : '5.3.'
}

widgets = ['AUDIO', 'VIDEO', 'CODE', 'DEMO', 'IMAGE']

def replace(text: str, prefix: str) -> str:
    temporary_text: list = []
    for line in text:
        for widget in widgets:
            for i in range(25):
                
                reg = f'[{widget} {i}]'
                search = re.search(reg, line)
                if search:
                    scoped_figure = f'[{widget} {prefix}{i}]'
                    line = line.replace(reg, scoped_figure)

                reg = f'"{widget} {i}"'
                search = re.search(reg, line)
                if search:
                    scoped_figure = f"'{widget} {prefix}{i}'"
                    line = line.replace(reg, scoped_figure)

                reg = f"'{widget} {i}'"
                search = re.search(reg, line)
                if search:
                    scoped_figure = f"'{widget} {prefix}{i}'"
                    line = line.replace(reg, scoped_figure)

        temporary_text.append(line)
    
    return ' '.join(temporary_text)

routes = [x for x in Path("src/routes").rglob('*.svx')]
sections = [x for x in routes if x.stem in lookup.keys()]

for section in sections:
    prefix = lookup[section.stem]
    updated_text = None
    with open(section, 'r') as f:
        text = f.readlines()
        updated_text = replace(text, prefix)
    with open(section, 'w') as out_file:
        out_file.write(updated_text)
            