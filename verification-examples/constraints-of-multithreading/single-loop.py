import time

def cpu_bound_task(n):
    if n <= 1:
        return n
    return cpu_bound_task(n - 1) + cpu_bound_task(n - 2)

start = time.time()

for _ in range(4):  # Running 4 tasks sequentially
    cpu_bound_task(35)

end = time.time()
print("Single-Loop Time:", end - start)
