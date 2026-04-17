#
# Base class for word graphs
#
# DO NOT MODIFY THIS FILE
#

from abc import ABC, abstractmethod


class WordGraph(ABC):
    """
    A representation of "adjacent words" or "adjacent strings".

    Two words are adjacent if they have the same length and differ by
    exactly one character. The strings that form the "vertices" of this
    undirected graph are defined by the concrete child classes. But
    every word graph also maintains a notion of strings that are deemed
    "valid words"; not every string vertex in a graph is valid.
    """

    @abstractmethod
    def adjacent_words(self, vertex: str) -> set[str]:
        """
        Returns the set of words that are adjacent to the given word.
        If the string is not a vertex in the graph, returns the empty set.
        """
        raise NotImplementedError

    @abstractmethod
    def is_valid_word(self, vertex: str) -> bool:
        """
        Determines whether the string is deemed to be a valid word.
        """
        raise NotImplementedError

    def degree(self, vertex: str) -> int:
        """
        Returns the number of words adjacent to the given word.
        If the string is not a vertex in the graph, returns zero.
        """
        return len(self.adjacent_words(vertex))
