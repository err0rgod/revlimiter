from tokenbucket import TokenBucket
from leakybucket import LeakyBucket

class RateLimitManager:

    def __init__(self,algorithm : str, **kwargs_config):
        self.algo = algorithm
        self.config = kwargs_config
        self.clients = {}

    def _create_bucket(self):
        if self.algo == "token-bucket":
            return TokenBucket(
                capacity=self.config["capacity"],
                refill_rate= self.config["refill_rate"]
            )
        elif self.algo == "leaky-bucket":
            return LeakyBucket(
                capacity= self.config["capacity"],
                leak_rate= self.config["leak_rate"]
            )
        raise ValueError(
            f"Unknown Algorithm Given : {self.algo}"
        )
    
    def get_bucket(self, client_id : str):
        if client_id not in self.clients:
            self.clients[client_id] = self._create_bucket()
        return self.clients[client_id]
        