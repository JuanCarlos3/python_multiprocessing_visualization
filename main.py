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
            from parallelImplementations import (
                multiprocessing_pool_executor_compute_primes,
            )

            multiprocessing_pool_executor_compute_primes(2, numOfTasks, primeNumber)
        case _:
            return False
    return True


def printUserInstructions():
    print(
        "This program compares different multiprocessing implementations for computing prime numbers."
    )
    print(
        "It includes concurrent implementations using threads and asynchronous tasks, as well as parallel implementations using multiprocessing."
    )
    print("The list of implementations includes:")
    print("1. Threaded implementation")
    print("2. Threaded sequential implementation")
    print("3. Thread pool implementation")
    print("4. Asyncio implementation")
    print("5. Multiprocessing implementation")
    print("6. Multiprocessing Pool implementation")
    print("7. Multiprocessing PoolExecutor implementation")


def convertUserInputToInteger(userInput, defaultValue):
    if not userInput:
        print(f"Empty Input. Defaulting to {defaultValue}.")
        return defaultValue
    try:
        return int(userInput)
    except ValueError:
        print(f"Invalid input. Defaulting to {defaultValue}.")
        return defaultValue


def collectUserInput():
    printUserInstructions()
    primeInput = input(
        "Please enter the prime number to compute (default is 109797044856282383): "
    )
    primeToCompute = convertUserInputToInteger(primeInput, 109797044856282383)
    tasksInput = input("Please enter the number of tasks to run (default is 2): ")
    numOfTasks = convertUserInputToInteger(tasksInput, 2)
    firstImplementationInput = input(
        "Please enter the number of the implementation you want to run (1-7): "
    )
    firstImplementation = convertUserInputToInteger(firstImplementationInput, 1)
    secondImplementationInput = input(
        "Please enter the number of the second implementation you want to run (1-7): "
    )
    secondImplementation = convertUserInputToInteger(secondImplementationInput, 2)
    return primeToCompute, numOfTasks, firstImplementation, secondImplementation


def main():
    primeToCompute, numOfTasks, firstImplementation, secondImplementation = (
        collectUserInput()
    )
    while runImplementation(firstImplementation, numOfTasks, primeToCompute) is False:
        firstImplementation = input(
            "Please enter the number of the implementation you want to run (1-7): "
        )
    while runImplementation(secondImplementation, numOfTasks, primeToCompute) is False:
        secondImplementation = input(
            "Please enter the number of the second implementation you want to run (1-7): "
        )


if __name__ == "__main__":
    main()
