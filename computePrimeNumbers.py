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


def compute_primes_ioIntensive(n):
    if n <= 1:
        return False

    upper = int(n**0.5) + 1
    with tqdm(total=upper) as pbar:
        sleep(5)
        for i in range(2, upper):
            pbar.update(1)
            if i == upper // 3:
                sleep(5)
            if i == upper // 2:
                sleep(5)
            if n % i == 0:
                pbar.close()
                return False
        sleep(5)
    pbar.close()
    return True


async def compute_primes_ioIntensive_async(n):
    if n <= 1:
        return False

    upper = int(n**0.5) + 1
    with tqdm(total=upper) as pbar:
        await asyncio.sleep(5)
        for i in range(2, upper):
            pbar.update(1)
            if i == upper // 3:
                await asyncio.sleep(5)
            if i == upper // 2:
                await asyncio.sleep(5)
            if n % i == 0:
                pbar.close()
                return False
        await asyncio.sleep(5)
    pbar.close()
    return True
