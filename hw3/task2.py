"""
CMSC 14200, Spring 2026
Homework 3, Task 2

People consulted:
   List anyone (other than the course staff) that you consulted about
   this assignment.

Online resources consulted:
   List the URLs of any online resources other than the course text and
   the official Python language documentation that you used to complete
   this assignment.
"""

from typing import Callable


def concat_map(f: Callable[[int], list[int]], xs: list[int]) -> list[int]:
    """
    A transformation of the input list `xs`, where each element `x` in the
    list is replaced by the zero or more elements corresponding to `f`
    applied to `x`.
    """
    raise NotImplementedError("TODO")


def my_map(f: Callable[[int], int], xs: list[int]) -> list[int]:
    """
    A re-implementation of map on lists, defined in terms of concat_map.
    """
    raise NotImplementedError("TODO")


def my_filter(pred: Callable[[int], bool], xs: list[int]) -> list[int]:
    """
    A re-implementation of filter on lists, defined in terms of concat_map.
    """
    raise NotImplementedError("TODO")
