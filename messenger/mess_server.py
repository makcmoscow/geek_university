import socket
import select
import json
from shared_utils import parser, send_message, get_message, preparing_responce
from threading import Thread
IP, PORT = parser()
# Список входящих сообщений
messages = []
class Message:
    def __init__(self, sock, name_from, message, name_to = None):
        self.sock = sock
        self.name_from = name_from
        self.name_to = name_to
        self.message = message

class Server:
    # Инициализируем входные данные и создаем серверный сокет
    def __init__(self):
        self.server_sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM, proto=0)  # TCP
        self.server_sock.bind((IP, PORT))
        self.server_sock.listen(5)
        self.server_sock.settimeout(0.2)


    def connection(self):
        self.sock, self.addr = server.server_sock.accept()
        return self.sock

    def _read(self, sock):
        raw_message = b''
        while not raw_message.endswith(b"\n\n"):
            try:
                raw_message += self.connection.recv(1024)
            except socket.error as err:
                print("error recv data", err)
        payload = raw_message.decode()
        message = payload[:-3]
        print('message', message)
        message = json.loads(message)
        print(message)
        return message

    def read_requests(self, r_clients, all_clients):
        """
        Чтение сообщений, которые будут посылать клиенты
        :param r_clients: клиенты которые могут отправлять сообщения
        :param all_clients: все клиенты
        :return:
        """

        for sock in r_clients:
            try:
                # Получаем входящие сообщения
                message = self._read(sock)
                print('mess: ', message)
                # Добавляем их в список
                # В идеале нам нужно сделать еще проверку, что сообщение нужного формата прежде чем его пересылать!
                # Пока оставим как есть, этим займемся позже
                messages.append(message)
            except:
                print('Клиент {} {} отключился'.format(sock.fileno(), sock.getpeername()))
                print(all_clients)
                del all_clients[sock]

        # Возвращаем словарь сообщений
        return messages

    def write_responses(self, messages, w_clients, all_clients):
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
                    send_message(sock, message)
                except:  # Сокет недоступен, клиент отключился
                    print('Клиент {} {} отключился'.format(sock.fileno(), sock.getpeername()))
                    sock.close()
                    print(all_clients)
                    del all_clients[sock]



        # elif 'action' in recieved_message and recieved_message['action'] == 'msg'\
        #         and 'time' in recieved_message and isinstance((recieved_message['time']), float):
        #     resp = {'responce': 200,
        #             'time': time.time()
        #             }
        #     return '111'


        else:
            return {'responce': 400,
                    'error': 'Неверный запрос'}


if __name__ == '__main__':

    server = Server()
    # Создаем словарик, где будут храниться пары username/socket
    clients = {}
    while True:
        try:
            conn = server.connection() # Проверка подключений
            clients[conn] = None
            # получаем сообщение от клиента
            message = get_message(conn)
            # из сообщения понимаем имя клиента и создаем пару username/socket
            # clients[message['user']['account_name']] = conn
            # формируем ответ
            response = preparing_responce(message)
            # отправляем ответ клиенту
            send_message(conn, response)
        except OSError as e:
            pass  # timeout вышел
        else:
            print("Получен запрос на соединение от %s" % str(server.addr))
            print(clients)
            # Добавляем клиента в список

        finally:
            # Проверить наличие событий ввода-вывода
            wait = 0
            r = []
            w = []
            try:
                r, w, e = select.select(clients.keys(), clients.keys(), [], wait)
                print('r,w,e = ', r, w, e)
                print(clients.keys())
            except:
                pass  # Ничего не делать, если какой-то клиент отключился

            requests = server.read_requests(r, clients)  # Получаем входные сообщения
            if requests:
                print(requests)
            server.write_responses(requests, w, clients)  # Выполним отправку входящих сообщений
