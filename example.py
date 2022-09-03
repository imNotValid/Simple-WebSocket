from re import match
from WebSocket import WebSocket
from util.filters import event, regex, filter_ips, create
from util.types import Connection

app = WebSocket()


@app.on_new_connection(filter_ips(["1.1.1.1", "1.1.1.2"]))  # Example
def on_connection(m: Connection):
    m.send("hello welcome to our server")


@app.on_message(event("bing"))
def event_message(message: Connection):
    message.send("bong! - from event filter")


@app.on_message(regex("ding"))
def regex_message(message: Connection):
    message.send("dong! - from regex filter")


def filter_hello(message: Connection):
    if match(r"(?i)hello", message.message):
        return True
    return False


filter_hello = create(filter_hello)


@app.on_message(filter_hello)
def message_hello(message: Connection):
    message.send("Hello! - from filter_hello")


@app.on_disconnect()
def disconnect(message: Connection):
    print(message.addr)


app.run(port=1234)
