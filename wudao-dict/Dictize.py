import json

NAME = 'dict'

word_map = {}
with open('./dict/%s.txt' % NAME, 'r') as f:
    list = json.load(f)
    for v in list:
        word_map[v['word']] = v

f = open('./dict/%s.json' % NAME, 'w+')
fin = open('./dict/%s.index' % NAME, 'w+')
for v in word_map:
    fin.write(v + ' ' + str(f.tell()) + '\n')
    f.write(v + ':::' + json.dumps(word_map[v]) + '\n')
f.close()
fin.close()


