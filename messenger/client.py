# from Const import IP, PORT, TIMEOUT
# IP = '127.0.0.1'
PORT = 7777
IP = input('Введите IP: ')
TIMEOUT = 10
import socket
import time
import json
from type_msg import *
from threading import Thread
import sys
user_name = input('Введите имя пользователя: ')
class WriteThread(Thread):
    def __init__(self):
        super().__init__()
    def run(self):
        while True:
            try:
                name_to = input('Кому? ')
                mess = input('Введите ваше сообщение: ')
                a = send_message(conn, user_name, name_to, mess)
                if a:
                    print('OK')
                time.sleep(1)
            except OSError:
                sys.exit(1)


class ReadThread(Thread):
    def __init__(self):
        super().__init__()
    def run(self):
        while True:
            try:
                mess = get_message(conn)
                if 'message' in mess:
                    print()
                    print(mess['from'], '>>:', mess['message'])
            except OSError as e:
                pass




def connect(IP, PORT):
    conn = socket.create_connection((IP, int(PORT)), 10)
    return conn

def create_presence(user_name = 'guest'):
    presence = f_presence(user_name)
    return presence

def make_sendable(mess):
    jmessage = json.dumps(mess)+'\n\n'
    bjmessage = jmessage.encode()
    return bjmessage

def send_message(conn, user_name, name_to=None, mess=None):
    message = f_msg(user_name, name_to, mess)
    conn.sendall(make_sendable(message))
    return True

def send_presence(conn, user_name):
    mess = f_presence(user_name)
    conn.sendall(make_sendable(mess))
    # mess = create_presence(user_name)


def get_message(conn):
    bjmess = conn.recv(1024)
    jmess = bjmess.decode()
    try:
        mess = json.loads(jmess)
    except Exception as e:
        pass
    else:
        return mess

def chk_responce(resp):
    try:
        if resp['responce'] == 200:
            conn_well = True
        else:
            conn_well = False
        return conn_well
    except Exception as e:
        print('error', e)

def send_online(conn):
    send_presence(conn)
    resp = get_message(conn)
    a = chk_responce(resp)
    return a

conn = connect(IP, PORT)
send_presence(conn, user_name)

wr1 = WriteThread()
wr1.start()
r1 = ReadThread()
r1.start()

# while 1:
#     try:
#         mess = get_message(conn)
#         print(mess)
#     except OSError:
#         pass