# -*- coding: utf-8 -*-

class JsonReader:
    def __init__(self):
        self.__main_dict = {}
        self.FILE_NAME = './dict/dict.json'
        self.INDEX_FILE_NAME = './dict/dict.index'
        self.ZH_FILE_NAME = './dict/zh_dict.json'
        self.ZH_INDEX_FILE_NAME = './dict/zh_dict.index'
        self.__index_dict = {}
        self.__zh_index_dict = {}
        with open(self.INDEX_FILE_NAME, 'r') as f:
            for v in f.readlines():
                v = v.strip().split(':::')
                self.__index_dict[v[0]] = int(v[1])
        with open(self.ZH_INDEX_FILE_NAME, 'r') as f:
            for v in f.readlines():
                v = v.strip().split(':::')
                self.__zh_index_dict[v[0]] = int(v[1])

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

    def get_zh_word_info(self, word):
        with open(self.ZH_FILE_NAME, 'r') as f:
            try:
                pos = self.__zh_index_dict[word]
                f.seek(pos)
                word_struct = f.readline().strip().split(':::')
                word_info = word_struct[1]
            except KeyError:
                return None
        return word_info

