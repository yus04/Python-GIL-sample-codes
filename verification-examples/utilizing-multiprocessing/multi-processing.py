from multiprocessing import Process
import time

def cpu_bound_task(n):
    if n <= 1:
        return n
    return cpu_bound_task(n - 1) + cpu_bound_task(n - 2)

if __name__ == '__main__':  # 必要なガード構文
    start = time.time()
    processes = []
    for _ in range(4):  # Creating 4 processes
        p = Process(target=cpu_bound_task, args=(35,))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    end = time.time()
    print("Multiprocessing Time:", end - start)
