import socket
import time
import select
from shared_utils import parser, send_message, get_message

IP, PORT = parser()

class Server:
    # Инициализируем входные данные и создаем серверный сокет
    def __init__(self):
        self.server_sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM, proto=0)  # TCP
        self.server_sock.bind((IP, PORT))
        self.server_sock.listen(5)
        self.server_sock.settimeout(0.2)


    def connection(self):
        self.sock, addr = server.server_sock.accept()
        return self.sock

    def read_requests(self, r_clients, all_clients):
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
                message = get_message(sock)
                # Добавляем их в список
                # В идеале нам нужно сделать еще проверку, что сообщение нужного формата прежде чем его пересылать!
                # Пока оставим как есть, этим займемся позже
                messages.append(message)
            except:
                print('Клиент {} {} отключился'.format(sock.fileno(), sock.getpeername()))
                all_clients.remove(sock)

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
                    all_clients.remove(sock)

    def preparing_responce(self, recieved_message):
        if 'action' in recieved_message and recieved_message['action'] == 'presence'\
                and 'time' in recieved_message and isinstance((recieved_message['time']), float):
            return {'responce': 200,
                    'time': time.time()
                    }

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
    clients = []
    while True:
        try:
            conn, addr = server.server_sock.accept() # Проверка подключений
            # получаем сообщение от клиента
            message = get_message(conn)
            # формируем ответ
            response = server.preparing_responce(message)
            print(response)
            # отправляем ответ клиенту
            send_message(conn, response)
        except OSError as e:
            pass  # timeout вышел
        else:
            print("Получен запрос на соединение от %s" % str(addr))
            # Добавляем клиента в список
            clients.append(conn)
        finally:
            # Проверить наличие событий ввода-вывода
            wait = 0
            r = []
            w = []
            try:
                r, w, e = select.select(clients, clients, [], wait)
            except:
                pass  # Ничего не делать, если какой-то клиент отключился

            requests = server.read_requests(r, clients)  # Получаем входные сообщения
            server.write_responses(requests, w, clients)  # Выполним отправку входящих сообщений
