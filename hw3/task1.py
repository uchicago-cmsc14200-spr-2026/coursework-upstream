"""
CMSC 14200, Spring 2026
Homework 3, Task 1

People consulted:
   List anyone (other than the course staff) that you consulted about
   this assignment.

Online resources consulted:
   List the URLs of any online resources other than the course text and
   the official Python language documentation that you used to complete
   this assignment.
"""

from typing import Callable


def compose(
    f: Callable[[int], int], g: Callable[[int], int]
) -> Callable[[int], int]:
    """
    The right-to-left composition of two functions `f` and `g`.
    """
    raise NotImplementedError("TODO")


def fixpoint(f: Callable[[int], int], x: int) -> list[int]:
    """
    Iteratively call a function `f` until the output equals the input.
    """
    raise NotImplementedError("TODO")


def apply_pipeline(fs: list[Callable[[int], int]], x: int) -> int:
    """
    Left-to-right composition of a list of functions `fs`,
    applied to a number `x`.
    """
    raise NotImplementedError("TODO")


def reify_pipeline(fs: list[Callable[[int], int]]) -> Callable[[int], int]:
    """
    Left-to-right composition of a list of functions `fs`,
    represented as a single function.
    """
    raise NotImplementedError("TODO")
