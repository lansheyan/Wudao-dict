import json

word_map = {}
with open('a_desulfar.txt', 'r') as f:
    list = json.load(f)
    for v in list:
        word_map[v['word']] = v

f = open('a_desulfar.json', 'w')
json.dump(word_map, f)
f.close()