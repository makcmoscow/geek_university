import socket
from shared_utils import parser, send_message, get_message
import messages

# my_login = input('Input your login: ')
my_login = 'max'
# Создаем класс Клиент, с методами отправки и получения сообщений
class Client:
    def __init__(self, host = '127.0.0.1', port = 7777, timeout=10):
        self.host = host
        self.port = port
        self.sock = socket.create_connection((host, port), timeout)

    # Функция создания сообщения о присутствии
    def create_presence(self, user_name = 'guest'):
        presence = messages.f_presence(user_name)
        return presence

    def create_message(self, user_name = 'guest'):
        message = messages.f_msg(user_name)
        return message


    def translating_message(self, message):
        print(message)
        for key, val in message.items():
            if key == 'responce' and val == 200:
                self.what_will_we_do(key)

            elif key == 'msg':
                self.what_will_we_do(key)




    def what_will_we_do(self, type_msg):
        print(type_msg)
        if type_msg == 'responce':
            print('goind for input msg')
        elif type_msg == 'msg':
            print('going to print msg')






# Создаем экземпляр класса Клиент
IP, PORT = parser()
client = Client(IP, PORT)
presence = client.create_presence(my_login)

# Отправляем сообщение о присутствии
send_message(client.sock, presence)
# Печатаем ответ от сервера
response = get_message(client.sock)
type_msg = client.translating_message(response)

while 1:
    message = messages.f_msg(my_login)
    print(message)
    # message['message'] = input('.....')
    message['message'] = '.....'
    message['to'] = 'For who?'
    # message['to'] = input('For who?')
    print('sending')
    try:
        send_message(client.sock, message)
        print('sended')
    except:
        pass
    try:
        resp = get_message(client.sock)
        print(resp)
    except:
        pass



















