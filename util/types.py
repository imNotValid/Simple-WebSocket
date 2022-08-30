from socket import socket
from typing import Any
from util.filters import _isit_json

def _decode_message(data: bytes):
    try:
        return data.decode().strip()

    except Exception:
        return False

class Connection:
    def __init__(self, conn: socket, addr: str, message: Any = None, filter_result: Any = None) -> None:
        self.conn, self.addr = conn, addr
        self.ip, self.port = addr
        self.message, self.json = message, _isit_json(message)
        self.filter_result = filter_result

    def send(self, message: str) -> None:
        type_of_message = type(message)
        if not type_of_message is bytes:
            message = message.encode()
        self.conn.send(message)

    def recieve(self, BufferSize: int = 4096) -> bytes:
        return _decode_message(self.conn.recv(BufferSize))

    def close(self):
        self.conn.close()
