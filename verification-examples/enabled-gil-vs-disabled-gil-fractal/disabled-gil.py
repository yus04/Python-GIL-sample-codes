from threading import Thread
import time

# Image parameters
WIDTH = 800
HEIGHT = 600
MAX_ITER = 256

# Define viewport for Mandelbrot calculation
RE_START = -2.0
RE_END = 1.0
IM_START = -1.0
IM_END = 1.0

# Shared 2D array for storing the iteration counts
fractal = [[0 for _ in range(WIDTH)] for _ in range(HEIGHT)]

def mandelbrot(c):
    z = 0
    for n in range(MAX_ITER):
        if abs(z) > 2:
            return n
        z = z * z + c
    return MAX_ITER

def render_rows(start_row, end_row):
    for y in range(start_row, end_row):
        imag = IM_START + (y / HEIGHT) * (IM_END - IM_START)
        for x in range(WIDTH):
            real = RE_START + (x / WIDTH) * (RE_END - RE_START)
            c = complex(real, imag)
            color = mandelbrot(c)
            fractal[y][x] = color

if __name__ == "__main__":
    NUM_THREADS = 4
    threads = []
    rows_per_thread = HEIGHT // NUM_THREADS

    start_time = time.time()

    # Create worker threads addressing different row ranges.
    for i in range(NUM_THREADS):
        start_row = i * rows_per_thread
        # Last thread takes all remaining rows
        end_row = (i + 1) * rows_per_thread if i != NUM_THREADS - 1 else HEIGHT
        t = Thread(target=render_rows, args=(start_row, end_row))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    end_time = time.time()

    print("Fractal rendering completed.")
    print("Disbled-GIL Time:", end_time - start_time)
