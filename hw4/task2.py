"""
CMSC 14200, Spring 2026
Homework 4, Task 2

People consulted:
   List anyone (other than the course staff) that you consulted about
   this assignment.

Online resources consulted:
   List the URLs of any online resources other than the course text and
   the official Python language documentation that you used to complete
   this assignment.
"""

from graph import WordGraph


def variations(g: WordGraph, w: str, n: int) -> set[str]:
    """
    Determine the set of valid words in a word graph that are
    exactly `n` steps away from the given starting word. No
    word is allowed to appear more than once in any sequence
    of steps. You may assume that the starting word is a
    vertex in the graph.
    """
    raise NotImplementedError("TODO")
