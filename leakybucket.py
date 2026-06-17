import time

class LeakyBucket:
    def __init__(self, capacity,leak_rate, interval = 1) -> None:
        self.storage = 0
        self.capacity = capacity
        self.leak_rate = leak_rate
        self.last_checked = time.time()

    def _leak(self):
        now = time.time()
        elapsed = now - self.last_check()
        leaked = elapsed * self.leak_rate
        self.storage = max(0,self.storage - leaked)
        self.last_checked = now

    def allow_request(self,requests   : int =1) -> bool:
        self._leak()
        if self.storage + requests <= self.capacity:
            self.storage += requests
            return True
        return False

    def get_remaining(self):
        self.leak()
        return int(self.capacity - self.storage)