from json import loads
from json.decoder import JSONDecodeError
from re import match

def _isit_json(data):
    try:
        return loads(data)
    except (JSONDecodeError, TypeError):
        return False

def create(func):
    def on_event(message):
        if func(message):
            return True
        return False
    return on_event

def filter_ips(ips: list[str]):
    def ip_fil(message):
        if message.ip in ips:
            return True
        return False
    return ip_fil

def regex(pattern, flags=0):
    def filter_regex(message):
        if match(pattern, message.message, flags):
            return True
        return False
    return filter_regex

def event(event_name):
    def on_event(message):
        msg = _isit_json(message.message)
        if msg:
            if "event" in msg:
                if msg["event"] == event_name:
                    return True
        return False
    return on_event
