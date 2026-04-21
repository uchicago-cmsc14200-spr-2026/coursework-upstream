"""
CMSC 14200, Spring 2026
Homework 2, Phase 2 Tests
"""

import pytest
import sys

from quadtree import Point, Region, QuadTree

import task1
import task2


## TASK 1


def test_task1_mean_01() -> None:
    assert task1.mean([]) is None


def test_task1_mean_02() -> None:
    assert task1.mean([1]) == 1


def test_task1_mean_03() -> None:
    assert task1.mean([2, 2, 2, 4, 4, 4]) == 3


def test_task1_mean_04() -> None:
    assert task1.mean([5, 1, 4, 3, 3, 2]) == 3


def test_task1_median_01() -> None:
    assert task1.median([]) is None


def test_task1_median_02() -> None:
    assert task1.median([1]) == 1


def test_task1_median_03() -> None:
    assert task1.median([1, 2]) in ((1, 2), (2, 1))


def test_task1_median_04() -> None:
    assert task1.median([4, 2, 2, 4, 2, 4]) in ((2, 4), (4, 2))


def test_task1_median_05() -> None:
    assert task1.median([2, 1, 14, 3, 13, 6, 5, 0, 4, 10, 7, 12, 11, 8, 9]) == 7


def test_task1_median_06() -> None:
    assert task1.median(
        [2, 9, 14, 0, 5, 12, 8, 3, 10, 13, 11, 15, 1, 4, 6, 7]
    ) in (
        (7, 8),
        (8, 7),
    )


def test_task1_mode_01() -> None:
    assert task1.mode([]) == []


def test_task1_mode_02() -> None:
    assert set(task1.mode([7, 4, 3, 1, 7, 8, 5, 2, 6, 6])) == set([6, 7])


def test_task1_mode_03() -> None:
    assert task1.mode(
        [13, 8, 12, 2, 10, 2, 6, 14, 4, 0, 9, 5, 7, 1, 3, 11]
    ) == [2]


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


def test_task2_region_7_4_dimensions() -> None:
    r = Region(Point(0, 0), 7, 4)
    assert task2.region_west_half(r) == 4
    assert task2.region_east_half(r) == 3
    assert task2.region_north_half(r) == 2
    assert task2.region_south_half(r) == 2


def test_task2_region_8_5_dimensions() -> None:
    r = Region(Point(0, 0), 8, 5)
    assert task2.region_west_half(r) == 4
    assert task2.region_east_half(r) == 4
    assert task2.region_north_half(r) == 3
    assert task2.region_south_half(r) == 2


def test_task2_region_1_4_dimensions() -> None:
    r = Region(Point(0, 0), 1, 4)
    assert task2.region_west_half(r) == 1
    assert task2.region_east_half(r) == 0
    assert task2.region_north_half(r) == 2
    assert task2.region_south_half(r) == 2


def test_task2_region_7_1_dimensions() -> None:
    r = Region(Point(0, 0), 7, 1)
    assert task2.region_west_half(r) == 4
    assert task2.region_east_half(r) == 3
    assert task2.region_north_half(r) == 1
    assert task2.region_south_half(r) == 0


def test_task2_region_100_40_dimensions() -> None:
    r = Region(Point(0, 0), 100, 40)
    assert task2.region_west_half(r) == 50
    assert task2.region_east_half(r) == 50
    assert task2.region_north_half(r) == 20
    assert task2.region_south_half(r) == 20


def test_task2_region_75_120_dimensions() -> None:
    r = Region(Point(0, 0), 75, 120)
    assert task2.region_west_half(r) == 38
    assert task2.region_east_half(r) == 37
    assert task2.region_north_half(r) == 60
    assert task2.region_south_half(r) == 60


def test_task2_region_4_4_center() -> None:
    r = Region(Point(0, 0), 4, 4)
    assert task2.region_center(r) == Point(2, 2)


def test_task2_region_7_5_center() -> None:
    r = Region(Point(0, 0), 7, 5)
    assert task2.region_center(r) == Point(4, 3)


def test_task2_region_7_4_center() -> None:
    r = Region(Point(0, 0), 7, 4)
    assert task2.region_center(r) == Point(4, 2)


def test_task2_region_8_5_center() -> None:
    r = Region(Point(0, 0), 8, 5)
    assert task2.region_center(r) == Point(4, 3)


def test_task2_region_1_4_center() -> None:
    r = Region(Point(0, 0), 1, 4)
    assert task2.region_center(r) == Point(1, 2)


def test_task2_region_7_1_center() -> None:
    r = Region(Point(0, 0), 7, 1)
    assert task2.region_center(r) == Point(4, 1)


def test_task2_region_100_40_center() -> None:
    r = Region(Point(0, 0), 100, 40)
    assert task2.region_center(r) == Point(50, 20)


def test_task2_region_75_120_center() -> None:
    r = Region(Point(0, 0), 75, 120)
    assert task2.region_center(r) == Point(38, 60)


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


def test_task2_contains_qt0() -> None:
    qt = task2.empty_quadtree(0, 0)
    assert not qt.contains(Point(0, 0))


def test_task2_contains_qt1() -> None:
    qt = task2.empty_quadtree(1, 1)
    assert not qt.contains(Point(0, 0))
    qt = qt.insert(Point(0, 0))
    assert qt.contains(Point(0, 0))


def test_task2_contains_qt4() -> None:
    qt = task2.empty_quadtree(4, 4)
    qt = qt.insert(Point(0, 0))
    qt = qt.insert(Point(3, 3))
    assert qt.contains(Point(0, 0))
    assert qt.contains(Point(3, 3))
    assert not qt.contains(Point(0, 1))
    assert not qt.contains(Point(1, 1))
    assert not qt.contains(Point(2, 2))


def test_task2_contains_qt8() -> None:
    qt = task2.empty_quadtree(8, 8)
    for i in range(8):
        qt = qt.insert(Point(i, i))

    for x in range(8):
        for y in range(8):
            if x == y:
                assert qt.contains(Point(x, y))
            else:
                assert not qt.contains(Point(x, y))


def test_task2_insert_out_of_bounds_0() -> None:
    qt = task2.empty_quadtree(0, 0)
    with pytest.raises(ValueError):
        qt = qt.insert(Point(-10, 0))
    with pytest.raises(ValueError):
        qt = qt.insert(Point(0, -10))
    with pytest.raises(ValueError):
        qt = qt.insert(Point(0, 0))


def test_task2_insert_out_of_bounds_1() -> None:
    qt = task2.empty_quadtree(1, 1)
    with pytest.raises(ValueError):
        qt = qt.insert(Point(-10, 0))
    with pytest.raises(ValueError):
        qt = qt.insert(Point(0, -10))
    with pytest.raises(ValueError):
        qt = qt.insert(Point(1, 1))


def test_task2_insert_out_of_bounds_8() -> None:
    qt = task2.empty_quadtree(8, 8)
    for i in range(8):
        qt = qt.insert(Point(i, i))
    with pytest.raises(ValueError):
        qt = qt.insert(Point(-10, 0))
    with pytest.raises(ValueError):
        qt = qt.insert(Point(0, -10))
    with pytest.raises(ValueError):
        qt = qt.insert(Point(8, 8))


def read_file(filename: str) -> tuple[int, int, list[Point]]:
    with open(filename, "r") as file:
        points: list[Point] = []
        w = int(file.readline())
        h = int(file.readline())
        for line in file:
            [x, y] = map(int, line.strip().split())
            points.append(Point(x, y))
        return (w, h, points)


def read_qt_from_file(filename: str) -> QuadTree:
    w, h, points = read_file(filename)
    qt = task2.empty_quadtree(w, h)
    for point in points:
        qt = qt.insert(point)
    return qt


def num_paths(qt: QuadTree) -> int:
    return len(all_path_depths(qt))


def all_path_depths(qt: QuadTree) -> list[int]:
    return _all_path_depths(0, qt)


def _all_path_depths(cur_depth: int, qt: QuadTree) -> list[int]:
    if isinstance(qt, task2.QTLeafNode):
        return [cur_depth]
    elif isinstance(qt, task2.QTInnerNode):
        list_ne = _all_path_depths(1 + cur_depth, qt._ne)
        list_nw = _all_path_depths(1 + cur_depth, qt._nw)
        list_sw = _all_path_depths(1 + cur_depth, qt._sw)
        list_se = _all_path_depths(1 + cur_depth, qt._se)
        return list_ne + list_nw + list_sw + list_se
    else:
        assert False


def test_task2_points_height_example_1() -> None:
    qt = read_qt_from_file("data/example-1.txt")
    assert qt.num_points() == 3
    assert qt.height() == 1
    assert num_paths(qt) == 4


def test_task2_points_height_example_2() -> None:
    qt = read_qt_from_file("data/example-2.txt")
    assert qt.num_points() == 10
    assert qt.height() == 4
    assert num_paths(qt) == 19


def test_task2_points_height_example_3() -> None:
    qt = read_qt_from_file("data/example-3.txt")
    assert qt.num_points() == 142
    assert qt.height() == 7
    assert num_paths(qt) == 301


def test_task2_paths_example_1() -> None:
    qt = read_qt_from_file("data/example-1.txt")
    assert num_paths(qt) == 4


def test_task2_paths_example_2() -> None:
    qt = read_qt_from_file("data/example-2.txt")
    assert num_paths(qt) == 19


def test_task2_paths_example_3() -> None:
    qt = read_qt_from_file("data/example-3.txt")
    assert num_paths(qt) == 301
