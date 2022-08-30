# Simple WebSocket
![image](https://github.com/imNotValid/Simple-WebSocket/blob/main/Screenshot%20from%202022-08-30%2018-11-17.png)
 # Example
 
 ```python
from re import match
from WebSocket import WebSocket
from util.filters import event, regex, filter_ips, create
from util.types import Connection

app = WebSocket()

# ---- Filter ips - on new connection 
@app.on_new_connection(filter_ips("192.168.114.226")) # Example
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

app.run(port=12346)
 
 ```
