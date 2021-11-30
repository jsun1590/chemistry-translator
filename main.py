import json

with open("pt.json") as fh:
    elements = json.loads(fh.read())

inp = "Francium Oganesson"
inp = inp.lower().split()

out = ""

for i in inp:
    for j in elements['elements']:
        if i == j["name"].lower():
            out += j["symbol"]

print(out)