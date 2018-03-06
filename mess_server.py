import socket
import json
import sys

class Server:
    def __init__(self, host = '127.0.0.1', port = 7777, timeout=10):
        self.host = host
        self.port = port
        self.server_sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM, proto=0)  # TCP

    def connection(self):
        try:
            IP = sys.argv[1]
        except IndexError:
            IP = ''
        try:
            PORT = int(sys.argv[2])
        except IndexError:
            PORT = 7777
        except ValueError:
            print('Порт должен быть целым числом, а не {}'.format(PORT))
            sys.exit(0)
        self.server_sock.bind(("{}".format(IP), int(PORT)))
        self.server_sock.listen(5)
        self.server_sock.settimeout(10)
        self.sock, addr = server.server_sock.accept()
        return self.sock

    def s_send(self, data):
        data = json.dumps(data).encode()
        self.sock.sendall(data)

    def s_recieve(self):
        data = b''
        data += self.connection().recv(1024)
        return data

def preparing_responce(recieved_presence):
    recieved_presence = recieved_presence.decode()
    recieved_presence = json.loads(recieved_presence)
    if 'action' in recieved_presence and recieved_presence['action'] == 'presence'\
            and 'time' in recieved_presence and isinstance ((recieved_presence['time']), float):
        return {'responce': 200}
    else:
        return {'responce': 400, 'error': 'Неверный запрос'}


if __name__ == '__main__':

    server = Server()
    payload = preparing_responce(server.s_recieve())
    server.s_send(payload)


