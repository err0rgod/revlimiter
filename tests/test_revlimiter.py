import unittest
import time
from revlimiter import TokenBucket, LeakyBucket, RateLimitManager

class TestTokenBucket(unittest.TestCase):
    def test_allow_request(self):
        bucket = TokenBucket(capacity=10, refill_rate=100)
        self.assertTrue(bucket.allow_request(5))
        self.assertTrue(bucket.allow_request(5))
        self.assertFalse(bucket.allow_request(1))
        
    def test_refill(self):
        bucket = TokenBucket(capacity=10, refill_rate=10)
        bucket.allow_request(10)
        self.assertFalse(bucket.allow_request(1))
        time.sleep(0.11) # Should refill at least 1 token
        self.assertTrue(bucket.allow_request(1))

class TestLeakyBucket(unittest.TestCase):
    def test_allow_request(self):
        bucket = LeakyBucket(capacity=10, leak_rate=100)
        self.assertTrue(bucket.allow_request(5))
        self.assertTrue(bucket.allow_request(5))
        self.assertFalse(bucket.allow_request(1))
        
    def test_leak(self):
        bucket = LeakyBucket(capacity=10, leak_rate=10)
        bucket.allow_request(10)
        self.assertFalse(bucket.allow_request(1))
        time.sleep(0.11) # Should leak at least 1 request
        self.assertTrue(bucket.allow_request(1))

class TestRateLimitManager(unittest.TestCase):
    def test_manager_token_bucket(self):
        manager = RateLimitManager("token-bucket", capacity=10, refill_rate=10)
        bucket1 = manager.get_bucket("user1")
        bucket2 = manager.get_bucket("user2")
        self.assertNotEqual(bucket1, bucket2)
        self.assertTrue(bucket1.allow_request(10))
        self.assertTrue(bucket2.allow_request(10))

    def test_manager_leaky_bucket(self):
        manager = RateLimitManager("leaky-bucket", capacity=5, leak_rate=1)
        bucket = manager.get_bucket("user1")
        self.assertIsInstance(bucket, LeakyBucket)

if __name__ == '__main__':
    unittest.main()
