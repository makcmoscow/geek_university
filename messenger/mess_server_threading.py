import socket
import json
import time
import select
from shared_utils import parser, send_message, get_message, preparing_responce
from type_msg import *

IP, PORT = parser()
clients = []
class Server():
    def __init__(self):
        self.server_sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM, proto=0)
        self.server_sock.bind((IP, PORT))
        self.server_sock.listen(5)
        self.server_sock.settimeout(0.2)
        self.clients = clients
        self.readers = []
        self.writers = []
    def acception(self, clients):
        while 1:
            try:
                conn, addr = self.server_sock.accept()
            except OSError as e:
                pass
            else:
                print('Получен запрос на соединение от {}'.format(addr))
                clients.append(conn)
            return clients

    def serv_forever(self):
        while 1:
            try:
                clients = self.acception(self.clients)
                # print(clients)
                wait = 0
            except OSError as e:
                pass
            try:
                self.readers, self.writers, errors = select.select(clients, clients, [], wait)
                print('readers: ',self.readers, 'writers ', self.writers)
                print(self.writers, self.readers)
                for writer in self.writers:
                    presence = get_message(writer)
                    clients.remove(writer)

                for reader in self.readers:
                    send_message(writer, preparing_responce(presence))
                    clients.remove(reader)
            except:
                pass



server = Server()
server.serv_forever()



