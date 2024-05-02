#!/usr/bin/env python3
"""Basic annotations - add"""


def sum_list(input_list: list[float]) -> float:
    """function sum_list"""
    sum: float = 0
    for item in input_list:
        sum += item
    return sum
