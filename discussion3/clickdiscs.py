from __future__ import annotations

import math
import sys
import pygame

"""
Your GUI should present nine discs, A through I, on the screen. When
you click on the screen, if you clicked within any disc (anywhere
within the radius of that disc, not just on its center), the app
should print a corresponding message to the terminal. If a click is on
no disc at all, that should also be printed to the terminal.
"""

DEFAULT_BGCOLOR = (30,144,255)
DEFAULT_WIDTH   = 400
DEFAULT_HEIGHT  = 400

DISC_COLOR      = (222,222,222)
DISC_RADIUS     = 24

# type synonym for convenience
rgb = tuple[int,int,int]

class Disc:

  center : tuple[int,int]
  radius : int
  label  : str

  def __init__(self, c : tuple[int,int], r : int, b : str):
    self.label = b.strip()
    if len(self.label)!=1 and not('A'<=self.label<='Z'):
      raise ValueError('please supply a label that is one capital letter')
    self.center = c
    self.radius = r

  # maybe write a method "clicked_within"?
  
  def __repr__(self) -> str:
    return f'Disc({self.center},{self.radius},{self.label})'
  
class ClickDiscs:

    bgcolor : rgb
    width   : int
    height  : int
    surface : pygame.Surface
    clock   : pygame.time.Clock
    discs   : set[Disc]
    
    def __init__(self,
                 bgcolor : rgb = DEFAULT_BGCOLOR,
                 width   : int = DEFAULT_WIDTH,
                 height  : int = DEFAULT_HEIGHT) -> None:
        self.bgcolor = bgcolor if bgcolor else DEFAULT_BGCOLOR
        self.width   = width if width else DEFAULT_WIDTH
        self.height  = height if height else DEFAULT_HEIGHT
        self.discs   = {}
        
    def run_app(self) -> None:
        pygame.init()
        pygame.display.set_caption("ClickDiscs")
        self.surface = pygame.display.set_mode((self.width,self.height))
        self.clock = pygame.time.Clock()
        self.run_event_loop()

    def quit_app(self) -> None:
        pygame.quit()
        sys.exit()

    def draw_window(self) -> None:
        self.surface.fill(self.bgcolor)
        pygame.display.update()

    def run_event_loop(self) -> None:
        while True:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.quit_app()
                elif event.type == pygame.MOUSEMOTION:
                    pass
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pass
                elif event.type == pygame.MOUSEBUTTONUP:
                    pass
                elif event.type == pygame.KEYDOWN:
                    pass
                elif event.type == pygame.KEYUP:
                    pass
            self.draw_window()
            self.clock.tick(24) # throttle redraws at 24fps (frames per second)

# ========

if __name__ == "__main__":
    cd = ClickDiscs()
    cd.run_app()

