from threading import Thread
import time

def cpu_bound_task(n):
    if n <= 1:
        return n
    return cpu_bound_task(n - 1) + cpu_bound_task(n - 2)

start = time.time()
results = []
threads = []

def worker(n):
    result = cpu_bound_task(n)
    results.append(result)

for _ in range(4):  # 4つのスレッドで計算
    t = Thread(target=worker, args=(35,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

end = time.time()
print("Results:", results)
print("Time:", end - start)
