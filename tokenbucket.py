# token bucket 
import time

class TokenBucket:
    def __init__(self, capacity : int , refill_rate : float) -> None:
        self.capacity = capacity
        self.refill_rate = refill_rate
        self.tokens = capacity
        self.last_refill = time.time()

    def _refill(self):
        now  = time.time()
        elapsed = now - self.last_refill
        new_tokens = elapsed * self.refill_rate
        self.tokens = min(self.capacity, self.tokens + new_tokens)
        self.last_refill = now


    def allow_request(self, token : int = 1) -> bool:
        self._refill()
        if self.tokens >= token:
            self.tokens-=token 
            return True
        return False
    

    def get_remaining(self):
        self._refill()
        return int(self.tokens)



