from pathlib import Path
import re
import json


api = {}
routes = Path("src/routes")
link_container = []
video_container = []
for x in routes.rglob("*.svx"):
    with open(x, 'r') as f:
        content = f.read()
        flattened = content.replace("\n", " ")
        
        tag_open = False
        url = ''
        name = ''
        for line in content.split('\n'):
            if '<YouTube' in line:
                tag_open = True
            if tag_open == True and 'title' in line:
                name = line
            if tag_open == True and 'url' in line:
                url = line
            if '/>' in line and tag_open == True:
                tag_open = False
                video_container.append({
                    "name" : name[7:-1],
                    "url" : url[5:-1]
                })


        # Extract []() style links
        link_name = "[^]]+"
        link_url = "http[s]?://[^)]+"
        markup_regex = f'\[({link_name})]\(\s*({link_url})\s*\)'

        for match in re.findall(markup_regex, content):
            name = match[0]
            url = match[1]
            exists = False
            for item in link_container:
                if item["url"] == url:
                    exists = True
            
            if not exists:
                link_container.append({
                    "name" : match[0],
                    "url" : match[1]
                })

        # Extract whatever is inbetween <VideoMedia>
        vids_regex = '<VideoMedia(.*?)</VideoMedia>'
        url_regex = 'src="(.*?)"'
        name_regex = "title='(.*?)'"
        iframes = re.findall(vids_regex, flattened)
        for x in iframes:
            url = re.findall(url_regex, x)
            name = re.findall(name_regex, x)
            if url and name:
                video_container.append({
                    "name" : name[0],
                    "url" : url[0]
                })
            else:
                print(f'ERROR: {url}, {name}')
        
        # Extract YouTube Links
        # youtube_regex = '<YouTube(.*?)>'
        # url_regex = 'url="(.*?)"'
        # title_regex = 'title="(.*?)"'

        # for x in re.findall(youtube_regex, flattened):
        #     url = re.findall(url_regex, x)
        #     name = re.findall(name_regex, x)
        #     if url and name:
        #         video_container.append({
        #             "name" : name[0],
        #             "url" : url[0],
        #         })

api["links"] = link_container
api["videos"] = video_container

with open("static/links.json", "w+") as f:
    json.dump(api, f, indent=4)

            