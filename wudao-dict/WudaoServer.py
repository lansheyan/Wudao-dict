from JsonReader import JsonReader

import socket


class WudaoServer:
    def __init__(self):
        self.json_reader = JsonReader()
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # Singleton
        try:
            self.server.bind(("0.0.0.0", 2376))
        except OSError:
            print('OSError: Port has been used.')
            exit(0)
        self.server.listen()
        print('Server on...')

    def run(self):
        while True:
            # Get bytes
            conn, addr = self.server.accept()
            data = conn.recv(256)
            word = data.decode('utf-8').strip()
            print('Get:' + str(len(data)) + ' bytes ' + word)
            # Shutdown
            if word == '---shutdown keyword---':
                self.server.close()
                exit(0)
            # Get word
            try:
                word_info = self.json_reader.get_word_info(word)
                if word_info is not None:
                    conn.sendall(word_info.encode('utf-8'))
                    print('Send: ' + str(len(word_info)) + ' bytes ')
                else:
                    conn.sendall('None'.encode('utf-8'))
            except KeyError:
                print('No words: ' + word)
            conn.close()


if __name__ == '__main__':
    ws = WudaoServer()
    ws.run()
