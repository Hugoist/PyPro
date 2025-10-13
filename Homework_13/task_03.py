import multiprocessing

if __name__ == "__main__":
    data = list(range(1000000))  # Massive data
    n_proc = 2  # number of processes

    # Split data into chunks for each process
    chunk_size = len(data) // n_proc
    chunks = [data[i:i + chunk_size] for i in range(0, len(data), chunk_size)]

    # Create a pool of processes and calculate partial sums in parallel
    with multiprocessing.Pool(processes=n_proc) as pool:
        results = pool.map(sum, chunks)

    # Combine all partial results into the final total sum
    total = sum(results)
    print("Загальна сума:", total)
