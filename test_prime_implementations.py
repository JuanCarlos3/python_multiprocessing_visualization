import pytest
from computePrimeNumbers import compute_primes
from main import convertUserInputToInteger, runImplementation
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


@pytest.mark.parametrize(
    "number, expected",
    [
        (2, True),
        (4, False),
        (109797044856282383, True),  # This large number is prime
    ],
)
def test_compute_primes(number, expected):
    assert compute_primes(number) == expected


# Test input conversion
@pytest.mark.parametrize(
    "input_value,default_value,expected",
    [
        ("", 10, 10),
        ("abc", 10, 10),
        ("5", 10, 5),
        ("-1", 10, 10),
    ],
)
def test_convert_user_input(input_value, default_value, expected):
    assert convertUserInputToInteger(input_value, default_value) == expected


# Test implementation selection
@pytest.mark.parametrize(
    "implementation_number,expected",
    [
        (1, lambda x: x > 0),
        (2, lambda x: x > 0),
        (3, lambda x: x > 0),
        (4, lambda x: x > 0),
        (5, lambda x: x > 0),
        (6, lambda x: x > 0),
        (7, lambda x: x > 0),
        (8, lambda x: x == -2),
        (9, lambda x: x == -1),
        (0, lambda x: x == -1),
        (-1, lambda x: x == -1),
    ],
)
def test_run_implementation(implementation_number, expected):
    # Test with simulateIOBound=False
    result = runImplementation(implementation_number, 1, 17, 2, False)
    assert expected(result)


# Test threaded implementation with different task counts
@pytest.mark.parametrize("num_tasks", [1, 2])
@pytest.mark.parametrize("simulateIOBound", [True, False])
def test_threaded_compute_primes(num_tasks, simulateIOBound):
    result = threaded_compute_primes(num_tasks, 17, simulateIOBound)
    assert isinstance(result, float) and result >= 0


# Test sequential threaded implementation
@pytest.mark.parametrize("num_tasks", [1, 2])
@pytest.mark.parametrize("simulateIOBound", [True, False])
def test_threaded_sequential_compute_primes(num_tasks, simulateIOBound):
    result = threaded_sequential_compute_primes(num_tasks, 17, simulateIOBound)
    assert isinstance(result, float) and result >= 0


# Test thread pool implementation
@pytest.mark.parametrize("num_threads,num_tasks", [(1, 1), (2, 2)])
@pytest.mark.parametrize("simulateIOBound", [True, False])
def test_thread_pool_compute_primes(num_threads, num_tasks, simulateIOBound):
    result = thread_pool_compute_primes(num_threads, num_tasks, 17, simulateIOBound)
    assert isinstance(result, float) and result >= 0


# Test asyncio implementation
@pytest.mark.asyncio
@pytest.mark.parametrize("num_tasks", [1, 2])
@pytest.mark.parametrize("simulateIOBound", [True, False])
async def test_asyncio_compute_primes(num_tasks, simulateIOBound):
    result = await asyncio_compute_primes(num_tasks, 17, simulateIOBound)
    assert isinstance(result, float) and result >= 0


# Test multiprocessing implementation
@pytest.mark.parametrize("num_tasks", [1, 2])
@pytest.mark.parametrize("simulateIOBound", [True, False])
def test_multiprocessing_compute_primes(num_tasks, simulateIOBound):
    result = multiprocessing_compute_primes(num_tasks, 17, simulateIOBound)
    assert isinstance(result, float) and result >= 0


# Test multiprocessing pool implementation
@pytest.mark.parametrize("num_processes,num_tasks", [(1, 1), (2, 2)])
@pytest.mark.parametrize("simulateIOBound", [True, False])
def test_multiprocessing_pool_compute_primes(num_processes, num_tasks, simulateIOBound):
    result = multiprocessing_pool_compute_primes(
        num_processes, num_tasks, 17, simulateIOBound
    )
    assert isinstance(result, float) and result >= 0


# Test multiprocessing pool executor implementation
@pytest.mark.parametrize("num_processes,num_tasks", [(1, 1), (2, 2)])
@pytest.mark.parametrize("simulateIOBound", [True, False])
def test_multiprocessing_pool_executor_compute_primes(
    num_processes, num_tasks, simulateIOBound
):
    result = multiprocessing_pool_executor_compute_primes(
        num_processes, num_tasks, 17, simulateIOBound
    )
    assert isinstance(result, float) and result >= 0


if __name__ == "__main__":
    pytest.main(["-v"])
