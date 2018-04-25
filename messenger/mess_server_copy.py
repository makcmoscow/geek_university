import socket
import select
import json
import messages
import time
# from shared_utils import parser, send_message, get_message, preparing_responce
# IP, PORT = parser()
clients = []
def preparing_responce(recieved_message):
    if 'action' in recieved_message and recieved_message['action'] == 'presence'\
            and 'time' in recieved_message and isinstance((recieved_message['time']), float):
        return {'responce': 200,
                'time': time.time()
            }


class Client:
    def __init__(self, name, socket, addr):
        self.name = name
        self.socket = socket
        self.addr = addr
    @staticmethod
    def send_message(message, socket):
        bjmess = json.dumps(message).encode()
        print('sending bjmessage')
        socket.sendall(bjmess)
    @staticmethod
    def get_message(socket):
        data = socket.recv(1024)
        data = data.decode()
        data = json.loads(data)
        return data

def read_requests(r_clients, all_clients):
    """
    Чтение сообщений, которые будут посылать клиенты
    :param r_clients: клиенты которые могут отправлять сообщения
    :param all_clients: все клиенты
    :return:
    """
    # Список входящих сообщений
    messages = []

    for sock in r_clients:
        try:
            # Получаем входящие сообщения
            message = Client.get_message(sock)
            # Добавляем их в список
            # В идеале нам нужно сделать еще проверку, что сообщение нужного формата прежде чем его пересылать!
            # Пока оставим как есть, этим займемся позже
            messages.append(message)
        except:
            print('Клиент {} {} отключился'.format(sock.fileno(), sock.getpeername()))
            print('Все клиенты: ', all_clients)
            print('удаляемый сокет: ', sock)
            all_clients.remove(sock)

    # Возвращаем словарь сообщений
    return messages

def write_responses(messages, w_clients, all_clients):
    """
    Отправка сообщений тем клиентам, которые их ждут
    :param messages: список сообщений
    :param w_clients: клиенты которые читают
    :param all_clients: все клиенты
    :return:
    """

    for sock in w_clients:
        # Будем отправлять каждое сообщение всем
        for message in messages:
            try:
                # Отправить на тот сокет, который ожидает отправки
                Client.send_message(message, sock)
            except:  # Сокет недоступен, клиент отключился
                print('Клиент {} {} отключился'.format(sock.fileno(), sock.getpeername()))
                sock.close()
                print('Все клиенты: ', all_clients)
                print('удаляемый сокет: ', sock)
                all_clients.remove(sock)

serv_sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM, proto=0)
net_args = ('127.0.0.1', 7777)
serv_sock.bind(net_args)
serv_sock.listen(5)
serv_sock.settimeout(7)
while 1:
    try:
        sock, addr = serv_sock.accept()
        recv_mess = sock.recv(1024)
        recv_mess = recv_mess.decode()
        recv_mess = json.loads(recv_mess)
        login = recv_mess['user']['account_name']
        client = Client(login, sock, addr)
        responce = preparing_responce(recv_mess)
        client.send_message(responce, sock)
    except OSError as e:
        print('timeout error')
        pass
    else:
        print("Получен запрос на соединение от %s" % str(addr))
        clients.append(client)
        print(clients)
    finally:
        wait = 0
        r = []
        w = []
        clients_sockets = []
        for client in clients:
            clients_sockets.append(client.socket)
            print(clients)
        try:
            r, w, e = select.select(clients_sockets, clients_sockets, [], wait)
        except:
            pass  # Ничего не делать, если какой-то клиент отключился


        requests = read_requests(r, clients_sockets)  # Получаем входные сообщения
        write_responses(requests, w, clients_sockets)  # Выполним отправку входящих сообщений




















#
#
#
#
#     def read_requests(self, r_clients, all_clients):
#         """
#         Чтение сообщений, которые будут посылать клиенты
#         :param r_clients: клиенты которые могут отправлять сообщения
#         :param all_clients: все клиенты
#         :return:
#         """
#         # Список входящих сообщений
#         messages = []
#
#         for sock in r_clients:
#             try:
#                 # Получаем входящие сообщения
#                 message = get_message(sock)
#                 print('mess: ', message)
#                 # Добавляем их в список
#                 # В идеале нам нужно сделать еще проверку, что сообщение нужного формата прежде чем его пересылать!
#                 # Пока оставим как есть, этим займемся позже
#                 messages.append(message)
#             except:
#                 print('Клиент {} {} отключился'.format(sock.fileno(), sock.getpeername()))
#                 print(all_clients)
#                 del all_clients[sock]
#
#         # Возвращаем словарь сообщений
#         return messages
#
#     def write_responses(self, messages, w_clients, all_clients):
#         """
#         Отправка сообщений тем клиентам, которые их ждут
#         :param messages: список сообщений
#         :param w_clients: клиенты которые читают
#         :param all_clients: все клиенты
#         :return:
#         """
#
#         for sock in w_clients:
#             # Будем отправлять каждое сообщение всем
#             for message in messages:
#                 try:
#                     # Отправить на тот сокет, который ожидает отправки
#                     send_message(sock, message)
#                 except:  # Сокет недоступен, клиент отключился
#                     print('Клиент {} {} отключился'.format(sock.fileno(), sock.getpeername()))
#                     sock.close()
#                     print(all_clients)
#                     del all_clients[sock]
#
#
#
#         # elif 'action' in recieved_message and recieved_message['action'] == 'msg'\
#         #         and 'time' in recieved_message and isinstance((recieved_message['time']), float):
#         #     resp = {'responce': 200,
#         #             'time': time.time()
#         #             }
#         #     return '111'
#
#
#         else:
#             return {'responce': 400,
#                     'error': 'Неверный запрос'}
#
#
# if __name__ == '__main__':
#
#     server = Server()
#     # Создаем словарик, где будут храниться пары username/socket
#     clients = {}
#     while True:
#         try:
#             conn = server.connection() # Проверка подключений
#
#             # получаем сообщение от клиента
#             message = get_message(conn)
#             # из сообщения понимаем имя клиента и создаем пару username/socket
#             clients[message['user']['account_name']] = conn
#             # формируем ответ
#             response = preparing_responce(message)
#             # отправляем ответ клиенту
#             send_message(conn, response)
#         except OSError as e:
#             pass  # timeout вышел
#         else:
#             print("Получен запрос на соединение от %s" % str(server.addr))
#             print(clients)
#             # Добавляем клиента в список
#
#         finally:
#             # Проверить наличие событий ввода-вывода
#             wait = 0
#             r = []
#             w = []
#             try:
#                 r, w, e = select.select(clients.keys(), clients.keys(), [], wait)
#                 print(clients.keys())
#             except:
#                 pass  # Ничего не делать, если какой-то клиент отключился
#
#             requests = server.read_requests(r, clients)  # Получаем входные сообщения
#             if requests:
#                 print(requests)
#             server.write_responses(requests, w, clients)  # Выполним отправку входящих сообщений
