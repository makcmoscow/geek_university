import socket
import select
import queue
import json
import time

IP = '127.0.0.1'
PORT = 7777
serv_sock = socket.socket(family=socket.AF_INET, type = socket.SOCK_STREAM, proto=0)
serv_sock.setblocking(0)
serv_sock.bind((IP, PORT))
serv_sock.listen(5)
serv_sock.settimeout(0.2)
all_clients = []
messages = []
named_sockets = {}
writers = []
readers = []
def get_name_socket(socket):
    for name, sock in named_sockets.items():
        if sock == socket:
            return name
        else:
            pass

def get_names(mess):
    name_from = None
    name_to = None
    try:
        name_from = str(mess['user']['account_name'])
    except Exception as e:
        try:
            name_from = str(mess['from'])
        except Exception as e:
            print('name_from_error', e)
            name_from = None
    else:
        try:
            name_to = str(mess['to'])
        except Exception as e:
            print('this mess haven\'t name_to')
            name_to = None
    return name_from, name_to

def get_message(sock):
    jbmess = sock.recv(1024)
    if jbmess:
        jmess = jbmess.decode()
        mess = json.loads(jmess)
        return mess
    else:
        pass

def send_message(message):
    sock = named_sockets[message.name_to]
    mess = message.message
    data = json.dumps(mess).encode()
    sock.sendall(data)

# def send_message(message, messages, reader):
#     if message.name_to

class Message:
    def __init__(self, sock, name_from, name_to, message):
        self.sock = sock
        self.name_from = name_from
        self.name_to = name_to
        self.message = message




while 1:
    try:
        conn, addr = serv_sock.accept()
        # conn.setblocking(0)
        all_clients.append(conn)
    except OSError as e:
        pass
    else:
        all_clients.append(conn)
    finally:
        try:
            writers, readers, errors = select.select(all_clients, all_clients, [])
        except Exception as e:
            pass
        else:
            for writer in writers:
                try:
                    mess = get_message(writer)
                    if mess:
                        name_from, name_to = get_names(mess)
                        message = Message(writer, name_from, name_to, mess)
                        print(message.message)
                        messages.append(message)
                        print(messages)
                    else:
                        pass
                except Exception as e:
                    print('get_message error', e)
                    pass
            for reader in readers:
                name_to = get_name_socket(reader)
                for message in messages:
                    try:
                        if message.name_to == name_to:
                            send_message(message)
                        else:
                            pass
                    except Exception as e:
                        # print('sending failed, name_to doesn\'t exist')
                        pass



    #
    #
    #
    #
    #         if data:
    #             try:
    #                 data = data.decode()
    #                 time.sleep(1)
    #                 data = json.loads(data)
    #                 sock_name = data['user']['account_name']
    #                 print(sock_name)
    #             except Exception as e:
    #                 print('error while finding username', e)
    #                 data = None
    #             else:
    #                 named_sockets[sock_name] = writer
    #             print(named_sockets)
    #             # if s not in outputs:
    #             #     outputs.append(s)
    #         else:
    #             break
    #             # if s in outputs:
    #             #     outputs.remove(s)
    #             # inputs.remove(s)
    #             # s.close()
    #             # del message_queues[s]
    # for writer in readers:
    #     try:
    #         next_msg = message_queues[writer].get_nowait()
    #         print(next_msg)
    #     except queue.Empty:
    #         pass
    #         # print('there is no message for this socket')
    #
    #     else:
    #         writer.send(next_msg)
    #
    # for writer in errors:
    #     all_clients.remove(writer)
    #     if writer in outputs:
    #         outputs.remove(writer)
    #     writer.close()
    #     del message_queues[writer]