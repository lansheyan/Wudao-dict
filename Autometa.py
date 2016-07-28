# -*- coding:utf8 -*-

# word, property, paraphrase, pronunciation_en,  pronunciation_us, intro, sentence, sentence_para

# TODO


class Autometa():
    index_file_path = './dicts/En_Zh/index.txt'
    dict_file_path = './dicts/En_Zh/final.txt'
    state = 0

    def __init__(self):
        pass

    def parse_word(self, seek_pos):
        parse_ans = {}
        with open(self.dict_file_path, 'r') as fdic:
            fdic.seek(seek_pos)
            line = fdic.readline().strip().split()
            parse_ans['word'] = line[0]
            if len(line) == 2:
                parse_ans['pronunciation_en'] = line[1]
            while True:
                line = fdic.readline().strip().split()
                if line[0].startswith('------------'):
                    self.state = 0
                    break
                elif line[0] == '英':
                    pronunciation_en = ''
                    for i in range(1,len[line]):
                        pronunciation_en += line[i] + ' '
                    parse_ans['pronunciation_en'] = pronunciation_en
                elif line[0] == '美':
                    pronunciation_us = ''
                    for i in range(1,len[line]):
                        pronunciation_us += line[i] + ' '
                    parse_ans['pronunciation_us'] = pronunciation_us
