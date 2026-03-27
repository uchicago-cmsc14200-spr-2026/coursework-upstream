"""
CMSC 14200, Spring 2026
Homework 1, Task 1

People consulted:
   List anyone (other than the course staff) that you consulted about
   this assignment.

Online resources consulted:
   List the URLs of any online resources other than the course text and
   the official Python language documentation that you used to complete
   this assignment.
"""


def to_base_n(n: int, num: int) -> str:
    """
    Return a nitstring of the form "0_n_nits", where nits is a
    string of characters representing the number `num` in base `n`.
    Assumes that `n` is between 2 and 9, and that `num` is
    greater than or equal to zero.
    """
    raise NotImplementedError("TODO: to_base_n")


def from_base_n(s: str) -> int:
    """
    Return the integer corresponding to the input nitstring.
    Assumes that `s` is a valid nitstring of the form "0_n_nits",
    where `n` is between 2 and 9, and `nits` is one or more valid
    symbols in base `n`.
    """
    raise NotImplementedError("TODO: from_base_n")
