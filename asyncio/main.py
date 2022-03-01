import asyncio
import time

async def async_sleep():
    await asyncio.sleep(2)
    # with open('async_output.txt', 'w') as writer:
    #     writer.write('Finished long running process')

async def main():
    task1 = asyncio.create_task(async_sleep())
    task2 = asyncio.create_task(async_sleep())

    print(f"started at {time.strftime('%X')}")

    # await async_sleep()
    # await async_sleep()

    await task1
    await task2

    print(f"finished at {time.strftime('%X')}")

asyncio.run(main())
