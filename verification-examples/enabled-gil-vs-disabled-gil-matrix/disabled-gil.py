import time
from threading import Thread
import random

# Matrix dimensions
M = 300  # Number of rows in A and C
N = 300  # Number of columns in A and rows in B
P = 300  # Number of columns in B and C

def generate_matrix(rows, cols):
    return [[random.randint(1, 10) for _ in range(cols)] for _ in range(rows)]

# Generate random matrices A and B.
A = generate_matrix(M, N)
B = generate_matrix(N, P)

# Pre-allocate result matrix C with zeros.
C = [[0 for _ in range(P)] for _ in range(M)]

def multiply_chunk(start_row, end_row):
    for i in range(start_row, end_row):
        for j in range(P):
            acc = 0
            for k in range(N):
                acc += A[i][k] * B[k][j]
            C[i][j] = acc

if __name__ == "__main__":
    NUM_THREADS = 4
    threads = []
    rows_per_thread = M // NUM_THREADS

    start_time = time.time()

    # Create worker threads to compute matrix multiplication in chunks.
    for i in range(NUM_THREADS):
        start_row = i * rows_per_thread
        # Ensure last thread processes all remaining rows.
        end_row = (i + 1) * rows_per_thread if i != NUM_THREADS - 1 else M
        t = Thread(target=multiply_chunk, args=(start_row, end_row))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    end_time = time.time()

    print("Disabled-GIL Time:", end_time - start_time)
