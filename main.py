import asyncio

# token bucket 

max_tokens = 10
refill_rate = 10

class TokenBucket:
    def __init__(self,max_tokens) -> None:
        self.tokens = max_tokens

    def HasTokens(self):
        return self.tokens>0
    def consume_token(self):
        if self.HasTokens():
            self.tokens-=1 

    def release_token(self):
        if self.tokens < max_tokens:
            self.tokens+=1


bucket = TokenBucket(max_tokens=max_tokens)

async def handleIncomingRequest(request_id: str):
    if not bucket.hastokens():
        print("Too many requests, please try again later")
        return 

    bucket.consume_token()
    print("request processibg......")

    return True


async def wait_for(ms):
    await asyncio.sleep(ms/1000)


async def setinterval():
    while True:
        await asyncio.sleep(5)
        if bucket.HasTokens< max_tokens:
            bucket.release_token()