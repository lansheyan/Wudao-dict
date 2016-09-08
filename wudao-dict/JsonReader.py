import json


class JsonReader:
    def __init__(self):
        self.__main_dict = {}
        self.FILE_NAME = './dict/a_desulfar.json'
        with open(self.FILE_NAME, 'r') as f:
            self.__main_dict = json.load(f)

    def get_word_info(self, word):
        try:
            word_info = self.__main_dict[word]
        except KeyError:
            return None
        return word_info

