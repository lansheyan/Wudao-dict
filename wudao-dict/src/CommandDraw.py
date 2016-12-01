# -*- coding: utf-8 -*-
from __future__ import print_function


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
            if '英' in word['pronunciation']:
                uncommit += u'英 ' + self.PEP_PATTERN % word['pronunciation']['英'] + '  '
            if '美' in word['pronunciation']:
                uncommit += u'美 ' + self.PEP_PATTERN % word['pronunciation']['美']
            if '' in word['pronunciation']:
                uncommit = u'英/美 ' + self.PEP_PATTERN % word['pronunciation']['']
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
        if not conf:
            print('')
        else:
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
                    # collins dict
                    if len(v) != 3:
                        continue
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
                    if len(v) != 2:
                        continue
                    print(str(count) + '. ' + self.GREEN_PATTERN % '[例]', end=' ')
                    print(v[0], end='  ')
                    print(self.BROWN_PATTERN % v[1])
                    count += 1

    def draw_zh_text(self, word, conf):
        # Word
        print(self.RED_PATTERN % word['word'])
        # pronunciation
        if word['pronunciation']:
            print(self.PEP_PATTERN % word['pronunciation'])
        # paraphrase
        if word['paraphrase']:
            for v in word['paraphrase']:
                v = v.replace('  ;  ', ', ')
                print(self.BLUE_PATTERN % v)
        # complex
        if conf:
            # description
            count = 1
            if word["desc"]:
                print('')
                for v in word['desc']:
                    if not v:
                        continue
                    # sub title
                    print(str(count) + '. ', end='')
                    v[0] = v[0].replace(';', ',')
                    print(self.GREEN_PATTERN % v[0])
                    # sub example
                    sub_count = 0
                    if len(v) == 2:
                        for e in v[1]:
                            if sub_count % 2 == 0:
                                e = e.strip().replace(';', '')
                                print(self.BROWN_PATTERN % ('    ' + e + '    '), end='')
                            else:
                                print(e)
                            sub_count += 1
                    count += 1
            # example
            if word['sentence']:
                count = 1
                print(self.RED_PATTERN % '\n例句:')
                for v in word['sentence']:
                    if len(v) == 2:
                        print('')
                        print(str(count) + '. ' + self.BROWN_PATTERN % v[0] + '    '+ v[1])
                    count += 1
