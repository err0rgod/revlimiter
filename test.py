from manager import RateLimitManager
import time

limiter = RateLimitManager(
    algorithm = "leaky-bucket",
    capacity = 5,
    leak_rate=1
)

user = limiter.get_bucket("192.8.9.8")


for i in range(20):

    if user.allow_request():
        print(f"Request {i+1}: ALLOWED")
    else:
        print(f"Request {i+1}: BLOCKED")

    time.sleep(0.2)