import threading


class EventWorker(threading.Thread):
    def __init__(self, queue, event_bus):
        super().__init__(daemon=True)
        self.queue = queue
        self.bus = event_bus

    def run(self):
        while True:
            event_name, data = self.queue.get()
            try:
                self.bus.emit(event_name, data)
            except Exception as exc:
                print("WORKER ERROR:", exc)
            finally:
                self.queue.task_done()
