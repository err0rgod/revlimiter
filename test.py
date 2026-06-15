from main import TokenBucket, handleIncomingRequest, setinterval
import asyncio

# bucket = TokenBucket(10)
id = "1234"

async def main():
    asyncio.create_task(setinterval())
    for i in range(1,100):
        print(f"request number {i}")
        await asyncio.sleep(1)
        await handleIncomingRequest(id)


asyncio.run(main())