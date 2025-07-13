import plotext as plt
from concurrentImplementations import (
    threaded_compute_primes,
    threaded_sequential_compute_primes,
    thread_pool_compute_primes,
    asyncio_compute_primes,
)
from parallelImplementations import (
    multiprocessing_compute_primes,
    multiprocessing_pool_compute_primes,
    multiprocessing_pool_executor_compute_primes,
)
import asyncio
from enum import Enum


invalidOption = -1
quitProgramAndGenerateReport = -2
implementationsRequiringPoolSize = [
    3,
    6,
    7,
]  # Implementations that require pool size input


class implementationOptions(Enum):
    threaded = 1
    threaded_sequential = 2
    thread_pool = 3
    asyncio = 4
    multiprocessing = 5
    multiprocessing_pool = 6
    multiprocessing_pool_executor = 7
    exit_program_and_generate_report = 8


class ComputationResult:
    def __init__(self, implementation, numOfTasks, primeNumber, executionTime):
        self.implementation = implementation
        self.numOfTasks = numOfTasks
        self.primeNumber = primeNumber
        self.executionTime = executionTime

    def __str__(self):
        return (
            f"Implementation: {self.implementation}, "
            f"Tasks: {self.numOfTasks}, "
            f"Prime: {self.primeNumber}, "
            f"Time: {self.executionTime:.2f} seconds"
        )

    def returnResult(self):
        return (
            self.implementation,
            self.numOfTasks,
            self.primeNumber,
            self.executionTime,
        )


class ComputationResults:
    def __init__(self):
        self.results = []

    def addResult(self, result):
        self.results.append(result)

    def returnResults(self):
        return self.results

    def displayResultsInText(self):
        for result in self.results:
            print(result.__str__())

    def displayBarGraph(self):
        # Extract data for plotting
        labels = []
        times = []

        for result in self.results:
            label = f"Impl:{result.implementation}\nTasks:{result.numOfTasks}\nPrime:{result.primeNumber}"
            labels.append(label)
            times.append(result.executionTime)

        # Create bar graph
        plt.clear_figure()
        plt.bar(labels, times)
        plt.title("Execution Time Comparison")
        plt.xlabel("Implementation Details")
        plt.ylabel("Execution Time (seconds)")
        plt.show()


def runImplementation(implementation, numOfTasks, primeNumber, poolSize):
    match implementation:
        case 1:

            return threaded_compute_primes(numOfTasks, primeNumber)
        case 2:

            return threaded_sequential_compute_primes(numOfTasks, primeNumber)
        case 3:

            return thread_pool_compute_primes(poolSize, numOfTasks, primeNumber)
        case 4:

            return asyncio.run(asyncio_compute_primes(numOfTasks, primeNumber))
        case 5:

            return multiprocessing_compute_primes(numOfTasks, primeNumber)
        case 6:

            return multiprocessing_pool_compute_primes(
                poolSize, numOfTasks, primeNumber
            )
        case 7:

            return multiprocessing_pool_executor_compute_primes(
                poolSize, numOfTasks, primeNumber
            )
        case 8:
            print("Exiting program and generating report.")
            return quitProgramAndGenerateReport  # Exit option

    return invalidOption  # Invalid implementation number


def printUserInstructions():
    print("The list of implementations includes:")
    print("1. Threaded implementation")
    print("2. Threaded sequential implementation")
    print("3. Thread pool implementation")
    print("4. Asyncio implementation")
    print("5. Multiprocessing implementation")
    print("6. Multiprocessing Pool implementation")
    print("7. Multiprocessing PoolExecutor implementation")
    print("8. Exit the program and generate a report")


def convertUserInputToInteger(userInput, defaultValue):
    if not userInput:
        print(f"Empty Input. Defaulting to {defaultValue}.")
        return defaultValue
    try:
        if int(userInput) < 0:
            print(f"Negative input. Defaulting to {defaultValue}.")
            return defaultValue
        return int(userInput)
    except ValueError:
        print(f"Invalid input. Defaulting to {defaultValue}.")
        return defaultValue


def userInputPoolSize(firstImplementation):
    poolSize = 2
    if firstImplementation in implementationsRequiringPoolSize:
        poolSize = input(
            "Enter the pool size for the first implementation (default is 2): "
        )
    return int(poolSize)


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
    implementation = convertUserInputToInteger(firstImplementationInput, 1)
    poolSize = userInputPoolSize(implementation)
    return (
        primeToCompute,
        numOfTasks,
        implementation,
        poolSize,
    )


def main():
    closeProgram = False
    computationResults = ComputationResults()
    print("Welcome to the Python Multiprocessing Visualization Tool!")
    print(
        "This tool allows you to compare different implementations of prime number computation."
    )
    print("You can run multiple implementations and see their execution times.")
    while not closeProgram:
        primeToCompute, numOfTasks, implementation, poolSize = collectUserInput()
        implementationResult = runImplementation(
            implementation, numOfTasks, primeToCompute, poolSize
        )
        if implementationResult == invalidOption:
            print("Invalid implementation number. Please try again.")
        elif implementationResult == quitProgramAndGenerateReport:
            closeProgram = True
        else:
            computationResult = ComputationResult(
                implementation, numOfTasks, primeToCompute, implementationResult
            )
            computationResults.addResult(computationResult)
    print("Computation Results:")
    # computationResults.displayResultsInText()
    computationResults.displayBarGraph()


if __name__ == "__main__":
    main()
