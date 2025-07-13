from multiprocessing import Process, Pool
from computePrimeNumbers import compute_primes
from concurrent.futures import ProcessPoolExecutor
import time

# primeNumber = 109797044856282383


def total_execution_time(thread_end_time, thread_start_time):
    print(f"Total execution time: {thread_end_time - thread_start_time:.2f} seconds")
    return thread_end_time - thread_start_time


def worker(name, primeNumber):
    thread_start_time = time.perf_counter()
    compute_primes(primeNumber)
    thread_end_time = time.perf_counter()
    print(f"{name} execution time: {thread_end_time - thread_start_time:.2f} seconds")


def multiprocessing_compute_primes(numOfTasks, primeNumber):
    processes = []

    total_start_time = time.perf_counter()
    for i in range(numOfTasks):
        process = Process(
            target=worker,
            args=(
                f"Process-{i+1}",
                primeNumber,
            ),
        )
        processes.append(process)

    for process in processes:
        process.start()
    for process in processes:
        process.join()

    total_end_time = time.perf_counter()
    return total_execution_time(total_end_time, total_start_time)


def multiprocessing_pool_compute_primes(numOfProcesses, numOfTasks, primeNumber):

    total_start_time = time.perf_counter()
    with Pool(processes=numOfProcesses) as pool:
        pool.starmap(
            worker, [(f"Process-{i+1}", primeNumber) for i in range(numOfTasks)]
        )

    total_end_time = time.perf_counter()
    return total_execution_time(total_end_time, total_start_time)


def multiprocessing_pool_executor_compute_primes(
    numOfProcesses, numOfTasks, primeNumber
):
    total_start_time = time.perf_counter()
    with ProcessPoolExecutor(max_workers=numOfProcesses) as executor:
        futures = [
            executor.submit(worker, f"Process={i+1}", primeNumber)
            for i in range(numOfTasks)
        ]
    total_end_time = time.perf_counter()
    return total_execution_time(total_end_time, total_start_time)
