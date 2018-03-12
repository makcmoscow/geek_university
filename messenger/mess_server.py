import socket
import json
import sys
import time
import select
from shared_utils import parser


IP, PORT = parser()

class Server:
    # Инициализируем входные данные и создаем серверный сокет
    def __init__(self):
        self.server_sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM, proto=0)  # TCP
        self.server_sock.bind((IP, PORT))
        self.server_sock.listen(5)
        self.server_sock.settimeout(10)

    def connection(self):
        self.sock, addr = server.server_sock.accept()
        return self.sock

    def send_message(self, data):
        data = json.dumps(data).encode()
        self.sock.sendall(data)

    def get_message(self):
        data = self.connection().recv(1024)
        data = data.decode()
        data = json.loads(data)
        return data


def preparing_responce(recieved_message):
    if 'action' in recieved_message and recieved_message['action'] == 'presence'\
            and 'time' in recieved_message and isinstance((recieved_message['time']), float):
        return {'responce': 200,
                'time': time.time()
                }
    else:
        return {'responce': 400,
                'error': 'Неверный запрос'}


if __name__ == '__main__':

    server = Server()
    responce = preparing_responce(server.get_message())
    server.send_message(responce)


