#!/usr/bin/env python3
"""Basic annotations - add"""


def floor(n: float) -> int:
    """function floor"""
    if n >= 0:
        return int(n)
    else:
        return int(n) - 1
