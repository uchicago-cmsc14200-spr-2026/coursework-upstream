import random
from typing import Callable

CHARS = '_123456789ABCDEF'
      
class SlidingPuzzle:

    # The puzzle contains integers 0 through 15 inclusive.
    # 0 represents that gap in the puzzle.
    puzzle : list[int]
  
    def __init__(self):
        self.puzzle = [(n+1)%16 for n in range(16)]

    def __repr__(self) -> str:
        return ''.join([CHARS[i] for i in self.puzzle])
      
    def __str__(self) -> str:
      def row(n:int) -> str:
        return ' '.join([CHARS[i] for i in self.puzzle[n:n+4]])
      return '\n'.join([row(i*4) for i in range(4)])

    def swap(self,a:int,b:int) -> None:
      # Pythonic one-line swap
      self.puzzle[a], self.puzzle[b] = self.puzzle[b], self.puzzle[a]

    def move(self,test:Callable[[int],bool],δ:int) -> None:
      """
      Swap the 0 if the 0 is in a swappable position as determined by test.
      """
      gap = self.puzzle.index(0)
      if test(gap):
        self.swap(gap,gap+δ)
        
    def up(self) -> None:
      self.move(lambda g: g<12, 4)

    def down(self) -> None:
      self.move(lambda g: g>3, -4)

    def right(self) -> None:
      self.move(lambda g: g%4!=0, -1)
    
    def left(self) -> None:
      self.move(lambda g: g%4!=3, 1)
    
    def scramble(self, n:int) -> None:
      if n>0:
        random.choice([self.up,self.down,self.left,self.right])()
        self.scramble(n-1)

    def solved(self) -> bool:
      return self.__repr__()=='123456789ABCDEF_'
    
class PuzzleGraph:

    _adj : dict[str,set[str]]

    def __init__(self):
        self._adj = {}

    def add_v(self, v : str) -> None:
        if v not in self._adj:
            self._adj[v] = set()

    def add_e(self, src : str, dst : str) -> None:
        if src not in self._adj:
            raise ValueError(f'vertex {src} not in graph')
        if dst not in self._adj:
            raise ValueError(f'vertex {dst} not in graph')
        self._adj[src].add(dst)

    def vertices(self) -> set[str]:
        return set(self._adj.keys())
        
    def neighbors(self, src : str) -> set[str]:
        if src not in self._adj:
            raise ValueError(f'(neighbors) {src}')
        return self._adj[src]

    def __repr__(self) -> str:
        return f'PuzzleGraph({self._adj})'

def build_graph(pzl : SlidingPuzzle, n: int) -> PuzzleGraph:
    """ Please see the accompanying README. """
    raise NotImplementedError('todo: build_graph')


# def play_game():
#     """Play game until solved."""
#     pzl = SlidingPuzzle()
#     pzl.scramble(N_SCRAMBLES)
#     while not pzl.solved():
#         print()
#         print(pzl)
#         cmd = input('\n  w\na s d\n  ')
#         match cmd.strip():
#             case 'w':
#                 pzl.up()
#             case 'a':
#                 pzl.left()
#             case 's':
#                 pzl.down()
#             case 'd':
#                 pzl.right()
#     print()
#     print(pzl)
#     print('*** Well done! ***')
#     print()

