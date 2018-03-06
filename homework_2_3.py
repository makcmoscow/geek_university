import json

class JIMMessage():
    def __init__(self, value):
        data = json.dumps(value).encode()
        return data


class JIMResponse():
    pass

class Client():
    pass

class Chat():
    pass

class ChatController():
    pass

class ChatGraph():
    pass

class Server():
    pass

class Storage():
    pass

class FileStorage(Storage):
    pass
