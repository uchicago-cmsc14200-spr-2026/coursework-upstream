"""
CMSC 14200, Spring 2026
Homework 2, Task 3

People consulted:
   List anyone (other than the course staff) that you consulted about
   this assignment.

Online resources consulted:
   List the URLs of any online resources other than the course text and
   the official Python language documentation that you used to complete
   this assignment.
"""


import math
import pygame
import random
import sys

from quadtree import Point, Region, QuadTree
from task2 import empty_quadtree, QTLeafNode, QTInnerNode



class QuadTreeGUI:

    surface: pygame.Surface
    clock: pygame.time.Clock

    ## TODO:
    ## Add additional instance attributes that your application
    ## needs to keep track of. Remember to include type annotations.

    ## INIT

    def __init__(
        self, width: int, height: int, initial_points: list[Point] | int
    ) -> None:
        """
        Constructor

        Inputs:
            width: Width of the region to be represented
            height: Height of the region
            initial_points: Either a list of points, or a number
              indicating how many points to randomly generate
        """
        pygame.init()
        pygame.display.set_caption("Quad Tree GUI")
        self.surface = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()
        self.run_event_loop()

        ## TODO: Add code to the constructor as needed

    ## CONTROLLER

    def run_event_loop(self) -> None:
        """Event loop"""

        while True:
            events = pygame.event.get()

            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                elif event.type == pygame.MOUSEBUTTONUP:
                    ## TODO:
                    ## Add code here so that mouse clicks
                    ## while in mode B insert points into
                    ## the quadtree. Don't do any drawing
                    ## here; that goes in the VIEW section.
                    pass

                else:
                    pass

            self.draw_window()
            self.clock.tick(24)

    # VIEW

    def draw_window(self) -> None:
        """
        Draw the current quadtree, according to the requirements
        described on the Homework 2 page.
        """

        ## TODO:
        ## Add code here to draw the current quadtree.

        pygame.display.update()


if __name__ == "__main__":
    # TODO:
    # Add code here to process the different forms
    # of command-line arguments, and then call the
    # QuadTreeGUI constructor accordingly.

    print(sys.argv)
    QuadTreeGUI(400, 600, [])
