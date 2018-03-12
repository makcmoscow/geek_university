import socket
import json
import sys
import time

# парсим параметры командной строки и проверяем их на валидность
try:
    IP = sys.argv[1]
except IndexError:
    IP = '127.0.0.1'
try:
    PORT = int(sys.argv[2])
except IndexError:
    PORT = 7777
except ValueError:
    print('Порт должен быть целым числом, а не {}'.format(sys.argv[2]))
    sys.exit(0)

# Создаем класс Клиент, с методами отправки и получения сообщений
class Client:
    def __init__(self, host = '127.0.0.1', port = 7777, timeout=None):
        self.host = host
        self.port = port
        self.sock = socket.create_connection((host, port), timeout)

    def _read(self):
        data = b''
        data += self.sock.recv(1024)
        data = json.loads(data.decode())
        return data

    def send_mess(self, data):
        data = json.dumps(data).encode()
        self.sock.sendall(data)

    def recieve(self):
        data = b''
        data += self.sock.recv(1024)
        data = json.loads(data.decode())
        return data

# Создаем функцию создания сообщения о присутствии
def create_presence(user_name = 'guest'):
    presence = {
        'action' : 'presence',
        'time' : time.time(),
        'user' : {
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
client = Client(IP, PORT)
# Отправляем сообщение о присутствии
client.send_mess(create_presence())
# Печатаем ответ от сервера
print(translating_message(client.recieve()))











