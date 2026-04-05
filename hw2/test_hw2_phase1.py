"""
CMSC 14200, Spring 2026
Homework 2, Phase 1 Tests
"""

import pytest

from quadtree import Point, Region

import task1
import task2


## TASK 1


def test_task1_mean_01() -> None:
    assert task1.mean([]) is None


def test_task1_mean_02() -> None:
    assert task1.mean([1]) == 1


def test_task1_median_01() -> None:
    assert task1.median([]) is None


def test_task1_median_02() -> None:
    assert task1.median([1]) == 1


def test_task1_median_03() -> None:
    assert task1.median([1, 2]) in ((1, 2), (2, 1))


def test_task1_mode_01() -> None:
    assert task1.mode([]) == []


def test_task1_sample_interactions() -> None:
    assert task1.mean([1, 2]) == 1.5
    assert task1.mean([1, 2, 141, 14200, 14300]) == 5728.8
    assert task1.mean([]) == None
    assert task1.median([1, 20, 300]) == 20
    assert task1.median([1, 20, 300, 4000]) in ((20, 300), (300, 20))
    assert task1.mode([1, 4, 2, 0, 0]) == [0]
    assert set(task1.mode([1, 4, 2])) == set([1, 2, 4])
    assert task1.mode([]) == []


## TASK 2


def test_task2_region_4_4_dimensions() -> None:
    r = Region(Point(0, 0), 4, 4)
    assert task2.region_west_half(r) == 2
    assert task2.region_east_half(r) == 2
    assert task2.region_north_half(r) == 2
    assert task2.region_south_half(r) == 2


def test_task2_region_7_5_dimensions() -> None:
    r = Region(Point(0, 0), 7, 5)
    assert task2.region_west_half(r) == 4
    assert task2.region_east_half(r) == 3
    assert task2.region_north_half(r) == 3
    assert task2.region_south_half(r) == 2


def test_task2_region_4_4_center() -> None:
    r = Region(Point(0, 0), 4, 4)
    assert task2.region_center(r) == Point(2, 2)


def test_task2_region_7_5_center() -> None:
    r = Region(Point(0, 0), 7, 5)
    assert task2.region_center(r) == Point(4, 3)


def test_task2_make_leaf_or_split_0() -> None:
    r = Region(Point(0, 0), 4, 4)
    qt = task2._make_leaf_or_split(r, [])
    assert isinstance(qt, task2.QTLeafNode)
    assert qt.num_points() == 0


def test_task2_make_leaf_or_split_1() -> None:
    r = Region(Point(0, 0), 4, 4)
    qt = task2._make_leaf_or_split(r, [Point(0, 0)])
    assert isinstance(qt, task2.QTLeafNode)
    assert qt.num_points() == 1


def test_task2_make_split_or_split_2() -> None:
    r = Region(Point(0, 0), 4, 4)
    qt = task2._make_leaf_or_split(r, [Point(0, 0), Point(3, 3)])
    assert isinstance(qt, task2.QTInnerNode)
    assert qt.num_points() == 2



def test_task2_sample_qt0() -> None:
    qt = task2.empty_quadtree(0, 0)
    assert qt.num_points() == 0
    assert len(qt.children()) == 0


def test_task2_sample_qt1() -> None:
    qt = task2.empty_quadtree(1, 1)
    assert qt.num_points() == 0
    qt = qt.insert(Point(0, 0))
    assert qt.num_points() == 1
    assert len(qt.children()) == 0


def test_task2_sample_qt4() -> None:
    """
    Create a 4 x 4 quadtree with points at the very top-left and
    bottom-right corners, and test a couple expected properties.
    """
    qt = task2.empty_quadtree(4, 4)
    qt = qt.insert(Point(0, 0))
    qt = qt.insert(Point(3, 3))
    assert qt.num_points() == 2
    assert isinstance(qt, task2.QTInnerNode)
    assert qt._ne.region() == Region(Point(2, 0), 2, 2)
    assert len(qt.children()) == 4


def test_task2_sample_qt8() -> None:
    """
    Create an 8 x 8 quadtree with points along the main diagonal,
    and test some expected properties.
    """
    qt = task2.empty_quadtree(8, 8)
    for i in range(8):
        qt = qt.insert(Point(i, i))

    assert qt.height() == 3
    assert qt.num_points() == 8
    assert len(qt.children()) == 4

    assert isinstance(qt, task2.QTInnerNode)
    assert len(qt._ne.children()) == 0
    assert qt._ne.region() == Region(Point(4, 0), 4, 4)
    assert qt._ne.points() == []

    assert len(qt._nw.children()) == 4
    assert isinstance(qt._nw, task2.QTInnerNode)
    assert len(qt._nw._ne.children()) == 0
    assert qt._nw._ne.region() == Region(Point(2, 0), 2, 2)
    assert qt._nw._ne.points() == []
    assert isinstance(qt._nw._nw, task2.QTInnerNode)
    assert qt._nw._nw._ne.region() == Region(Point(1, 0), 1, 1)
    assert qt._nw._nw._ne.points() == []
    assert qt._nw._nw._nw.region() == Region(Point(0, 0), 1, 1)
    assert qt._nw._nw._nw.points() == [Point(0, 0)]
    assert qt._nw._nw._sw.region() == Region(Point(0, 1), 1, 1)
    assert qt._nw._nw._sw.points() == []
    assert qt._nw._nw._se.region() == Region(Point(1, 1), 1, 1)
    assert qt._nw._nw._se.points() == [Point(1, 1)]

    assert len(qt._sw.children()) == 0

    assert len(qt._se.children()) == 4
    assert isinstance(qt._se, task2.QTInnerNode)
    assert qt._se._ne.region() == Region(Point(6, 4), 2, 2)
    assert qt._se._ne.points() == []
