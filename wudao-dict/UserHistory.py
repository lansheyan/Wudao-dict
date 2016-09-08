import json
import os


class UserHistory:
    MAX_LATEST_LEN = 10
    content = {}
    latest_word = []
    DICT_FILE_NAME = './usr/usr_word.json'
    LATEST_FILE_NAME = './usr/latest.txt'

    def __init__(self):
        # Create empty file
        if not os.path.exists(self.DICT_FILE_NAME):
            with open(self.DICT_FILE_NAME, 'w+') as f:
                tmp_dict = {}
                json.dump(tmp_dict, f)
        if not os.path.exists(self.LATEST_FILE_NAME):
            open(self.LATEST_FILE_NAME, 'w+').close()

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
            json.dump(self.content, f, indent=4)

