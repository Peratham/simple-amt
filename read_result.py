import json
a = []
for l in open('examples/image_sentence/results.txt','r'):
    a.append(json.loads(l))
#  a[0]['output'][0]['description']
