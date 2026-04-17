"""
CMSC 14200, Spring 2026
Homework 4, Task 1

People consulted:
   List anyone (other than the course staff) that you consulted about
   this assignment.

Online resources consulted:
   List the URLs of any online resources other than the course text and
   the official Python language documentation that you used to complete
   this assignment.
"""

from graph import WordGraph


class PrecomputedWordGraph(WordGraph):
    """
    A word graph defined by a file comprising valid words:
    vertices are the words in the file that are no longer than
    a specified maximum length.

    This word graph is "precomputed" in the sense that all of
    vertices and edges are computed immediately after loading
    a file of words.
    """

    # TODO: Add type declarations for all instance attributes

    def __init__(self, wordfile: str, maxlen: int):
        """
        Construct a new word graph based on the given file of
        words, ignoring any words longer than the specified
        maximum length. Words that contain anything besides
        the 26 characters of the alphabet are also ignored.
        Uppercase letters should be converted to lowercase.
        """
        raise NotImplementedError("TODO")

    # TODO: Implement the required abstract methods


# We do not intend to run this Python file as a main program.
# But we include a __main__ definition below with constructor
# calls, as a way to nudge mypy to typecheck the implementations
# of abstract methods in the classes above.

if __name__ == "__main__":
    PrecomputedWordGraph("", 0)
