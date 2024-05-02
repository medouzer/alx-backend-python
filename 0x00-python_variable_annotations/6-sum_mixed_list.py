#!/usr/bin/env python3
"""Basic annotations - add"""

from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """function sum_mixed_list"""
    sum: float = 0
    for item in mxd_lst:
        sum += item
    return sum
