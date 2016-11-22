# -*- coding: utf-8 -*-

import json
import os


class UserHistory:
    MAX_LATEST_LEN = 20
    content = {}
    latest_word = []
    DICT_FILE_NAME = './usr/usr_word.json'
    LATEST_FILE_NAME = './usr/latest.txt'
    ONLINE_CACHE = './usr/online_cache.json'

    def __init__(self):
        # Create empty file
        if not os.path.exists(self.DICT_FILE_NAME):
            with open(self.DICT_FILE_NAME, 'w+') as f:
                tmp_dict = {}
                json.dump(tmp_dict, f)
        if not os.path.exists(self.LATEST_FILE_NAME):
            open(self.LATEST_FILE_NAME, 'w+').close()
        if not os.path.exists(self.ONLINE_CACHE):
            with open(self.ONLINE_CACHE, 'w+') as f:
                json.dump([], f)

    def add_item(self, word):
        # Update word dict
        with open(self.DICT_FILE_NAME, 'r') as f:
            self.content = json.load(f)
            if word in self.content:
                self.content[word] += 1
            else:
                self.content[word] = 1
        # Update latest word list
        with open(self.LATEST_FILE_NAME, 'r') as f:
            self.latest_word = [v.strip() for v in f.readlines()]
            if len(self.latest_word) < self.MAX_LATEST_LEN:
                self.latest_word.append(word)
            else:
                self.latest_word.pop(0)
                self.latest_word.append(word)
        with open(self.LATEST_FILE_NAME, 'w') as f:
            for v in self.latest_word:
                f.write(v + '\n')
        with open(self.DICT_FILE_NAME, 'w') as f:
            # TODO :to many words i/o
            if len(self.content) <= 1000:
                json.dump(self.content, f, indent=4)

    # add word info to online cache
    def add_word_info(self, word_info):
        with open(self.ONLINE_CACHE, 'r') as f:
            now_list = json.load(f)
        # TODO :too much usr word
        with open(self.ONLINE_CACHE, 'w') as f:
            now_list.append(word_info)
            json.dump(now_list, f)

    # get word info from online cache
    def get_word_info(self, word):
        with open(self.ONLINE_CACHE, 'r') as f:
            now_list = json.load(f)
        for v in now_list:
            if word == v['word']:
                return v
        return None


