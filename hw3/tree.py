#
# Tree base class
#
# DO NOT MODIFY THIS FILE
#


from abc import ABC, abstractmethod
from typing import Callable


class Tree(ABC):
    """
    A Tree class, where each node carries an integer value and
    zero or more children.
    """
    value: int
    children: list["Tree"]

    @abstractmethod
    def map(self, f: Callable[[int], int]) -> "Tree":
        """
        Return a tree that is like the input tree, but where each value
        in the tree has been transformed by the function `f`.
        """
        raise NotImplementedError

    @abstractmethod
    def reduce(self, f: Callable[[int, int], int], init: int) -> int:
        """
        Return a number produced by "reducing" the input tree.
        """
        raise NotImplementedError

    @abstractmethod
    def sum(self) -> int:
        """Return the sum of values stored in the tree."""
        raise NotImplementedError

    @abstractmethod
    def size(self) -> int:
        """Return the number of nodes in the tree."""
        raise NotImplementedError

    @abstractmethod
    def min(self) -> int:
        """Return the minimum value in the tree."""
        raise NotImplementedError

    @abstractmethod
    def max(self) -> int:
        """Return the maximum value in the tree."""
        raise NotImplementedError
