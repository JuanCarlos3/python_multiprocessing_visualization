import asyncio
from tqdm import tqdm
from time import sleep


def compute_primes(n, position=None):
    if n <= 1:
        return False

    upper = int(n**0.5) + 1
    is_worker = position is not None
    with tqdm(
        total=upper,
        position=position or 0,
        leave=not is_worker,
        desc=f"Task {position}" if is_worker else "CPU Task",
    ) as pbar:
        for i in range(2, upper):
            pbar.update(1)
            if n % i == 0:
                return False
    return True


def compute_primes_ioIntensive(n, position=None):
    if n <= 1:
        return False

    upper = int(n**0.5) + 1
    is_worker = position is not None
    with tqdm(
        total=upper,
        position=position or 0,
        leave=not is_worker,
        desc=f"I/O Task {position}" if is_worker else "I/O Task",
    ) as pbar:
        sleep(10)
        for i in range(2, upper):
            pbar.update(1)
            if i == upper // 3:
                sleep(10)
            if i == upper // 2:
                sleep(10)
            if n % i == 0:
                return False
        sleep(10)
    return True


async def compute_primes_ioIntensive_async(n, position=None):
    if n <= 1:
        return False

    upper = int(n**0.5) + 1
    is_worker = position is not None
    with tqdm(
        total=upper,
        position=position or 0,
        leave=not is_worker,
        desc=f"Async I/O {position}" if is_worker else "Async I/O",
    ) as pbar:
        await asyncio.sleep(10)
        for i in range(2, upper):
            pbar.update(1)
            if i == upper // 3:
                await asyncio.sleep(10)
            if i == upper // 2:
                await asyncio.sleep(10)
            if n % i == 0:
                return False
        await asyncio.sleep(10)
    return True
