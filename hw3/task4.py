"""
CMSC 14200, Spring 2026
Homework 3, Task 4

People consulted:
   List anyone (other than the course staff) that you consulted about
   this assignment.

Online resources consulted:
   List the URLs of any online resources other than the course text and
   the official Python language documentation that you used to complete
   this assignment.
"""

from typing import Callable
import functools


def memoize(f: Callable[[int], int]) -> Callable[[int], int]:
    """
    Create a memoized verison of the input function. See the
    homework assignment for more complete details.
    """
    raise NotImplementedError("TODO")


def trace(f: Callable[[int], int]) -> Callable[[int], int]:
    """
    Create a tracing verison of the input function. See the
    homework assignment for more complete details.
    """
    raise NotImplementedError("TODO")
