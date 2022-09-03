# Simple WebSocket
![image](https://github.com/imNotValid/Simple-WebSocket/blob/f48ea8e78a3dad8075be880afb198eee171d6077/ex_image/Screenshot%20from%202022-09-04%2001-01-32.png)
 # Project Setup
```bash
git clone https://github.com/imNotValid/Simple-WebSocket
cd Simple-WebSocket
do ...
```
# Create Object
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

# list of filter
```python
from util.filters import event, regex, filter_ips

# event("bing") -> {"event": "bing"}
# regex(pattern, flags=0)
# filter_ips(list_of_ip: list or str)
```
# how to use filters
```python
@app.on_message(your filters)
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
