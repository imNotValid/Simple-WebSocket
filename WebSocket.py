from socket import AF_INET, SOCK_STREAM, gethostbyname, gethostname, socket
from threading import Thread
from util.types import Connection, _decode_message


class WebSocket:
    def __init__(self, host: str = gethostbyname(gethostname()), port: int = 8000, buffer_size: int = 4096) -> None:
        self.on_message_listener, self.on_connection_listener = [], []
        self.host, self.port, self.buffer_size = host, port, buffer_size

    def on_new_connection(self, filters=None):
        def add_new_con(func):
            self.on_connection_listener.append([func, filters])
        return add_new_con

    def on_message(self, filters=None):
        def add_handler(func):
            self.on_message_listener.append([func, filters])
        return add_handler

    def __on_update(self, conn: socket, addr):
        if self.on_connection_listener:
            data = Connection(conn, addr)
            for event in self.on_connection_listener:
                try:
                    funct, filterss = event
                    if filterss:
                        data.filter_result = filterss(data)
                        if data.filter_result:
                            funct(data)
                            break
                    else:
                        funct(data)
                except Exception as e:
                    print(f"{e} - on handler -> {funct.__name__}")

        while True:
            data = _decode_message(conn.recv(self.buffer_size))
            if data:
                data = Connection(conn, addr, data)
                for event in self.on_message_listener:
                    try:
                        func, filters = event
                        if filters:
                            data.filter_result = filters(data)
                            if data.filter_result:
                                func(data)
                                break
                        else:
                            func(data)

                    except Exception as e:
                        print(f"{e} - on handler -> {func.__name__}")

    def run(self, host: str = gethostbyname(gethostname()), port: int = 8000, show_ip_after_run=True) -> None:
        self.host, self.port = host, port
        self.serv = socket(AF_INET, SOCK_STREAM)
        self.serv.bind((self.host, self.port)), self.serv.listen()
        if show_ip_after_run:
            print(host, port)
        while True:
            conn, addr = self.serv.accept()
            Thread(target=self.__on_update, args=[conn, addr]).start()
