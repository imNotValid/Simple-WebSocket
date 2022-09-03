from socket import AF_INET, SOCK_STREAM, gethostbyname, gethostname, socket
from threading import Thread
from util.types import Connection, _decode_message


class WebSocket:
    def __init__(self, host: str = gethostbyname(gethostname()), port: int = 8000, buffer_size: int = 4096) -> None:
        self._on_message_listener, self._on_disconnect_listener, self._on_connection_listener = [], [], []
        self.host, self.port, self.buffer_size = host, port, buffer_size

    def on_new_connection(self, filters=None):
        def add_handler(func):
            self._on_connection_listener.append([func, filters])
        return add_handler

    def on_disconnect(self, filters=None):
        def add_handler(func):
            self._on_disconnect_listener.append([func, filters])
        return add_handler

    def on_message(self, filters=None):
        def add_handler(func):
            self._on_message_listener.append([func, filters])
        return add_handler

    @staticmethod
    def _run_listeners(list_of_listeners, *args, **kwargs):
        if list_of_listeners:
            data = Connection(*args, **kwargs)
            for event in list_of_listeners:
                try:
                    func, filters = event
                    if filterss:
                        fr = data.filter_result = filters(data)
                        if fr:
                            func(data)
                            break
                    else:
                        func(data)
                except Exception as e:
                    print(f"{e} - on handler -> {funct.__name__}")

    def _on_update(self, conn: socket, addr):
        self._run_listeners(self._on_connection_listener, conn, addr)
        while True:
            try:
                data = _decode_message(conn.recv(self.buffer_size))
                if data:
                    self._run_listeners(self._on_message_listener, conn, addr, data)
            except OSError:
                self._run_listeners(self._on_disconnect_listener, conn, addr)
                break

    def run(self, host: str = gethostbyname(gethostname()), port: int = 8000, show_ip_after_run=True) -> None:
        self.host, self.port = host, port
        self.serv = socket(AF_INET, SOCK_STREAM)
        self.serv.bind((self.host, self.port)), self.serv.listen()
        if show_ip_after_run:
            print(host, port)
        while True:
            conn, addr = self.serv.accept()
            Thread(target=self._on_update, args=[conn, addr]).start()
