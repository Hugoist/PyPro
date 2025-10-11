import multiprocessing
import random
from typing import Tuple


# Function to simulate one organism's life
def organism_life(org_id: int) -> Tuple[int, bool, int]:
    survived: bool = random.choice([True, False])
    offspring: int = random.randint(0, 3) if survived else 0
    return (org_id, survived, offspring)


if __name__ == "__main__":
    population_size = 5
    generations = 3

    population = range(1, population_size)

    for gen in range(1, generations + 1):
        print(f"Покоління {gen}")

        # Parallel processing with multiprocessing Pool
        with multiprocessing.Pool() as pool:
            results = pool.map(organism_life, population)

        # Display results
        for org_id, survived, offspring in results:
            status = "вижив" if survived else "не вижив"
            print(f"Організм {org_id}: {status}, кількість нащадків: {offspring}")

        # Create next generation
        new_population = []
        for org_id, survived, offspring in results:
            if survived:
                new_population.append(org_id)
                new_population.extend([f"{org_id}-{i}" for i in range(offspring)])
        population = new_population
        print(f"Розмір популяції: {len(population)}\n")
