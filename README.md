# revlimiter

A simple and efficient Python library for rate limiting, implementing popular algorithms like Token Bucket and Leaky Bucket.

## Features

- **Token Bucket**: Allows for bursts of requests while maintaining a steady average rate.
- **Leaky Bucket**: Smooths out bursts by processing requests at a constant rate.
- **RateLimitManager**: Easy management of multiple clients and algorithms.
- **Type-safe**: Built with Python type hints.
- **Lightweight**: Zero external dependencies.

## Installation

```bash
pip install revlimiter
```

## Quick Start

### Using RateLimitManager

The `RateLimitManager` is the easiest way to manage rate limits for multiple users or clients.

```python
from revlimiter import RateLimitManager

# Create a manager with Token Bucket algorithm
manager = RateLimitManager(
    algorithm="token-bucket",
    capacity=10,
    refill_rate=2.0  # 2 tokens per second
)

# Get bucket for a specific client
client_id = "user_123"
bucket = manager.get_bucket(client_id)

if bucket.allow_request():
    print("Request allowed!")
else:
    print("Rate limit exceeded.")
```

### Direct Algorithm Usage

#### Token Bucket

```python
from revlimiter import TokenBucket

# 10 tokens capacity, 1 token refilled every second
bucket = TokenBucket(capacity=10, refill_rate=1.0)

if bucket.allow_request(tokens=1):
    # Process request
    pass
```

#### Leaky Bucket

```python
from revlimiter import LeakyBucket

# 5 requests capacity, leaks 1 request every 2 seconds (0.5 per sec)
bucket = LeakyBucket(capacity=5, leak_rate=0.5)

if bucket.allow_request():
    # Process request
    pass
```

## API Reference

### `TokenBucket(capacity: int, refill_rate: float)`
- `allow_request(tokens: int = 1) -> bool`: Consumes tokens and returns `True` if successful.
- `get_remaining() -> int`: Returns current available tokens.

### `LeakyBucket(capacity: int, leak_rate: float)`
- `allow_request(requests: int = 1) -> bool`: Adds requests to bucket and returns `True` if successful.
- `get_remaining() -> int`: Returns current remaining capacity.

### `RateLimitManager(algorithm: str, **kwargs_config)`
- `get_bucket(client_id: str)`: Returns a bucket for the given client.

## License

MIT License. See [LICENSE](LICENSE) for details.
