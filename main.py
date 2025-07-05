def runImplementation(implementation, numOfTasks, primeNumber):
    match implementation:
        case 1:
            from concurrentImplementations import threaded_compute_primes
            threaded_compute_primes(numOfTasks, primeNumber)
        case 2:
            from concurrentImplementations import threaded_sequential_compute_primes
            threaded_sequential_compute_primes(numOfTasks, primeNumber)
        case 3:
            from concurrentImplementations import thread_pool_compute_primes
            thread_pool_compute_primes(2, numOfTasks, primeNumber)
        case 4:
            from concurrentImplementations import asyncio_compute_primes
            import asyncio
            asyncio.run(asyncio_compute_primes(numOfTasks, primeNumber))
        case 5:
            from parallelImplementations import multiprocessing_compute_primes
            multiprocessing_compute_primes(numOfTasks, primeNumber)
        case 6:
            from parallelImplementations import multiprocessing_pool_compute_primes
            multiprocessing_pool_compute_primes(2, numOfTasks, primeNumber)
        case 7:
            from parallelImplementations import multiprocessing_pool_executor_compute_primes
            multiprocessing_pool_executor_compute_primes(numOfTasks, primeNumber)
        case _:
            return False
    return True

def printUserInstructions():
    print("This program compares different multiprocessing implementations for computing prime numbers.")
    print("It includes concurrent implementations using threads and asynchronous tasks, as well as parallel implementations using multiprocessing.")
    print("The list of implementaionts includes:")
    print("1. Threaded implementation")
    print("2. Threaded sequential implementation")
    print("3. Thread pool implementation")
    print("4. Asyncio implementation")
    print("5. Multiprocessing implementation")
    print("6. Multiprocessing Pool implementation")
    print("7. Multiprocessing PoolExecutor implementation")

def collectUserInput():
    printUserInstructions()
    numOfTasks = input("Please enter the number of tasks to run (default is 2): ")
    firstImplementation = input("Please enter the number of the implementation you want to run (1-7): ")
    secondImplementation = input("Please enter the number of the second implementation you want to run (1-7): ")
    return int(numOfTasks), int(firstImplementation), int(secondImplementation)

def main():
    printUserInstructions()
    numOfTasks, firstImplementation, secondImplementation = collectUserInput()
    while runImplementation(int(firstImplementation), numOfTasks, 109797044856282383) is False:
        firstImplementation = input("Please enter the number of the implementation you want to run (1-7): ")
    while runImplementation(int(secondImplementation), numOfTasks, 109797044856282383) is False:
        secondImplementation = input("Please enter the number of the second implementation you want to run (1-7): ")

if __name__ == "__main__":
    main()
    
    
