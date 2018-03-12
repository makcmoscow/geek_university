import json

def send_message(sock, data):
    data = json.dumps(data).encode()
    sock.send(data)

