'''Use multiprocessing.Pool to compute the square of every number in a list of 20 integers
across 4 worker processes. Print results and compare time with a single-process version.'''

import multiprocessing

import time

def square(n):
    time.sleep(0.1)  
    return n * n

numbers = list(range(1, 21))  # 1 to 20

start = time.time()
single_results = [square(n) for n in numbers]
end = time.time()

print("Single-process results:", single_results)
print(f"Time taken (single process): {end - start:.2f} seconds\n")

start = time.time()
with multiprocessing.Pool(processes=4) as pool:
    multi_results = pool.map(square, numbers)
end = time.time()
# print(type(multi_results))
print("Multiprocessing results:", multi_results)
print(f"Time taken (4 processes): {end - start:.2f} seconds")
