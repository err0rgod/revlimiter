import asyncio
from leakybucket import LeakyBucket

bucket = LeakyBucket(10,1)

bucket.addRequest(1)
bucket.addRequest(1)
bucket.addRequest(1)
bucket.addRequest(1)
bucket.addRequest(5)
bucket.addRequest(10)
bucket.addRequest(3)
bucket.addRequest(1)

