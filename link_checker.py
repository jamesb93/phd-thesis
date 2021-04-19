import re
import json
import requests
from pathlib import Path


routes = Path("src/routes")
details = []
for x in routes.rglob("*.svx"):
    with open(x, 'r') as f:
        content = f.read()
        link_name = "[^]]+"
        link_url = "http[s]?://[^)]+"
        markup_regex = f'\[({link_name})]\(\s*({link_url})\s*\)'

        for match in re.findall(markup_regex, content):
            name = match[0]
            url = match[1]
            try:
                r = requests.head(url)
                print(url, r.status_code)
                details.append({
                    "name": name,
                    "url" : url,
                    "status_code" : r.status_code
                })
            except:
                details.append({
                    "name": name,
                    "url" : url,
                    "status_code" : "ERROR"
                })
            
api = {}
api["links"] = details

with open("status_codes.json", "w+") as f:
    json.dump(api, f, indent=4)
            

            