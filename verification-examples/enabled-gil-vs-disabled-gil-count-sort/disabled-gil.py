import threading
import time
import random

def count_worker(subarr, local_count, max_val):
    """Count the occurrences of each number in the subarray into local_count"""
    for num in subarr:
        local_count[num] += 1

if __name__ == "__main__":
    random.seed(42)  # Set seed for reproducibility
    
    NUM_THREADS = 4
    arr_size = 10000000
    # Generate a random array of non-negative integers (values from 0 to max_value)
    max_value = 10000000
    arr = [random.randint(0, max_value) for _ in range(arr_size)]
    
    # Prepare a local count array for each thread
    local_counts = [[0] * (max_value + 1) for _ in range(NUM_THREADS)]
    threads = []
    chunk_size = len(arr) // NUM_THREADS
    
    start_time = time.time()
    
    # Split the array and count in each thread
    for i in range(NUM_THREADS):
        start = i * chunk_size
        end = (i + 1) * chunk_size if i != NUM_THREADS - 1 else len(arr)
        t = threading.Thread(target=count_worker, args=(arr[start:end], local_counts[i], max_value))
        threads.append(t)
        t.start()
    
    for t in threads:
        t.join()
    
    # Combine the local counts from each thread
    final_count = [0] * (max_value + 1)
    for value in range(max_value + 1):
        for i in range(NUM_THREADS):
            final_count[value] += local_counts[i][value]
    
    # Generate the sorted array from the aggregated counts
    sorted_arr = []
    for value, freq in enumerate(final_count):
        if freq:
            sorted_arr.extend([value] * freq)
    
    end_time = time.time()
    
    print("Disabled-GIL Time:", end_time - start_time)
