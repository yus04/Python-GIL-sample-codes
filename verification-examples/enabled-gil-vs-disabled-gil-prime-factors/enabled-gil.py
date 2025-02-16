import time
from threading import Thread

# Function to compute prime factors
def prime_factors(n):
    factors = []
    i = 2
    while i * i <= n:
        while n % i == 0:
            factors.append(i)
            n //= i
        i += 1
    if n > 1:
        factors.append(n)
    return factors

# Worker function to process a list of numbers
def factor_worker(numbers, results, index):
    results[index] = [prime_factors(n) for n in numbers]

if __name__ == "__main__":
    NUM_THREADS = 4

    # List of numbers to factorize
    numbers = [
        12345678910123, 98765432111237, 11111111111347, 22222222222459,
        33333333333571, 44444444444683, 55555555555797, 66666666666911,
        77777777777023, 88888888888137, 99999999999241, 101010101010351,
        121212121212467, 131313131313577, 141414141414683, 151515151515797,
        161616161616911, 171717171717023, 181818181818137, 191919191919241,
        202020202020351, 212121212121467, 222222222222577, 232323232323683,
        242424242424797, 252525252525911, 262626262626023, 272727272727137,
        282828282828241, 292929292929351, 303030303030467, 313131313131577,
        323232323232683, 333333333333797, 343434343434911, 353535353535023,
        363636363636137, 373737373737241, 383838383838351, 393939393939467
    ]
    chunk_size = len(numbers) // NUM_THREADS
    factor_threads = []
    factor_results = [None] * NUM_THREADS

    start_time = time.time()

    # Create and start threads
    for i in range(NUM_THREADS):
        start = i * chunk_size
        end = (i + 1) * chunk_size
        t = Thread(target=factor_worker, args=(numbers[start:end], factor_results, i))
        factor_threads.append(t)
        t.start()

    # Wait for all threads to finish
    for t in factor_threads:
        t.join()

    factor_end_time = time.time()

    # Print results
    # print("Results:", factor_results)
    print("Enabled-GIL Time:", factor_end_time - start_time)
