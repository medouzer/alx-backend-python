#!/usr/bin/env python3


def sum_list(input_list: list[float]) -> float:
    sum: float = 0
    for item in input_list:
        sum += item
    return sum
