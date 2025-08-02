from computePrimeNumbers import (
    compute_primes,
    compute_primes_ioIntensive,
    compute_primes_ioIntensive_async,
)
from concurrent.futures import ThreadPoolExecutor
import threading
import time
import asyncio

# primeNumber = 109797044856282383


def total_execution_time(thread_end_time, thread_start_time):
    print(f"Total execution time: {thread_end_time - thread_start_time:.2f} seconds")
    return thread_end_time - thread_start_time


def worker(worker_id, primeNumber, simulateIOBound):
    thread_start_time = time.perf_counter()
    if simulateIOBound:
        compute_primes_ioIntensive(primeNumber, worker_id)
    else:
        compute_primes(primeNumber, worker_id)
    thread_end_time = time.perf_counter()
    print(
        f"Thread {worker_id} execution time: {thread_end_time - thread_start_time:.2f} seconds"
    )


# This function creates multiple threads to compute prime numbers concurrently.
# While the threads finish at simiilar times, due to the GIL, they do not run in parallel.
# This makes the runtime similar to a single-threaded implementation.
def threaded_compute_primes(numOfTasks, primeNumber, simulateIOBound):
    threads = []

    for i in range(numOfTasks):
        thread = threading.Thread(
            target=worker,
            args=(i, primeNumber, simulateIOBound),
        )
        threads.append(thread)

    total_start_time = time.perf_counter()

    for i in range(numOfTasks):
        threads[i].start()
    for i in range(numOfTasks):
        threads[i].join()

    total_end_time = time.perf_counter()
    return total_execution_time(total_end_time, total_start_time)


# This function creates multiple threads to compute prime numbers sequentially.
# However, due to joining a thread before starting a new one, each thread starts and finishes before the next one starts.
def threaded_sequential_compute_primes(numOfTasks, primeNumber, simulateIOBound):
    threads = []

    for i in range(numOfTasks):
        thread = threading.Thread(
            target=worker,
            args=(i, primeNumber, simulateIOBound),
        )
        threads.append(thread)

    total_start_time = time.perf_counter()

    for i in range(numOfTasks):
        threads[i].start()
        threads[i].join()

    total_end_time = time.perf_counter()
    return total_execution_time(total_end_time, total_start_time)


# This function uses a thread pool to compute prime numbers concurrently.
# It creates a fixed number of threads and submits tasks to the pool.
# As there is a static number of threads, we save runtime as we do not have to create and join threads for each task.
# This is useful when we may have multiple smaller tasks where creating the threads may take significant time.
def thread_pool_compute_primes(numOfThreads, numOfTasks, primeNumber, simulateIOBound):

    total_start_time = time.perf_counter()
    with ThreadPoolExecutor(max_workers=numOfThreads) as executor:
        futures = [
            executor.submit(worker, i, primeNumber, simulateIOBound)
            for i in range(numOfTasks)
        ]  # Future object is an async computation that has not completed yet

    total_end_time = time.perf_counter()
    return total_execution_time(total_end_time, total_start_time)


async def asyncio_worker(worker_id, primeNumber):
    loop = asyncio.get_running_loop()
    thread_start_time = time.perf_counter()
    await loop.run_in_executor(None, compute_primes, primeNumber, worker_id)
    thread_end_time = time.perf_counter()
    print(
        f"Thread {worker_id} execution time: {thread_end_time - thread_start_time:.2f} seconds"
    )


async def asyncio_compute_prime(worker_id, primeNumber, simulateIOBound):
    if simulateIOBound:

        await compute_primes_ioIntensive_async(primeNumber, worker_id)
    else:
        await asyncio_worker(worker_id, primeNumber)


async def asyncio_compute_primes(numOfTasks, primeNumber, simulateIOBound):
    total_start_time = time.perf_counter()
    tasks = [
        asyncio.create_task(asyncio_compute_prime(i, primeNumber, simulateIOBound))
        for i in range(numOfTasks)
    ]
    await asyncio.gather(*tasks)

    total_end_time = time.perf_counter()
    return total_execution_time(total_end_time, total_start_time)


# threaded_compute_primes(2, primeNumber)
# threaded_sequential_compute_primes(2, primeNumber)
# thread_pool_compute_primes(2, 2, primeNumber)
# asyncio.run(asyncio_compute_primes(2, primeNumber))
