import socket
import json
import sys
import time
from shared_utils import parser

print(parser()[0])
# Создаем класс Клиент, с методами отправки и получения сообщений
class Client:
    def __init__(self, host = '127.0.0.1', port = 7777, timeout=None):
        self.host = host
        self.port = port
        self.sock = socket.create_connection((host, port), timeout)

    def send_mess(self, data):
        data = json.dumps(data).encode()
        self.sock.sendall(data)

    def recieve(self):
        data = self.sock.recv(1024)
        data = json.loads(data.decode())
        return data

# Функция создания сообщения о присутствии


def create_presence(user_name = 'guest'):
    presence = {
        'action': 'presence',
        'time': time.time(),
        'user': {
            'account_name': user_name
        }
    }
    return presence


def translating_message(message):
    if message['responce'] == 200:
        return 'OK'
    elif message['responce'] == 400:
        return 'shit'


# Создаем экземпляр класса Клиент
IP, PORT = parser()
client = Client(IP, PORT)
print('created client')
# Отправляем сообщение о присутствии
client.send_mess(create_presence())
print('sended message')
# Печатаем ответ от сервера
print(translating_message(client.recieve()))











