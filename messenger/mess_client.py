import socket
import json
import sys
import time
from shared_utils import parser, send_message, get_message


# Создаем класс Клиент, с методами отправки и получения сообщений
class Client:
    def __init__(self, host = '127.0.0.1', port = 7777, timeout=10):
        self.host = host
        self.port = port
        self.sock = socket.create_connection((host, port), timeout)

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

while 1:
    # Создаем экземпляр класса Клиент
    IP, PORT = parser()
    client = Client(IP, PORT)
    # Отправляем сообщение о присутствии
    send_message(client.sock, create_presence())
    # Печатаем ответ от сервера
    print(translating_message(get_message(client.sock)))











