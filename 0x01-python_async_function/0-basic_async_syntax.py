#!/usr/bin/env python3

import random


async def wait_random(max_delay=10):
    return random.uniform(0, max_delay)
