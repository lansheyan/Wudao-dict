
class CommandDraw:
    RED_PATTERN = '\033[31m%s\033[0m'
    GREEN_PATTERN = '\033[32m%s\033[0m'
    BLUE_PATTERN = '\033[34m%s\033[0m'
    PEP_PATTERN = '\033[36m%s\033[0m'
    BROWN_PATTERN = '\033[33m%s\033[0m'

    def draw_text(self, word, conf):
        # Word
        print(self.RED_PATTERN % word['word'])
        # pronunciation
        if word['pronunciation']:
            uncommit = ''
            try:
                uncommit += u'英 ' + self.PEP_PATTERN % word['pronunciation']['英'] + '  '
                uncommit += u'美 ' + self.PEP_PATTERN % word['pronunciation']['美']
            except KeyError:
                uncommit = u'英/美 ' + self.PEP_PATTERN % word['pronunciation']['']
            finally:
                print(uncommit)
        # paraphrase
        for v in word['paraphrase']:
            print(self.BLUE_PATTERN % v)
        # short desc
        if word['rank']:
            print(self.RED_PATTERN % word['rank'], end='  ')
        if word['pattern']:
            print(self.RED_PATTERN % word['pattern'].strip())
        # sentence
        if conf:
            count = 1
            if word['sentence']:
                print('')
                if len(word['sentence'][0]) == 2:
                    collins_flag = False
                else:
                    collins_flag = True
            else:
                return
            for v in word['sentence']:
                if collins_flag:
                    # collins dcit
                    if v[1] == '' or len(v[2]) == 0:
                        continue
                    if v[1].startswith('['):
                        print(str(count) + '. ' + self.GREEN_PATTERN % (v[1]), end=' ')
                    else:
                        print(str(count) + '. ' + self.GREEN_PATTERN % ('[' + v[1] + ']'), end=' ')
                    print(v[0])
                    for sv in v[2]:
                        print(self.GREEN_PATTERN % u'  例: ' + self.BROWN_PATTERN % (sv[0] + sv[1]))
                    count += 1
                    print('')
                else:
                    # 21 new year dict
                    print(str(count) + '. ' + self.GREEN_PATTERN % '[例]', end=' ')
                    print(v[0], end='  ')
                    print(self.BROWN_PATTERN % v[1])
                    count += 1


