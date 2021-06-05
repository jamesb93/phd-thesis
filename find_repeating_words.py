from pathlib import Path

files = [x for x in Path("src/routes").rglob("*.svx")]
ignores = ['test', 'references', 'directory', 'index', 'acknowledgements']
svx = [x for x in files if x.stem not in ignores]
route_lookup = {
    'routes' : '',
    'projects' : '/projects',
    'tech' : '/tech'
}

structure = {}

for page in svx:
    with open(page) as text:
        lines = text.readlines();
        for i, line in enumerate(lines):
            word_array = line.split(' ')
            word_array = [x for x in word_array if x != '']
            for a, b in zip(word_array, word_array[1:]):
                if a == b:
                    print(page, i, a, b)