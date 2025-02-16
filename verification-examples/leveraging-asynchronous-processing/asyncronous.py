import asyncio
import time

async def say_hello(name, delay):
    await asyncio.sleep(delay)  # Simulates an I/O operation
    print(f"Hello, {name}!")

async def main():
    start = time.time()  # Start time
    # Run tasks concurrently
    await asyncio.gather(
        say_hello("Alice", 2),
        say_hello("Bob", 1),
        say_hello("Charlie", 3)
    )
    end = time.time()  # End time
    print(f"Asyncronous Time: {end - start} seconds")

asyncio.run(main())
