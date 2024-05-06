#!/usr/bin/env python3
"""
Let's execute multiple coroutines at the same time with async
"""

wait_random = __import__('0-basic_async_syntax').wait_random
import asyncio
from typing import List


async def wait_n(n: int, max_delay: int) -> List[float]:
    """function wait_n"""
    list_of_delays = []
    delays = []
    for i in range(n):
        delays.append(wait_random(max_delay))
    for k in asyncio.as_completed(delays):
        list_of_delays.append(await k)
    return list_of_delays
