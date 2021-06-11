from pathlib import Path
import subprocess
import nltk

subprocess.call('mkdir -p tmp'.split(' '))

routes = {
    'index' : 'src/routes/index.svx',
    'howto' : 'src/routes/howto.svx',
    'introduction' : 'src/routes/introduction.svx',
    'preoccupations' : 'src/routes/introduction.svx',
    'content-awareness' : 'src/routes/content-awareness.svx',
    'projects' : 'src/routes/projects/index.svx',
    'stitch-strata' : 'src/routes/projects/stitch-strata.svx',
    'annealing-strategies' : 'src/routes/projects/annealing-strategies.svx',
    'refracted-touch' : 'src/routes/projects/refracted-touch.svx',
    'reconstruction-error' : 'src/routes/projects/reconstruction-error.svx',
    'interferences' : 'src/routes/projects/interferences.svx',
    'technical-implementation' : 'src/routes/tech/index.svx',
    'mosh' : 'src/routes/tech/mosh.svx',
    'ftis' : 'src/routes/tech/ftis.svx',
    'reacoma' : 'src/routes/tech/reacoma.svx',
    'conclusion' : 'src/routes/conclusion.svx'
}

main_string = ''

# Pandoc to docx which has the sanest format
for route, path in routes.items():
    command = f'pandoc -f markdown -s {path} -o tmp/{route}.docx'
    cli = subprocess.Popen(command.split(' '))
    cli.wait()

# Pandoc docx to text
for docx in Path('tmp').rglob('*.docx'):
    command = f'pandoc -s {docx} -o tmp/{docx.with_suffix(".txt").name}'
    subprocess.call(command.split(' '))

for x in routes.keys():
    with open(f'tmp/{x}.txt', 'r') as f:
        content = f.read()
        main_string += content

with open('/Users/james/Cloud/PhD/turnitin-version.txt', 'w') as f:
    f.write(main_string)