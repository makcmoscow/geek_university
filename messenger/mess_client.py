import socket
from shared_utils import parser, send_message, get_message
import messages


# Создаем класс Клиент, с методами отправки и получения сообщений
class Client:
    def __init__(self, host = '127.0.0.1', port = 7777, timeout=10):
        self.host = host
        self.port = port
        self.sock = socket.create_connection((host, port), timeout)

# Функция создания сообщения о присутствии


    def create_presence(self, user_name = 'guest'):
        presence = messages.f_presence()
        return presence

    def create_message(self, user_name = 'guest'):
        message = messages.f_msg()
        return message


    def translating_message(self, message):
        if message['responce'] == 200:
            return 'OK'
        elif message['responce'] == 400:
            return 'shit'


# Создаем экземпляр класса Клиент
IP, PORT = parser()
client = Client(IP, PORT)
# Отправляем сообщение о присутствии
send_message(client.sock, client.create_presence())
# Печатаем ответ от сервера
response = client.translating_message(get_message(client.sock))

print(response)
# if response == 'OK':
#     a = client.create_message()
#     print(a)
#     send_message(client.sock, a)
#     response = get_message(client.sock)
#     print(response)













