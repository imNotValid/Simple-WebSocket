# Simple WebSocket
![image](https://github.com/imNotValid/Simple-WebSocket/blob/f48ea8e78a3dad8075be880afb198eee171d6077/ex_image/Screenshot%20from%202022-09-04%2001-01-32.png)
 # Example
 
 ```python
from re import match
from WebSocket import WebSocket
from util.filters import event, regex, filter_ips, create
from util.types import Connection

app = WebSocket()

# ---- Filter ips - on new connection
@app.on_new_connection(filter_ips(["1.1.1.1", "1.1.1.2"]))  # Example
def on_connection(m: Connection):
    m.send("hello welcome to our server")

# ---- On event handler
@app.on_message(event("bing"))
def event_message(message: Connection):
    message.send("bong! - from event filter")

# ---- Regex filter
@app.on_message(regex("ding"))
def regex_message(message: Connection):
    message.send("dong! - from regex filter")

# ---- Create filter
def filter_hello(message: Connection):
    if match(r"(?i)hello", message.message):
        return True
    return False


filter_hello = create(filter_hello)


@app.on_message(filter_hello)
def message_hello(message: Connection):
    message.send("Hello! - from filter_hello")

# ---- On disconnect
@app.on_disconnect()
def disconnect(message: Connection):
    print(message.addr)

app.run(port=1234)
 ```
