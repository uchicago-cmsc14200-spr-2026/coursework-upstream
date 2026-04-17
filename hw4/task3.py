"""
CMSC 14200, Spring 2026
Homework 4, Task 3

People consulted:
   List anyone (other than the course staff) that you consulted about
   this assignment.

Online resources consulted:
   List the URLs of any online resources other than the course text and
   the official Python language documentation that you used to complete
   this assignment.
"""

from typing import Optional
from graph import WordGraph


def shortest_path(g: WordGraph, s: str, d: str) -> Optional[list[str]]:
    """
    Determine the shortest path between words in a word graph, if
    such a path exists. If there are multiple words with the same
    shortest length, one of the paths is returned arbitrarily.

    Inputs:
        g: the graph to traverse
        s: the starting vertex
        d: the destination vertex

    Returns:
        A shortest path from s to d, represented as a list whose first
        entry is s, last entry is d, and with intermediate vertices in
        order between them. None if no path exists.
    """
    raise NotImplementedError("TODO")
