import time

def say_hello(name, delay):
    time.sleep(delay)  # Simulates an I/O operation (using time.sleep for simplicity)
    print(f"Hello, {name}!")

# Run tasks sequentially
start = time.time()

say_hello("Alice", 2)
say_hello("Bob", 1)
say_hello("Charlie", 3)

end = time.time()
print("Single-Loop Time:", end - start)
