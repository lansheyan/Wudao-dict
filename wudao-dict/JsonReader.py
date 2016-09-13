import json


class JsonReader:
    def __init__(self):
        self.__main_dict = {}
        self.FILE_NAME = './dict/dict.json'
        self.INDEX_FILE_NAME = './dict/dict.index'
        self.__index_dict = {}
        with open(self.INDEX_FILE_NAME, 'r') as f:
            for v in f.readlines():
                v = v.strip().split(':::')
                self.__index_dict[v[0]] = int(v[1])

    # return strings of word info
    def get_word_info(self, word):
        with open(self.FILE_NAME, 'r') as f:
            try:
                pos = self.__index_dict[word]
                f.seek(pos)
                word_struct = f.readline().strip().split(':::')
                word_info = word_struct[1]
            except KeyError:
                return None
        return word_info

