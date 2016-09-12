from WudaoClient import WudaoClient
from CommandDraw import CommandDraw
from UserHistory import UserHistory

import sys
import socket
import json


class WudaoCommand:
    def __init__(self):
        # Member
        self.word = ''
        self.param_list = []
        self.draw_conf = True
        # Init
        self.param_separate()
        # self.word = 'ass'
        self.painter = CommandDraw()
        self.history_manager = UserHistory()
        # client
        self.client = WudaoClient()

    def param_separate(self):
        if len(sys.argv) == 1:
            self.param_list.append('h')
        else:
            for v in sys.argv[1:]:
                if v.startswith('-'):
                    self.param_list.append(v[1:])
                else:
                    self.word += v
        self.word = self.word.strip()

    def param_parse(self):
        if len(self.param_list) == 0:
            return
        if 'h' in self.param_list or '-help' in self.param_list:
            print('Youdao is wudao, An powerful dict.')
            exit(0)
        if 'k' in self.param_list:
            self.client.close()
            exit(0)
        if 's' in self.param_list:
            self.draw_conf = False

    def query(self):
        server_context = self.client.get_word_info(self.word).strip()
        if server_context != 'None':
            wi = json.loads(server_context)
            self.history_manager.add_item(self.word)
            self.painter.draw_text(wi, self.draw_conf)
        else:
            print('Error: no such word')


def main():
    app = WudaoCommand()
    app.param_parse()
    app.query()


if __name__ == '__main__':
    main()
