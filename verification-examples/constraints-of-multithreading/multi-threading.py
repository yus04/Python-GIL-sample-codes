from threading import Thread
import time

def cpu_bound_task(n):
    if n <= 1:
        return n
    return cpu_bound_task(n - 1) + cpu_bound_task(n - 2)

start = time.time()
threads = []
for _ in range(4):  # Creating 4 threads
    t = Thread(target=cpu_bound_task, args=(35,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

end = time.time()
print("Multithreading Time:", end - start)
