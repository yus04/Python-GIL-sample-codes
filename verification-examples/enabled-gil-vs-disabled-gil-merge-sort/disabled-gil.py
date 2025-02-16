import time
import random
from threading import Thread

# Function to perform merge sort
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Worker function for sorting chunks
def sort_worker(arr, results, index):
    merge_sort(arr)
    results[index] = arr

if __name__ == "__main__":
    NUM_THREADS = 4

    # Set the seed for the random number generator
    random.seed(42)

    # Generate a list of 1000 random numbers between 1 and 10000
    numbers = [random.randint(1, 1000000) for _ in range(1000000)]
    chunk_size = len(numbers) // NUM_THREADS
    sort_threads = []
    sort_results = [None] * NUM_THREADS

    start_time = time.time()

    # Create and start threads
    for i in range(NUM_THREADS):
        start = i * chunk_size
        end = (i + 1) * chunk_size if i != NUM_THREADS - 1 else len(numbers)
        t = Thread(target=sort_worker, args=(numbers[start:end], sort_results, i))
        sort_threads.append(t)
        t.start()

    # Wait for all threads to finish
    for t in sort_threads:
        t.join()

    sort_end_time = time.time()

    # Merge sorted chunks
    sorted_list = []
    for sorted_chunk in sort_results:
        sorted_list.extend(sorted_chunk)
    merge_sort(sorted_list)

    # Print results
    # print("Results:", sorted_list)
    print("Disabled-GIL Time:", sort_end_time - start_time)
