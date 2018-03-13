import json
import sys

# парсим параметры командной строки и проверяем их на валидность
def parser():
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
    return IP, PORT


def send_message(conn, data):
    data = json.dumps(data).encode()
    conn.sendall(data)


def get_message(conn):
    data = conn.recv(1024)
    data = data.decode()
    data = json.loads(data)
    return data