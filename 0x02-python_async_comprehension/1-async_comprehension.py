#!/usr/bin/env python3
"""Async Comprehensions"""

import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """function async_comprehension"""
    rand_num = [i async for i in async_generator()]
    return rand_num
