"""
Fake implementations of the ConnectMBase class
"""

from base import ConnectMBase, PieceColor
from typing import Optional
from copy import deepcopy


class ConnectMStub(ConnectMBase):
    """
    Stub implementation of the ConnectMBase class
    """

    _board: list[list[Optional[PieceColor]]]

    def __init__(self, nrows: int, ncols: int, m: int):
        super().__init__(nrows, ncols, m)
        self._board = [[None] * ncols for _ in range(nrows)]

    def __str__(self) -> str:
        return "BOARD"

    # TODO: Stub the rest of the methods here!


class ConnectMFake(ConnectMBase):
    """
    Fake implementation of the ConnectMBase class

    Expected behaviours:
    - Stores the full board internally, but we only ever
      modify the bottom row of the board. i.e., we
      effectively have a 1-row board, even if we display
      a larger board.
    - Game ends after M moves. If M is even, Red wins;
      otherwise, Yellow wins.
    """

    _board: list[list[Optional[PieceColor]]]
    _nummoves: int

    def __init__(self, nrows: int, ncols: int, m: int):
        super().__init__(nrows, ncols, m)
        self._board = [[None] * ncols for _ in range(nrows)]
        self._nummoves = 0

    # TODO: Fake the rest of the methods here!