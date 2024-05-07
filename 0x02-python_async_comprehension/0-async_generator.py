#!/usr/bin/env python3
"""Async Generator"""

import asyncio
from typing import Generator
import random


async def async_generator() -> Generator[float, None, None]:
    """function async_generator"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
