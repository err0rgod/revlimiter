from manager import RateLimitManager
import time

limiter = RateLimitManager(
    algorithm = "token-bucket",
    capacity = 10,
    refill_rate=1
)

user = limiter.get_bucket("192.8.9.8")


for i in range(10):

    if user.allow_request():
        print(f"Request {i+1}: ALLOWED")
    else:
        print(f"Request {i+1}: BLOCKED")

    time.sleep(0.5)