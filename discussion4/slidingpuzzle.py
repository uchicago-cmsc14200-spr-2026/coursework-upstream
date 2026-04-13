import random
from typing import Callable

# Adjust N_SCRAMBLES upwards for higher difficulty.
N_SCRAMBLES = 4

class SlidingPuzzle:

    puzzle : list[int]
    __n : int
    rows : int
    cols : int
  
    def __init__(self, rows: int, cols: int):
        self.rows = rows
        self.cols = cols

        # TODO: Determine N, and use a list comprehension to initialize puzzle.
        raise NotImplementedError


    def __repr__(self) -> str:
        """Present the puzzle for debugging."""
        return f'SlidingPuzzle({self.puzzle})'
  

    def __str__(self) -> str:
        """Present the puzzle for gameplay."""
        def show_row(row_number: int) -> str:
            # If any of your cells will have a larger-than-two-digit number
            # in them, you may need to update this function
            return ' '.join(map(lambda n: f"{n if n != 0 else ' ': >2}", self.puzzle[row_number * self.cols:(row_number + 1) * self.cols]))
        return '\n'.join(show_row(n) for n in range(self.rows))

    
    def valid_moves(self) -> list[Callable[[], None]]:
        """Return a list of move functions that are currently possible, based on the location of the empty square."""
        empty_square = self.puzzle.index(0)
        
        # TODO: update these lambda functions to determine if each move is valid
        move_checks = {
            self.up: lambda: empty_square == 0, 
            self.down: lambda: empty_square == 0,
            self.left: lambda: empty_square == 0,
            self.right: lambda: empty_square == 0
        }
        
        # TODO: return a list comprehension which builds a list of functions
        # corresponding to valid moves
        raise NotImplementedError('valid moves')


    def up(self) -> None:
        """Move a tile up"""

        raise NotImplementedError('up')
  

    def down(self) -> None:
        """Move a tile down"""
        
        raise NotImplementedError('down')
  

    def right(self) -> None:
        """Move a tile right"""
        
        raise NotImplementedError('right')
  

    def left(self) -> None:
        """Move a tile left"""
        
        raise NotImplementedError('left')
    

    def scramble(self, i: int) -> None:
        """Make n random moves to scramble the puzzle."""
        
        raise NotImplementedError('scramble')


    def solved(self) -> bool:
        """Determine whether or not the puzzle is solved."""

        raise NotImplementedError('solved')
    

def play_game():
    """Play game until solved."""
    pzl = SlidingPuzzle(4, 4)
    pzl.scramble(N_SCRAMBLES)

    while not pzl.solved():
        print()
        print(pzl)
        cmd = input('\n  w\na s d\n  ').strip()
        match cmd:
            case 'w':
                requested_function = pzl.up
            case 'a':
                requested_function = pzl.left
            case 's':
                requested_function = pzl.down
            case 'd':
                requested_function = pzl.right
        if requested_function in pzl.valid_moves():
            requested_function()
        else:
            print("That's not a valid move!")

    print()
    print(pzl)
    print('*** Well done! ***')
    print()
    
# ======

if __name__=='__main__':
   play_game()