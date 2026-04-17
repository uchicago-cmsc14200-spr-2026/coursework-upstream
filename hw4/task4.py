"""
CMSC 14200, Spring 2026
Homework 4, Task 4

People consulted:
   List anyone (other than the course staff) that you consulted about
   this assignment.

Online resources consulted:
   List the URLs of any online resources other than the course text and
   the official Python language documentation that you used to complete
   this assignment.
"""

from graph import WordGraph


class PseudoWordGraph(WordGraph):
    """
    A word graph where the vertices are arbitrary strings, what
    we are calling "pseudo words".

    Given the effectively unbounded number of pseudo words, when the
    graph object is initialized the implementation does not precompute
    vertices and edges, nor store them in instance attributes. Instead,
    vertices and edges are manipulated "on demand" as needed by the
    implementations of the required methods.

    The definition of valid words for this word graph is given by
    a specified input file, and there is no restriction on the
    maximum length of words.
    """

    # TODO: Add type declarations for all instance attributes

    def __init__(self, wordfile: str):
        """
        Construct a new word graph based on the given file of
        words. Words that contain anything besides the 26
        characters of the alphabet are ignored. Uppercase letters
        should be converted to lowercase.
        """
        raise NotImplementedError("TODO")

    # TODO: Implement the required abstract methods


# We do not intend to run this Python file as a main program.
# But we include a __main__ definition below with constructor
# calls, as a way to nudge mypy to typecheck the implementations
# of abstract methods in the classes above.

if __name__ == "__main__":
    PseudoWordGraph("")
