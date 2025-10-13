import multiprocessing
import math
from functools import reduce
import operator


def partial_factorial(start: int, end: int) -> int:
    """ Calculate the partial factorial """
    result = 1
    for i in range(start, end + 1):
        result *= i
    return result


if __name__ == "__main__":
    n = 100000
    n_proc = 4

    # Split range 1 to n into chunks for each process
    chunk_size = n // n_proc
    ranges = []
    for i in range(n_proc):
        start = i * chunk_size + 1
        end = (i + 1) * chunk_size if i != n_proc - 1 else n
        ranges.append((start, end))

    # Compute partial factorials in parallel
    with multiprocessing.Pool(processes=n_proc) as pool:
        partial_results = pool.starmap(partial_factorial, ranges)

    # Multiply partial results to get the final factorial
    factorial_result = reduce(operator.mul, partial_results, 1)
    digits = int(math.log10(factorial_result)) + 1

    print(f"Approximate order of factorial: 10^{digits - 1}")
