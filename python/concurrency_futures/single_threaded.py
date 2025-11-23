import time
from concurrent.futures import ProcessPoolExecutor

def sum_of_squares(n):
    return sum(i*i for i in range(n))

if __name__ == "__main__":
    numbers = [10_000_000, 20_000_000, 30_000_000, 40_000_000]

    start = time.time()

    with ProcessPoolExecutor() as executor:
        results = list(executor.map(sum_of_squares, numbers))

    # results = [sum_of_squares(n) for n in numbers]
    end = time.time()

    print(f"Results: {results}")
    print(f"Single-threaded time: {end - start:.2f} seconds")
