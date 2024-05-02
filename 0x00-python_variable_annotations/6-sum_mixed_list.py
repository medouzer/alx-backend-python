#!/usr/bin/env python3

from typing import Union


def sum_mixed_list(mxd_lst: list[Union[int, float]]) -> float:
    sum: float = 0
    for item in mxd_lst:
        sum += item
    return sum
