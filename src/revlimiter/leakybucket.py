import time

class LeakyBucket:
    """
    Implementation of the Leaky Bucket algorithm for rate limiting.
    
    The leaky bucket algorithm smooths out bursts by processing requests
    at a constant rate.
    
    Attributes:
        capacity (int): Maximum capacity of the bucket.
        leak_rate (float): Rate at which the bucket leaks per second.
        storage (float): Current amount of data/requests in the bucket.
        last_checked (float): Timestamp of the last leak check.
    """
    
    def __init__(self, capacity: int, leak_rate: float) -> None:
        """
        Initialize the Leaky Bucket.
        
        Args:
            capacity (int): Maximum bucket capacity.
            leak_rate (float): Rate at which requests leak out per second.
        """
        self.storage = 0.0
        self.capacity = capacity
        self.leak_rate = leak_rate
        self.last_checked = time.time()

    def _leak(self) -> None:
        """Remove leaked amount from storage based on elapsed time."""
        now = time.time()
        elapsed = now - self.last_checked
        leaked = elapsed * self.leak_rate
        self.storage = max(0.0, self.storage - leaked)
        self.last_checked = now

    def allow_request(self, requests: int = 1) -> bool:
        """
        Check if a request can be added to the bucket.
        
        Args:
            requests (int): Number of requests to add. Defaults to 1.
            
        Returns:
            bool: True if request is added and allowed, False if bucket is full.
        """
        self._leak()
        if self.storage + requests <= self.capacity:
            self.storage += requests
            return True
        return False

    def get_remaining(self) -> int:
        """
        Get the remaining capacity of the bucket.
        
        Returns:
            int: Number of additional requests the bucket can hold.
        """
        self._leak()
        return int(self.capacity - self.storage)
