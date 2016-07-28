import sys


class IndexBuilder():
    index_count = 207728
    index_file_path = './dicts/En_Zh/index.txt'
    dict_file_path = './dicts/En_Zh/final.txt'

    def __init__(self):
        pass

    def generate_index(self):
        generated_count = 0
        fw = open(self.index_file_path, 'w+')
        with open(self.dict_file_path, 'r') as fp:
            while True:
                if fp.tell() == 0:
                    line = fp.readline().strip()
                    fw.write(line + '\t0\n')
                else:
                    now_line = fp.readline()
                    if len(now_line) == 0:
                        break
                    elif now_line.strip().startswith('------------'):
                        index_num = fp.tell()
                        line = fp.readline().strip().split()
                        if len(line) == 0:
                            break
                        elif not line[0].startswith('------------'):
                            fw.write(line[0] + '\t%d\n' % index_num)
                            sys.stdout.write('\rGenerate Index: %d/%d\r' % (generated_count, self.index_count))
                            sys.stdout.flush()
                            generated_count += 1
        fw.close()

d = IndexBuilder()
d.generate_index()
