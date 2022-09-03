# Simple WebSocket
 # Project Setup
```bash
git clone https://github.com/imNotValid/Simple-WebSocket
cd Simple-WebSocket
```
# Create an object
```python
from WebSocket import WebSocket
from util.types import Connection

app = WebSocket()
```
# on new connection
```python
@app.on_new_connection()  # Example
def on_connection(m: Connection):
    m.send("hello welcome to our server")
```

# on message handler
```python
@app.on_message()
def event_message(message: Connection):
    message.send("Recieved!")
```

# On disconnect
```python
@app.on_disconnect()
def disconnect(message: Connection):
    print(message.addr)
```

# list of filters
```python
from util.filters import event, regex, filter_ips

# event("bing") -> {"event": "bing"}
# regex(pattern, flags=0)
# filter_ips(list_of_ip: list or str)
```

# how to use filters
```python
@app.on_message(your filters) # [event, regex, filter_ips] or you can create new filters
def message_hello(message: Connection):
    message.send("Hello! - from filter_hello")
```

# Create filter
```python
def filter_hello(message: Connection):
    if match(r"(?i)hello", message.message):
        return True
    return False

filter_hello = create(filter_hello)
```

# run server
```python
app.run(port=1234)
```
