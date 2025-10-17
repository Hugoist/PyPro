import asyncio


async def producer(queue):
    """Adds 5 tasks to the queue with a 1-second delay."""
    for i in range(5):
        await asyncio.sleep(1)
        task = f"Task-{i + 1}"
        await queue.put(task)
        print(f"Produced: {task}")


async def consumer(queue, name):
    """Consumes tasks from the queue with a 2-second delay per task."""
    while True:
        task = await queue.get()
        print(f"{name} processing {task}")
        await asyncio.sleep(2)
        print(f"{name} finished {task}")
        queue.task_done()


async def main():
    """Runs producer and multiple consumers concurrently."""
    queue = asyncio.Queue()
    producers = [asyncio.create_task(producer(queue))]
    consumers = [asyncio.create_task(consumer(queue, f"Consumer-{i + 1}")) for i in range(2)]

    await asyncio.gather(*producers)
    await queue.join()  # Wait until all tasks are processed

    for c in consumers:
        c.cancel()  # Stop consumers after all tasks are done


if __name__ == "__main__":
    asyncio.run(main())
