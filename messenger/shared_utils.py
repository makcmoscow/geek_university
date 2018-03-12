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