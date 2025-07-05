from computePrimeNumbers import compute_primes
from concurrent.futures import ThreadPoolExecutor
import threading
import time
import asyncio

primeNumber = 109797044856282383

def worker(name):
    thread_start_time = time.perf_counter()
    compute_primes(primeNumber)
    thread_end_time = time.perf_counter()  
    print(f"{name} execution time: {thread_end_time - thread_start_time:.2f} seconds")

#This function creates multiple threads to compute prime numbers concurrently.
#While the threads finish at simiilar times, due to the GIL, they do not run in parallel.
#This makes the runtime similar to a single-threaded implementation.
def threaded_compute_primes(numOfTasks, primeNumber):
    threads = []

    for i in range(numOfTasks):
        thread = threading.Thread(target=worker, args=(primeNumber,))
        threads.append(thread)

    total_start_time = time.perf_counter()

    for i in range(numOfTasks):
        threads[i].start()
    for i in range(numOfTasks):
        threads[i].join()

    total_end_time = time.perf_counter()
    print("Total thread time: {:.2f} seconds".format(total_end_time - total_start_time))   

# This function creates multiple threads to compute prime numbers sequentially.
# However, due to joining a thread before starting a new one, each thread starts and finishes before the next one starts.
def threaded_sequential_compute_primes(numOfTasks, primeNumber):
    threads = []

    for i in range(numOfTasks):
        thread = threading.Thread(target=worker, args=(primeNumber,))
        threads.append(thread)

    total_start_time = time.perf_counter()

    for i in range(numOfTasks):
        threads[i].start()
        threads[i].join()
        

    total_end_time = time.perf_counter()
    print("Total thread time: {:.2f} seconds".format(total_end_time - total_start_time))   


# This function uses a thread pool to compute prime numbers concurrently.
# It creates a fixed number of threads and submits tasks to the pool.
# As there is a static number of threads, we save runtime as we do not have to create and join threads for each task.
# This is useful when we may have multiple smaller tasks where creating the threads may take significant time.
def thread_pool_compute_primes(numOfThreads, numOfTasks, primeNumber):

    total_start_time = time.perf_counter()
    with ThreadPoolExecutor(max_workers=numOfThreads) as executor:
        futures = [executor.submit(worker, primeNumber) for _ in range(numOfTasks)]#Future object is an async computation that has not completed yet
        
    total_end_time = time.perf_counter()
    print("Total thread time: {:.2f} seconds".format(total_end_time - total_start_time))   



async def asyncio_computer_prime(threadNum):
    await worker(threadNum)
    # await asyncio.to_thread(worker, threadNum)


#This function creates multiple asynchronous tasks to compute prime numbers concurrently.
#It uses asyncio to run the tasks in an event loop.
async def asyncio_compute_primes(numOfTasks, primeNumber):
    total_start_time = time.perf_counter()
    tasks = [asyncio.create_task(asyncio_computer_prime(_)) for _ in range(numOfTasks)]
    await asyncio.gather(*tasks)

    total_end_time = time.perf_counter()
    print("Total thread time: {:.2f} seconds".format(total_end_time - total_start_time))   





# threaded_compute_primes(2, primeNumber)
# threaded_sequential_compute_primes(2, primeNumber)
# thread_pool_compute_primes(2, 2, primeNumber)
# asyncio.run(asyncio_compute_primes(2, primeNumber))







