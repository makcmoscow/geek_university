import socket
import select
import queue
import json

IP = '127.0.0.1'
PORT = 7777
serv_sock = socket.socket(family=socket.AF_INET, type = socket.SOCK_STREAM, proto=0)
serv_sock.setblocking(0)
serv_sock.bind((IP, PORT))
serv_sock.listen(5)
serv_sock.settimeout(0.2)
all_clients = [serv_sock]
outputs = []
message_queues = {}
named_sockets = {}




while all_clients:
    writers, readers, errors = select.select(all_clients, all_clients, [])
    for s in writers:
        if s is serv_sock:
            connection, client_address = s.accept()
            connection.setblocking(0)
            all_clients.append(connection)
            message_queues[connection] = queue.Queue()
        else:
            try:
                data = s.recv(1024)
            except OSError:
                pass
            if data:
                try:
                    data = data.decode()
                    data = json.loads(data)
                    sock_name = data['user']['account_name']
                    print(sock_name)
                except Exception as e:
                    print('error while finding username', e)
                else:
                    named_sockets[sock_name] = s
                print(named_sockets)
                # if s not in outputs:
                #     outputs.append(s)
            else:
                break
                # if s in outputs:
                #     outputs.remove(s)
                # inputs.remove(s)
                # s.close()
                # del message_queues[s]
    for s in readers:
        try:
            next_msg = message_queues[s].get_nowait()
        except queue.Empty:
            outputs.remove(s)
        else:
            s.send(next_msg)

    for s in errors:
        all_clients.remove(s)
        if s in outputs:
            outputs.remove(s)
        s.close()
        del message_queues[s]
