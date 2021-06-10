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

routes = [x for x in Path("src/routes").rglob('*.svx')]
sections = [x for x in routes if x.stem in lookup.keys()]

for x in sections:
    print(x.stem)