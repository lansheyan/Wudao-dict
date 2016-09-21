import json

f = open('zh_dict.txt', 'r')
a = json.load(f)
f.close()

for v in a:
    ndesc = []
    for s in v['desc']:
        if s:
            ndesc.append(s)
    v['desc'] = ndesc

f = open('zh_dict.txt', 'w')
json.dump(a, f)
f.close()

