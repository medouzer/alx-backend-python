#!/usr/bin/env python3
"""Tasks"""
import asyncio
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n, max_delay):
    """function task_wait_n"""
    list_of_delays = []
    delays = []
    for i in range(n):
        delays.append(task_wait_random(max_delay))
    for k in asyncio.as_completed(delays):
        list_of_delays.append(await k)
    return list_of_delays
