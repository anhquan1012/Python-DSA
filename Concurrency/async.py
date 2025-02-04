""" Use create_task() when:
- You want tasks to run in the background without blocking execution.
- Tasks are independent and do not require immediate results.
"""

import asyncio
import time 

async def fn():
    start_time = asyncio.get_running_loop().time()
    print("one")
    await asyncio.sleep(1)
    await fn2()
    print('four')
    await asyncio.sleep(1)
    print('five')
    await asyncio.sleep(1)
    print(f"Total execution time: {asyncio.get_running_loop().time() - start_time:.2f} seconds")
    return "Done"

async def fn2():
    await asyncio.sleep(1)
    print("two")
    await asyncio.sleep(1)
    print("three")

res = asyncio.run(fn())

print(res)
print("----------------------------------------------")

"""Use gather() when:
- You need to run multiple async tasks and wait for all to complete.
- You need to collect results from tasks.
"""
import asyncio

async def task(name, duration):
    print(f"Task {name} started...")
    await asyncio.sleep(duration)
    print(f"Task {name} completed.")
    return f"Result from Task {name}"

async def main():
    start_time = asyncio.get_running_loop().time()

    # Run multiple tasks and wait for them to complete
    results = await asyncio.gather(
        task("A", 3),
        task("B", 2),
        task("C", 1)
    )

    print(f"Results: {results}")
    print(f"Total execution time: {asyncio.get_running_loop().time() - start_time:.2f} seconds")

asyncio.run(main())

