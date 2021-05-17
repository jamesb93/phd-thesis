from pathlib import Path
import nltk
import re

script_tags = r"<script>(.*?)</script>"
css_tags = r"<style>(.*?)</style>"

print('Downloading words corpus')
nltk.download('words')

words = set(nltk.corpus.words.words())

text_files = [x for x in Path("txt").rglob("*.txt")]

container = ''
for x in text_files:
    print(x)
    with open(x) as f:
        text = f.read()
        container += text

# for x in container.split():
#     print(x, x.lower() in words)

nonPunct = re.compile('.*[A-Za-z0-9].*')

filtered = [x for x in container.split() if nonPunct.match(x)] 
iswords = [x for x in filtered if x.lower() in words]

print(len(iswords))
with open('stripped_text.txt', 'w') as f:
    # for item in iswords:
        # f.write(f'{item}\n')

    f.write(' '.join(iswords))