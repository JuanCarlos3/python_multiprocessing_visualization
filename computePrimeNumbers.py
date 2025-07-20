import asyncio
from tqdm import tqdm
from time import sleep


def compute_primes(n):
    if n <= 1:
        return False

    upper = int(n**0.5) + 1
    with tqdm(total=upper) as pbar:
        for i in range(2, upper):
            pbar.update(1)
            if n % i == 0:
                pbar.close()
                return False
    pbar.close()
    return True


def ioIntensiveComputePrimeNumbers(n):
    sleep(5)  # Simulating I/O operation
    compute_primes(n)
    sleep(5)  # Simulating I/O operation


async def ioIntensiveAsyncComputePrimeNumbers(n):
    await asyncio.sleep(5)  # Simulating I/O operation
    compute_primes(n)
    await asyncio.sleep(5)  # Simulating I/O operation
