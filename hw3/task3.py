"""
CMSC 14200, Spring 2026
Homework 3, Task 3

People consulted:
   List anyone (other than the course staff) that you consulted about
   this assignment.

Online resources consulted:
   List the URLs of any online resources other than the course text and
   the official Python language documentation that you used to complete
   this assignment.
"""

from typing import Callable

from tree import Tree


class TreeNode(Tree):
    """
    A concrete implementation of the abstract base class Tree.
    """

    value: int
    children: list[Tree]

    def __init__(self, value: int, children: list[Tree] | None = None) -> None:
        """Constructor"""
        self.value = value
        self.children = [] if children is None else children

    def __str__(self) -> str:
        """A simple string representation of a tree."""
        if self.children == []:
            return f"(L {self.value})"
        else:
            return f"(T {self.value} [{' '.join(map(str, self.children))}])"

    # TODO:
    # Implement all of the required methods from the Tree ABC
    # here in the TreeNode class.


# We do not intend to run this Python file as a main program.
# But we include a __main__ definition below with constructor
# calls, as a way to nudge mypy to typecheck the implementations
# of abstract methods in the classes above.

if __name__ == "__main__":
    TreeNode(0, None)
