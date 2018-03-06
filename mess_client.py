import socket
import json
import sys
import time

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


class Client:
    def __init__(self, host = '127.0.0.1', port = 7777, timeout=None):
        self.host = host
        self.port = port
        self.connection = socket.create_connection((host, port), timeout)

    def _read(self):
        data = b''
        data += self.connection.recv(1024)
        data = json.loads(data.decode())
        return data

    def send(self, data):
        data = json.dumps(data).encode()
        self.connection.sendall(data)

    def recieve(self):
        payload = self._read()
        return payload


def create_presence(user_name = 'guest'):
    presence = {
        'action' : 'presence',
        'time' : time.time(),
        'user' : {
            'account_name': user_name
        }
    }
    return presence

client = Client(IP, PORT)
client.send(create_presence())
print(client.recieve())











