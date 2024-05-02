#!/usr/bin/env python3
"""Basic annotations - add"""

import typing


def element_length(lst: typing.Iterable[typing.Sequence]) -> typing.List[typing.Tuple[typing.Sequence, int]]:
    """function element_length"""
    return [(i, len(i)) for i in lst]
