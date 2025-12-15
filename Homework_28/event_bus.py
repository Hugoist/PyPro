class EventBus:
    def __init__(self):
        self.subscribers = {}
        self.event_log = []

    def subscribe(self, event_name, callback):
        self.subscribers.setdefault(event_name, []).append(callback)

    def unsubscribe(self, event_name, callback):
        if event_name in self.subscribers:
            self.subscribers[event_name] = [
                cb for cb in self.subscribers[event_name] if cb != callback
            ]
            if not self.subscribers[event_name]:
                del self.subscribers[event_name]

    def emit(self, event_name, data):
        self.event_log.append((event_name, data))
        for key, callbacks in self.subscribers.items():
            if self.match(event_name, key):
                for cb in callbacks:
                    try:
                        cb(data)
                    except Exception as e:
                        print(f"Error in listener {cb.__name__}: {e}")

    def get_event_log(self):
        return list(self.event_log)

    def match(self, event_name, pattern):
        if pattern.endswith(".*"):
            prefix = pattern[:-2]
            return event_name.startswith(prefix + ".")
        return event_name == pattern
