from Const import IP, PORT, TIMEOUT
import socket
import time
import json
from type_msg import *
user_name = input('Введите имя пользователя')

def connect(IP, PORT):
    conn = socket.create_connection((IP, int(PORT)), TIMEOUT)
    return conn

def create_presence(user_name = 'guest'):
    presence = {
        'action': 'presence',
        'time': time.time(),
        'user': {
            'account_name': user_name
        }
    }
    return presence

def make_sendable(mess):
    jmessage = json.dumps(mess)
    bjmessage = jmessage.encode()
    return bjmessage

def send_message(conn, user_name, name_to=None, mess=None):
    message = f_msg(user_name, name_to, mess)
    conn.sendall(make_sendable(message))

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
while 1:
    name_to = input('For who? ')
    mess = input('Введите ваше сообщение ')
    try:
        send_message(conn, user_name, name_to, mess)
    except OSError as e:
        print(e)
    try:
        mess = get_message(conn)
        print(mess)
    except OSError:
        pass