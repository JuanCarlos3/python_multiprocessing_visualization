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


class implementationOptions(Enum):
    threaded = 1
    threaded_sequential = 2
    thread_pool = 3
    asyncio = 4
    multiprocessing = 5
    multiprocessing_pool = 6
    multiprocessing_pool_executor = 7
    exit_program_and_generate_report = 8


invalidOption = -1
quitProgramAndGenerateReport = -2
defaultPoolSize = 2
defaultNumberOfTasks = 2
defaultPrimeNumber = 109797044856282383
defaultPrimeNumber = 834238027356431
defaultImplementation = implementationOptions["threaded"].value
implementationsRequiringPoolSize = [
    3,
    6,
    7,
]  # Implementations that require pool size input


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
            label = f"I:{implementationOptions(result.implementation).name} T:{result.numOfTasks} P:{result.primeNumber}"
            labels.append(label)
            times.append(result.executionTime)

        # Create bar graph
        # print(labels)
        plt.clear_figure()
        plt.bar(labels, times)
        plt.title("Execution Time Comparison")
        plt.xlabel("Implementation Details")
        plt.ylabel("Execution Time (seconds)")
        plt.show()


def runImplementation(
    implementation, numOfTasks, primeNumber, poolSize, simulateIOBound
):
    match implementation:
        case 1:
            return threaded_compute_primes(numOfTasks, primeNumber, simulateIOBound)
        case 2:

            return threaded_sequential_compute_primes(
                numOfTasks, primeNumber, simulateIOBound
            )
        case 3:

            return thread_pool_compute_primes(
                poolSize, numOfTasks, primeNumber, simulateIOBound
            )
        case 4:

            return asyncio.run(
                asyncio_compute_primes(numOfTasks, primeNumber, simulateIOBound)
            )
        case 5:

            return multiprocessing_compute_primes(
                numOfTasks, primeNumber, simulateIOBound
            )
        case 6:

            return multiprocessing_pool_compute_primes(
                poolSize, numOfTasks, primeNumber, simulateIOBound
            )
        case 7:

            return multiprocessing_pool_executor_compute_primes(
                poolSize, numOfTasks, primeNumber, simulateIOBound
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
    if firstImplementation not in implementationsRequiringPoolSize:
        return defaultPoolSize

    userInput = input("Enter the pool size for the implementation (default is 2): ")
    if not userInput:
        print(f"Empty Input. Defaulting to {defaultPoolSize}.")
        return defaultPoolSize
    try:
        if int(userInput) < 0:
            print(f"Negative input. Defaulting to {defaultPoolSize}.")
            return defaultPoolSize
        return int(userInput)
    except ValueError:
        print(f"Invalid input. Defaulting to {defaultPoolSize}.")
        return defaultPoolSize

    poolSize = defaultPoolSize
    if firstImplementation in implementationsRequiringPoolSize:
        poolSize = input("Enter the pool size for the implementation (default is 2): ")
    return int(poolSize)


def userInputSimulateIOBound(prompt):
    simulateIOBound = input(prompt)
    if simulateIOBound.lower() in ["y", "yes"]:
        print("Simulating I/O bound computation.")
        return True
    elif simulateIOBound.lower() in ["n", "no"]:
        print("Not simulating I/O bound computation.")
        return False
    else:
        print("Invalid input. Defaulting to no I/O simulation.")
        return False


def collectUserInput():
    printUserInstructions()
    implementationInput = input(
        "Please enter the number of the implementation you want to run (1-7): "
    )
    implementation = convertUserInputToInteger(
        implementationInput, defaultImplementation
    )
    if implementation == implementationOptions.exit_program_and_generate_report.value:
        return (
            defaultPrimeNumber,
            defaultNumberOfTasks,
            implementation,
            defaultPoolSize,
            False,
        )

    primeInput = input(
        "Please enter the prime number to compute (default is 109797044856282383): "
    )
    primeToCompute = convertUserInputToInteger(primeInput, defaultPrimeNumber)
    tasksInput = input(
        "Please enter the number of times you want to computer the primenumber: "
    )
    numOfTasks = convertUserInputToInteger(tasksInput, defaultNumberOfTasks)
    poolSize = userInputPoolSize(implementation)
    simulateIOBound = userInputSimulateIOBound(
        "Do you want to simulate I/O bound computation? (y/n)"
    )
    return (primeToCompute, numOfTasks, implementation, poolSize, simulateIOBound)


def main():
    closeProgram = False
    computationResults = ComputationResults()
    print("Welcome to the Python Multiprocessing Visualization Tool!")
    print(
        "This tool allows you to compare different implementations of prime number computation."
    )
    print("You can run multiple implementations and see their execution times.")
    while not closeProgram:
        primeToCompute, numOfTasks, implementation, poolSize, simulateIOBound = (
            collectUserInput()
        )
        implementationResult = runImplementation(
            implementation, numOfTasks, primeToCompute, poolSize, simulateIOBound
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
