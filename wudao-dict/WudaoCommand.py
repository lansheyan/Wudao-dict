from JsonReader import JsonReader
from CommandDraw import CommandDraw
from UserHistory import UserHistory

import sys


class WudaoCommand:
    def __init__(self):
        # Member
        self.word = ''
        self.param_list = []
        # Init
        #self.param_separate()
        self.word = 'ass'
        self.reader = JsonReader()
        self.painter = CommandDraw()
        self.history_manager = UserHistory()

    def param_separate(self):
        if len(sys.argv) == 1:
            print('Usage: wdd word')
            sys.exit(0)
        else:
            for v in sys.argv[1:]:
                if v.startswith('-'):
                    self.param_list.append(v[1:])
                else:
                    self.word += v
        self.word = self.word.strip()

    def query(self):
        wi = self.reader.get_word_info(self.word)
        if wi is None:
            print('Error: no such word')
        else:
            self.history_manager.add_item(self.word)
            self.painter.draw_text(wi)


def main():
    app = WudaoCommand()
    app.query()


if __name__ == '__main__':
    main()
