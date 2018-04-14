from Const import IP, PORT, TIMEOUT
import socket
import time
import json

user_name = input()

def connect(IP, PORT):
    conn = socket.create_connection((IP, PORT), TIMEOUT)
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

def make_sendable(message):
    jmessage = json.dumps(message)
    bjmessage = jmessage.encode()
    return bjmessage

def send_presence(conn):
    mess = create_presence(user_name)
    mess = make_sendable(mess)
    conn.sendall(mess)

conn = connect(IP, PORT)
send_presence(conn)
