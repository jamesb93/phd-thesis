from pathlib import Path
import re

files = [x for x in Path("src/routes").rglob("*.svx")]
ignores = ['test', 'references', 'directory', 'index', 'acknowledgements']
svx = [x for x in files if x.stem not in ignores]
route_lookup = {
    'routes' : '',
    'projects' : '/projects',
    'tech' : '/tech'
}

structure = {}

list_of_bad_words = [
    'Of', 'And', 'The', 'To', 'As', 'In', 'For'
]

how_many = 0

for every_other_document in svx:
    with open(every_other_document) as content:
        all_text = content.readlines()

        for line_number, writing in enumerate(all_text):
            regex = re.findall('\[\[(.*?)\]\]', writing)
            for finds in regex:
                for word in list_of_bad_words:
                    if word in finds:
                        print(every_other_document.stem, line_number, word)
                        how_many += 1

print(how_many)

                            # if '#' not in writing and stripped_heading.lower() in writing.lower():
                            #     print(stripped_heading, writing)
                