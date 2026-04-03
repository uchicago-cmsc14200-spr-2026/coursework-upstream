"""
CMSC 14200, Spring 2026
Homework 2, Task 2

People consulted:
   List anyone (other than the course staff) that you consulted about
   this assignment.

Online resources consulted:
   List the URLs of any online resources other than the course text and
   the official Python language documentation that you used to complete
   this assignment.
"""


import math

from quadtree import Point, Region, QuadTree


def empty_quadtree(w: int, h: int) -> QuadTree:
    """
    Initialize a quadtree with top-left corner (0, 0) and the
    given width and height values
    """
    return QTLeafNode(Region(Point(0, 0), w, h), None)


## Helper functions involving regions.
##
## You should implement them, and look out for opportunities
## to use them in the classes below.


def region_west_half(region: Region) -> int:
    """How many units wide are the northwest and southwest quadrants"""
    raise NotImplementedError("TODO")


def region_east_half(region: Region) -> int:
    """How many units wide are the northeast and southeast quadrants"""
    raise NotImplementedError("TODO")


def region_north_half(region: Region) -> int:
    """How many units tall are the northwest and northeast quadrants"""
    raise NotImplementedError("TODO")


def region_south_half(region: Region) -> int:
    """How many units tall are the southwest and southeast quadrants"""
    raise NotImplementedError("TODO")


def region_nw_corner(region: Region) -> Point:
    """The top-left corner of the northwest quadrant"""
    raise NotImplementedError("TODO")


def region_ne_corner(region: Region) -> Point:
    """The top-left corner of the northeast quadrant"""
    raise NotImplementedError("TODO")


def region_sw_corner(region: Region) -> Point:
    """The top-left corner of the southwest quadrant"""
    raise NotImplementedError("TODO")


def region_se_corner(region: Region) -> Point:
    """The top-left corner of the southeast quadrant"""
    raise NotImplementedError("TODO")


def region_center(region: Region) -> Point:
    """
    The center point of the region, i.e., the top-left corner
    of the southeast quadrant
    """
    return region_se_corner(region)


## Helper function for insertion.
##
## You should implement it, and look out for opportunities
## to use it in the QTLeafNode class.


def _make_leaf_or_split(region: Region, points: list[Point]) -> QuadTree:
    """
    Given a list of points within a region, create a quadtree.

    Inputs:
        points: Can include zero, one, or more points.

    Returns:
        If zero or one points in the list, the result is a leaf node.
        If two or more points in the list, the result is an inner node
            with the points distributed in the appropriate quadrants.

    Raises:
        ValueError if any of the input points is not contained
        within the region.
    """
    raise NotImplementedError("TODO")


## QTLeafNode class


class QTLeafNode(QuadTree):
    """
    Quadtree leaf nodes.

    A quirky characteristic of the representation we choose here
    is that a leaf contains _either_ zero points or one point.
    """
    _region: Region
    _optional_point: Point | None

    def __init__(self, region: Region, optional_point: Point | None) -> None:
        """Constructor"""
        self._region = region
        self._optional_point = optional_point

    def __str__(self) -> str:
        """Simple string representation of a point"""
        return f"{self._region}: {self._optional_point}"

    # TODO:
    # Implement all of the required methods from the QuadTree ABC
    # here in the QTLeafNode class.


## QTInnerNode class


class QTInnerNode(QuadTree):
    """
    Quadtree inner nodes.

    Notice that each of the four quadrants is an arbitrary QuadTree,
    which means either a QTLeafNode or a QTInnerNode.
    """
    _region: Region
    _ne: QuadTree
    _nw: QuadTree
    _sw: QuadTree
    _se: QuadTree

    def __init__(
        self,
        region: Region,
        ne: QuadTree,
        nw: QuadTree,
        sw: QuadTree,
        se: QuadTree,
    ) -> None:
        """
        Constructor.

        Notice that the children arguments appear in counter-clockwise
        order starting with the northeast quadrant.
        """
        self._region = region
        self._ne = ne
        self._nw = nw
        self._sw = sw
        self._se = se

    def __str__(self) -> str:
        """String representation of inner nodes."""
        def str_node(depth: int, qt: QuadTree) -> str:
            if isinstance(qt, QTLeafNode):
                return str(qt)
            elif isinstance(qt, QTInnerNode):
                tab = "  " * depth
                str_ne = f"\n{tab}ne: {str_node(depth + 1, qt._ne)}"
                str_nw = f"\n{tab}nw: {str_node(depth + 1, qt._nw)}"
                str_sw = f"\n{tab}sw: {str_node(depth + 1, qt._sw)}"
                str_se = f"\n{tab}se: {str_node(depth + 1, qt._se)}"
                return "".join([str_ne, str_nw, str_sw, str_se])
            else:
                return "QuadTree.__str__(???)"

        return str_node(0, self)

    # TODO:
    # Implement all of the required methods from the QuadTree ABC
    # here in the QTInnerNode class.


# We do not intend to run this Python file as a main program.
# But we include a __main__ definition below with constructor
# calls, as a way to nudge mypy to typecheck the implementations
# of abstract methods in the classes above.

if __name__ == "__main__":
    empty_region = Region(Point(0, 0), 0, 0)
    QTLeafNode(empty_region, None)
    QTInnerNode(
        empty_region,
        QTLeafNode(empty_region, None),
        QTLeafNode(empty_region, None),
        QTLeafNode(empty_region, None),
        QTLeafNode(empty_region, None),
    )
