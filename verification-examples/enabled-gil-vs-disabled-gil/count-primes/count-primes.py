from threading import Thread
import time  

def is_prime(n):  
    if n <= 1:  
        return False  
    if n <= 3:  
        return True  
    if n % 2 == 0 or n % 3 == 0:  
        return False  
    i = 5  
    while i * i <= n:  
        if n % i == 0 or n % (i + 2) == 0:  
            return False  
        i += 6  
    return True 

def count_primes(start, end):  
    count = 0  
    for n in range(start, end):  
        if is_prime(n):  
            count += 1  
    return count  
  
def worker(start, end, result, index):  
    count = count_primes(start, end)  
    result[index] = count  
  
if __name__ == "__main__":  
    RANGE = 2000000  
    NUM_THREADS = 4  
  
    threads = []  
    results = [0] * NUM_THREADS  
    chunk_size = RANGE // NUM_THREADS  
  
    start_time = time.time()  
  
    for i in range(NUM_THREADS):  
        start = i * chunk_size  
        end = (i + 1) * chunk_size  
        t = Thread(target=worker, args=(start, end, results, i))  
        threads.append(t)  
        t.start()  
  
    for t in threads:  
        t.join()  
  
    total_primes = sum(results)  
    end_time = time.time()  
  
    print(f"Total Primes: {total_primes}")  
    print("Time:", end_time - start_time)  
