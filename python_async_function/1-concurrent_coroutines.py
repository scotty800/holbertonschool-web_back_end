#!/usr/bin/env python3
"""Spawns wait_random n times with the specified
max_delay and returns a list of delays.
"""


import asyncio
from typing import List
module = __import__("0-basic_async_syntax")
print(module.__doc__)
wait_random = module.wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns wait_random n times with
    the specified max_delay and returns a list of delays.
    The list of delays is in ascending order
    using sort() due to concurrency.

    Args:
        n (int): Number of times to spawn wait_random.
        max_delay (int): Maximum delay time in seconds.

    Returns:
        List[float]: List of delays in ascending order.
    """
    delays = []
    tasks = [wait_random(max_delay) for index in range(n)]
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)
    return delays
