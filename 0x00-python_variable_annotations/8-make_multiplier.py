#!/usr/bin/env python3

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    def multii(x: float):
        return multiplier * x
    return multii
