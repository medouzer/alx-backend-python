#!/usr/bin/env python3
"""Basic annotations - add"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """function sum_list"""
    sum: float = 0
    for item in input_list:
        sum += item
    return sum
