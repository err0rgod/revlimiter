import time

class TokenBucket:
    """
    Implementation of the Token Bucket algorithm for rate limiting.
    
    The token bucket algorithm allows for bursts of requests while maintaining
    a steady average rate.
    
    Attributes:
        capacity (int): Maximum number of tokens the bucket can hold.
        refill_rate (float): Number of tokens added to the bucket per second.
        tokens (float): Current number of tokens in the bucket.
        last_refill (float): Timestamp of the last token refill.
    """
    
    def __init__(self, capacity: int, refill_rate: float) -> None:
        """
        Initialize the Token Bucket.
        
        Args:
            capacity (int): Maximum bucket capacity.
            refill_rate (float): Rate at which tokens are added per second.
        """
        self.capacity = capacity
        self.refill_rate = refill_rate
        self.tokens = float(capacity)
        self.last_refill = time.time()

    def _refill(self) -> None:
        """Add new tokens to the bucket based on elapsed time."""
        now = time.time()
        elapsed = now - self.last_refill
        new_tokens = elapsed * self.refill_rate
        self.tokens = min(self.capacity, self.tokens + new_tokens)
        self.last_refill = now

    def allow_request(self, tokens: int = 1) -> bool:
        """
        Check if a request can be allowed and consume tokens.
        
        Args:
            tokens (int): Number of tokens to consume. Defaults to 1.
            
        Returns:
            bool: True if tokens were consumed and request is allowed, False otherwise.
        """
        self._refill()
        if self.tokens >= tokens:
            self.tokens -= tokens
            return True
        return False

    def get_remaining(self) -> int:
        """
        Get the current number of available tokens.
        
        Returns:
            int: Number of whole tokens remaining.
        """
        self._refill()
        return int(self.tokens)
