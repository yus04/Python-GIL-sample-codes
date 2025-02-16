import time
import random

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # In each outer loop, the last i elements are already sorted
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

if __name__ == "__main__":
    random.seed(42)
    # Bubble sort has O(n^2) complexity, so use a small array size
    arr_size = 10000  
    arr = [random.randint(0, 100000) for _ in range(arr_size)]
    
    start_time = time.time()
    sorted_arr = bubble_sort(arr)
    end_time = time.time()
    
    print("Disabled-GIL Time:", end_time - start_time)
