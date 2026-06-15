import asyncio

# token bucket 

max_tokens = 10
refill_rate = 2

class TokenBucket:
    def __init__(self,max_tokens) -> None:
        self.tokens = max_tokens

    def HasTokens(self):
        return self.tokens>0
    def howmany(self):
        return self.tokens
    def consume_token(self):
        if self.HasTokens():
            self.tokens-=1 

    def release_token(self):
        if self.tokens < max_tokens:
            self.tokens+=1


bucket = TokenBucket(max_tokens=max_tokens)

async def handleIncomingRequest(request_id: str):
    if not bucket.HasTokens():
        print("Too many requests, please try again later")
        return 

    print("request processing......")
    bucket.consume_token()

    return True


async def wait_for(ms):
    await asyncio.sleep(ms/1000)


async def setinterval():
    while True:
        await asyncio.sleep(refill_rate)
        if bucket.howmany()< max_tokens:
            bucket.release_token()


