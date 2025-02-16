import threading
import time
import random

def bucket_sort(arr, bucket_count=10):
    """Distribute the values of the input array into bucket_count buckets"""
    min_value = min(arr)
    max_value = max(arr)
    range_val = max_value - min_value + 1
    buckets = [[] for _ in range(bucket_count)]
    for num in arr:
        # Determine the bucket index based on the value range
        index = (num - min_value) * bucket_count // range_val
        if index == bucket_count:
            index = bucket_count - 1
        buckets[index].append(num)
    return buckets

if __name__ == "__main__":
    random.seed(42)  # Set seed for reproducibility

    # Generate a random array for testing
    arr_size = 10000000
    arr = [random.randint(0, 100000) for _ in range(arr_size)]
    bucket_count = 10

    # Distribute into buckets (this part is fast enough in single-thread)
    buckets = bucket_sort(arr, bucket_count=bucket_count)
    
    # Parallelize sorting within each bucket
    threads = []
    sorted_buckets = [None] * bucket_count

    def sort_bucket_worker(idx, bucket):
        sorted_buckets[idx] = sorted(bucket)

    start_time = time.time()
    
    for i in range(bucket_count):
        t = threading.Thread(target=sort_bucket_worker, args=(i, buckets[i]))
        threads.append(t)
        t.start()
        
    for t in threads:
        t.join()
        
    # Merge the sorted buckets
    sorted_arr = []
    for bucket in sorted_buckets:
        sorted_arr.extend(bucket)
    
    end_time = time.time()
    
    print("Time:", end_time - start_time)
