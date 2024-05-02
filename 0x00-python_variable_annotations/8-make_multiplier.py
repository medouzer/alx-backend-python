#!/usr/bin/env python3
"""Basic annotations - add"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """function make_multiplier"""
    def multii(x: float):
        return multiplier * x
    return multii
