import asyncio
from time import sleep

def compute_primes(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def ioIntensiveComputePrimeNumbers(n):
    sleep(5)  # Simulating I/O operation
    compute_primes(n)
    sleep(5) # Simulating I/O operation

async def ioIntensiveAsyncComputePrimeNumbers(n):
    await asyncio.sleep(5)  # Simulating I/O operation
    compute_primes(n)
    await asyncio.sleep(5)  # Simulating I/O operation


