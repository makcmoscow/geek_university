import time
import select
from socket import socket, AF_INET, SOCK_STREAM
def new_listen_socket(address):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(address)
    sock.listen(5)
    sock.settimeout(0.2)
    return sock
def mainloop():
    address = ('', 7777)
    clients = []
    sock = new_listen_socket(address)
    while True:
        try:
            conn, addr = sock.accept()
        except OSError as e:
            pass
        else:
            print('Получен запрос на соединение с %s'%str(addr))
            clients.append(conn)
        finally:
            w = []
            try:
                r,w,e = select.select([], clients, [], 0)
            except Exception as e:
                pass
            for s_client in w:
                timestr = time.ctime(time.time()) + '\n'
                try:
                    s_client.send_message(timestr.encode('ascii'))
                except:
                    clients.remove((s_client))
print('Эхо-сервер запущен')
mainloop()
