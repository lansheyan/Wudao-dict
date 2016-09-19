import json

NAME = 'zh_dict'

word_map = {}
with open('bajiushi.txt', 'r') as f:
    list = json.load(f)
    for v in list:
        word_map[v['word']] = v

f = open('%s.json' % NAME, 'w+')
fin = open('%s.index' % NAME, 'w+')
for v in word_map:
    fin.write(v + ':::' + str(f.tell()) + '\n')
    f.write(v + ':::' + json.dumps(word_map[v]) + '\n')
f.close()
fin.close()


