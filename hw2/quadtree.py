#
# QuadTree base class
#
# DO NOT MODIFY THIS FILE
#

from abc import ABC, abstractmethod


class Point:
    """
    A point in a 2-D plane with origin (0, 0).
    """

    x: int
    y: int

    def __init__(self, x: int, y: int) -> None:
        """Constructor"""
        self.x = x
        self.y = y

    def __str__(self) -> str:
        """Simple string representation of a point"""
        return f"({self.x}, {self.y})"

    def __eq__(self, other: object) -> bool:
        """
        Check equality of points by checking their coordinates.

        Defining this "dunder method" (double-underscore method)
        with the special name `__eq__` allows us to write

            point1 == point2

        instead of:

            point1.__eq__(point2)

        Defining this method also allows us to write, for example,
        `point in points` to check for the presence of a given
        point in a list.

        The static type annotation `other: object` followed by a
        run-time `isinstance` check in the code is a preferred
        way of implementing these special methods, for reasons
        we do not need to worry about at this point in the course.
        """
        if not isinstance(other, Point):
            return NotImplemented

        return self.x == other.x and self.y == other.y

    def __add__(self, other: object) -> "Point":
        """
        Add two points (treated as vectors from the origin (0, 0)).

        This "dunder method" allows us to write

            point1 + point2

        instead of:

            point1.__add__(point2)
        """
        if not isinstance(other, Point):
            return NotImplemented

        return Point(self.x + other.x, self.y + other.y)

    def __mul__(self, n: object) -> "Point":
        """
        Scale each dimension of a point (vector) by an integer factor.

        This "dunder method" allows us to write

            point * 1.5

        instead of:

            point.__mul__(1.5)
        """
        if not isinstance(n, int):
            return NotImplemented

        return Point(n * self.x, n * self.y)


class Region:
    """
    A rectangular region, or grid, of integer coordinates, defined
    by a top-left corner plus width and height values.

    Width and/or height are allowed to be zero.
    """

    corner: Point
    width: int
    height: int

    def __init__(self, corner: Point, w: int, h: int) -> None:
        """Constructor"""
        self.corner = corner
        self.width = w
        self.height = h

    def __str__(self) -> str:
        """Simple string representation of a region"""
        return f"({self.corner} {self.width} x {self.height})"

    def __eq__(self, other: object) -> bool:
        """Check equality."""
        if not isinstance(other, Region):
            return NotImplemented

        return (
            self.corner == other.corner
            and self.width == other.width
            and self.height == other.height
        )

    def contains(self, pt: Point) -> bool:
        """Check whether a point is contained within the region."""
        return (
            pt.x >= self.corner.x
            and pt.x < self.corner.x + self.width
            and pt.y >= self.corner.y
            and pt.y < self.corner.y + self.height
        )


class QuadTree(ABC):
    """
    Quadtree base class.
    """

    @abstractmethod
    def region(self) -> Region:
        """Get the spatial region represented by this quadtree"""
        raise NotImplementedError

    @abstractmethod
    def points(self) -> list[Point]:
        """Get the points contained in this quadtree"""
        raise NotImplementedError

    @abstractmethod
    def children(self) -> list["QuadTree"]:
        """Get the children of this quadtree"""
        raise NotImplementedError

    ### MAIN QUADTREE OPERATIONS ###

    @abstractmethod
    def contains(self, pt: Point) -> bool:
        """Check whether a given point is in the quadtree"""
        raise NotImplementedError

    @abstractmethod
    def insert(self, pt: Point) -> "QuadTree":
        """
        Insert a point into the quadtree, returning an updated
        quadtree. If the point is already contained, the
        quadtree is returned without any change.

        Raises:
            ValueError if any of the point is not contained
            within the region.
        """
        raise NotImplementedError

    ### BASIC STATS ###

    def num_points(self) -> int:
        """Calculuate the number of points in this quadtree"""
        return len(self.points())

    @abstractmethod
    def num_nodes(self) -> int:
        """
        Calculate the number of nodes, both leaf nodes and inner nodes,
        that comprise this quadtree
        """
        raise NotImplementedError

    @abstractmethod
    def height(self) -> int:
        """
        Calculate the height of this quadtree, that is, the number
        of edges on the longest path from the root to a leaf node
        in the tree.
        """
        raise NotImplementedError
