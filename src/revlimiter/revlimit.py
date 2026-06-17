from .tokenbucket import TokenBucket
from .leakybucket import LeakyBucket
from typing import Dict, Any, Union

class RateLimitManager:
    """
    Manager class to handle rate limiting for multiple clients using different algorithms.
    
    Attributes:
        algo (str): The rate limiting algorithm to use ('token-bucket' or 'leaky-bucket').
        config (Dict[str, Any]): Configuration parameters for the buckets.
        clients (Dict[str, Union[TokenBucket, LeakyBucket]]): Map of client IDs to their respective buckets.
    """

    def __init__(self, algorithm: str, **kwargs_config: Any) -> None:
        """
        Initialize the RateLimitManager.
        
        Args:
            algorithm (str): 'token-bucket' or 'leaky-bucket'.
            **kwargs_config: Configuration for the buckets (e.g., capacity, refill_rate, leak_rate).
        """
        self.algo = algorithm
        self.config = kwargs_config
        self.clients = {}

    def _create_bucket(self) -> Union[TokenBucket, LeakyBucket]:
        """
        Create a new bucket instance based on the configured algorithm.
        
        Returns:
            Union[TokenBucket, LeakyBucket]: A new bucket instance.
            
        Raises:
            ValueError: If an unknown algorithm is specified.
            KeyError: If required configuration parameters are missing.
        """
        if self.algo == "token-bucket":
            return TokenBucket(
                capacity=self.config["capacity"],
                refill_rate=self.config["refill_rate"]
            )
        elif self.algo == "leaky-bucket":
            return LeakyBucket(
                capacity=self.config["capacity"],
                leak_rate=self.config["leak_rate"]
            )
        raise ValueError(
            f"Unknown Algorithm Given: {self.algo}"
        )
    
    def get_bucket(self, client_id: str) -> Union[TokenBucket, LeakyBucket]:
        """
        Retrieve or create a rate limit bucket for a specific client.
        
        Args:
            client_id (str): Unique identifier for the client.
            
        Returns:
            Union[TokenBucket, LeakyBucket]: The bucket assigned to the client.
        """
        if client_id not in self.clients:
            self.clients[client_id] = self._create_bucket()
        return self.clients[client_id]
