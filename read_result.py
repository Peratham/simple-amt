import json
a = []
for l in open('examples/image_sentence/results.txt','r'):
    a.append(json.loads(l))
