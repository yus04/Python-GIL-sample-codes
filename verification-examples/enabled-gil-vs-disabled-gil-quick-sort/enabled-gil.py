import time
import random

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

if __name__ == "__main__":
    random.seed(42)
    # Quick sort is a divide and conquer algorithm, so it can easily handle larger arrays
    arr_size = 1000000  
    arr = [random.randint(0, 100000) for _ in range(arr_size)]
    
    start_time = time.time()
    sorted_arr = quick_sort(arr)
    end_time = time.time()
    
    print("Enabled-GIL Time:", end_time - start_time)
