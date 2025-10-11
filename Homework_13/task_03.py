import multiprocessing


# Function to sum one part of the array
def partial_sum(numbers: list[float]) -> float:
    return sum(numbers)


if __name__ == "__main__":
    data = list(range(1000000))  # Massive data
    n_proc = 2  # number of processes

    # Split data into chunks for each process
    chunk_size = len(data) // n_proc
    chunks = [data[i:i + chunk_size] for i in range(0, len(data), chunk_size)]

    with multiprocessing.Pool(processes=n_proc) as pool:
        results = pool.map(partial_sum, chunks)

    total = sum(results)
    print("Загальна сума:", total)
