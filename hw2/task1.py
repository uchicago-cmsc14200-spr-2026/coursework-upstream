"""
CMSC 14200, Spring 2026
Homework 2, Task 1

People consulted:
   List anyone (other than the course staff) that you consulted about
   this assignment.

Online resources consulted:
   List the URLs of any online resources other than the course text and
   the official Python language documentation that you used to complete
   this assignment.
"""


def mean(nums: list[int]) -> float | None:
    """
    Compute the mean (average) of a list of integers.

    Inputs:
        nums (list[int]): Not necessarily in sorted order
    """
    raise NotImplementedError("TODO: mean")


def median(nums: list[int]) -> int | tuple[int, int] | None:
    """
    Compute the median of a list of integers.

    Inputs:
        nums (list[int]): Not necessarily in sorted order

    Returns:
        None, if the input list is empty.
        The middlemost element, if the input list has odd length.
        The pair of the two middlemost elements, if the input list
            has even length.
    """
    raise NotImplementedError("TODO: median")


def mode(nums: list[int]) -> list[int]:
    """
    Compute the mode(s) of a list of integers.

    Inputs:
        nums (list[int]): Not necessarily in sorted order

    Returns (list[int]): The most common element(s)
    """
    raise NotImplementedError("TODO: mode")
