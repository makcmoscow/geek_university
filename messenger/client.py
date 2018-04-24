from Const import IP, PORT, TIMEOUT
import socket
import time
import json

user_name = '12'
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

def send_message(conn, mess):
    conn.sendall(make_sendable(mess))

def send_presence(conn):
    mess = create_presence(user_name)
    send_message(conn, mess)

def get_message(conn):
    bjmess = conn.recv(1024)
    jmess = bjmess.decode()
    mess = json.loads(jmess)
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
# conn_exist = send_online(conn)
# if conn_exist:
while 1:
    mess = input('Введите ваше сообщение ')
    try:
        send_message(conn, mess)
    except OSError:
        pass