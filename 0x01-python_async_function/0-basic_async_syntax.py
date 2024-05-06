#!/usr/bin/env python3
"""The basics of async"""

import random
import asyncio


async def wait_random(max_delay=10):
    """function wait_random"""
    time_sleep = random.uniform(0, max_delay)
    await asyncio.sleep(time_sleep)
    return time_sleep
