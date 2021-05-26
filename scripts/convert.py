import json
import sys

f = sys.argv[1]
neighbours = sys.argv[2]
mindist = sys.argv[3]
out = sys.argv[4]

d = {
    'parameters' : {
        'neighbours' : neighbours,
        'mindist' : mindist
    },
    'data' : []
}

with open(f) as json_file:
    data = json.load(json_file)

    for k, v in data.items():
        d['data'].append({
            'x' : v[0],
            'y' : v[1],
            'file' : str(k)
        })

with open(out, 'w') as f:
    json.dump(d, f)
