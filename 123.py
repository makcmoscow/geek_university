def send(self, payload):
    try:
        self._send(payload)
    except pika.exceptions.ConnectionClosed:
        #reconnect
        self.connect()
        self.send(payload)
