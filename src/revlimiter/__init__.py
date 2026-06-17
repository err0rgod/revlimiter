"""
revlimiter - A simple and efficient rate limiting library.

This package provides implementations of common rate limiting algorithms
including Token Bucket and Leaky Bucket, along with a manager to handle
multiple clients.
"""

from .revlimit import RateLimitManager

from .tokenbucket import TokenBucket
from .leakybucket import LeakyBucket

__all__ = ["RateLimitManager", "TokenBucket", "LeakyBucket"]
