"""
CMSC 14200, Spring 2026
Homework 1, Phase 2 Tests
"""

import pytest

import task1
import task2
import task3
from task4 import Card


## TASK 1


def test_task1_to_base_2_0() -> None:
    assert task1.to_base_n(2, 0) == "0_2_0"


def test_task1_to_base_2_7() -> None:
    assert task1.to_base_n(2, 7) == "0_2_111"


def test_task1_to_base_2_8() -> None:
    assert task1.to_base_n(2, 8) == "0_2_1000"


def test_task1_to_base_2_142() -> None:
    assert task1.to_base_n(2, 142) == "0_2_10001110"


# NOTE: Compared to the individual tests for to_base_n(2, ...) above,
# the following definition includes multiple tests for to_base_n(9, ...)
# in a single "parameterized" test. Don't worry about how this pytest
# library function is working. Just know that you can add more tests by
# adding to the lists that appear in @pytest.mark.parametrize annotations
# before each test.


@pytest.mark.parametrize(
    "n, expected", [(0, "0_9_0"), (81, "0_9_100"), (80, "0_9_88")]
)
def test_task1_to_base_9(n: int, expected: str) -> None:
    assert task1.to_base_n(9, n) == expected


def test_task1_from_base_2_111() -> None:
    assert task1.from_base_n("0_2_111") == 7


def test_task1_from_base_9_88() -> None:
    assert task1.from_base_n("0_9_88") == 80


@pytest.mark.parametrize("s, expected", [("0_9_088", 80), ("0_9_00088", 80)])
def test_task1_leading_zeroes(s: str, expected: int) -> None:
    assert task1.from_base_n(s) == expected


def test_task1_to_base_3_0() -> None:
    assert task1.to_base_n(3, 0) == "0_3_0"


def test_task1_to_base_3_7() -> None:
    assert task1.to_base_n(3, 7) == "0_3_21"


def test_task1_to_base_3_8() -> None:
    assert task1.to_base_n(3, 8) == "0_3_22"


def test_task1_to_base_3_13() -> None:
    assert task1.to_base_n(3, 13) == "0_3_111"


def test_task1_to_base_5_44444444444() -> None:
    assert task1.to_base_n(5, 44444444444) == "0_5_1212010234210234"


def test_task1_to_base_6_44444444444() -> None:
    assert task1.to_base_n(6, 44444444444) == "0_6_32230102404512"


def test_task1_to_base_7_44444444444() -> None:
    assert task1.to_base_n(7, 44444444444) == "0_7_3132242354531"


def test_task1_to_base_8_44444444444() -> None:
    assert task1.to_base_n(8, 44444444444) == "0_8_513106063434"


def test_task1_to_base_9_44444444444() -> None:
    assert task1.to_base_n(9, 44444444444) == "0_9_136642051088"


def test_task1_from_base_5_11() -> None:
    assert task1.from_base_n("0_5_11") == 6


def test_task1_from_base_5_21() -> None:
    assert task1.from_base_n("0_5_21") == 11


def test_task1_from_base_6_31() -> None:
    assert task1.from_base_n("0_6_31") == 19


def test_task1_from_base_7_101() -> None:
    assert task1.from_base_n("0_7_101") == 50


def test_task1_from_base_5_44444444444() -> None:
    assert task1.from_base_n("0_5_44444444444") == 48828124


def test_task1_from_base_6_44444444444() -> None:
    assert task1.from_base_n("0_6_44444444444") == 290237644


def test_task1_from_base_7_44444444444() -> None:
    assert task1.from_base_n("0_7_44444444444") == 1318217828


def test_task1_from_base_8_44444444444() -> None:
    assert task1.from_base_n("0_8_44444444444") == 4908534052


def test_task1_from_base_9_44444444444() -> None:
    assert task1.from_base_n("0_9_44444444444") == 15690529804


## TASK 2


def assert_equal_task2(list1: list[list[int]], list2: list[list[int]]) -> None:
    # Sort both lists to make comparison easier
    list1.sort()
    list2.sort()
    assert list1 == list2


_1234 = list(range(1, 4))


@pytest.mark.parametrize(
    "budget, ints, expected",
    [
        (0, _1234, [[]]),
        (4, _1234, [[], [1], [2], [1, 2], [3], [1, 3]]),
        (
            6,
            _1234,
            [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]],
        ),
        (
            6,
            _1234,
            [[1, 2, 3], [2, 3], [1, 3], [3], [1, 2], [2], [1], []],
        ),
    ],
)
def test_task2_1234(
    budget: int, ints: list[int], expected: list[list[int]]
) -> None:
    assert_equal_task2(task2.affordable_subsequences(budget, ints), expected)


def test_task2_empty() -> None:
    assert_equal_task2(task2.affordable_subsequences(4, []), [[]])


@pytest.mark.parametrize(
    "budget, ints, expected",
    [
        (0, [1, 5, 7, 3, 2, 6], [[]]),
        (4, [1, 5, 7, 3, 2, 6], [[], [1], [2], [1, 2], [3], [1, 3]]),
        (
            6,
            [1, 5, 7, 3, 2, 6],
            [
                [1, 5],
                [1, 3, 2],
                [1, 3],
                [1, 2],
                [1],
                [5],
                [3, 2],
                [3],
                [2],
                [6],
                [],
            ],
        ),
    ],
)
def test_task2_157326(
    budget: int, ints: list[int], expected: list[list[int]]
) -> None:
    assert_equal_task2(task2.affordable_subsequences(budget, ints), expected)


@pytest.mark.parametrize(
    "budget, ints, expected",
    [
        (0, [100, 141, 111111, 14200, 22300, 9999999], [[]]),
        (100, [100, 141, 111111, 14200, 22300, 9999999], [[100], []]),
        (
            1000,
            [100, 141, 111111, 14200, 22300, 9999999],
            [[100, 141], [100], [141], []],
        ),
        (
            10000,
            [100, 141, 111111, 14200, 22300, 9999999],
            [[100, 141], [100], [141], []],
        ),
        (
            100000,
            [100, 141, 111111, 14200, 22300, 9999999],
            [
                [100, 141, 14200, 22300],
                [100, 141, 14200],
                [100, 141, 22300],
                [100, 141],
                [100, 14200, 22300],
                [100, 14200],
                [100, 22300],
                [100],
                [141, 14200, 22300],
                [141, 14200],
                [141, 22300],
                [141],
                [14200, 22300],
                [14200],
                [22300],
                [],
            ],
        ),
        (
            1000000,
            [100, 141, 111111, 14200, 22300, 9999999],
            [
                [100, 141, 111111, 14200, 22300],
                [100, 141, 111111, 14200],
                [100, 141, 111111, 22300],
                [100, 141, 111111],
                [100, 141, 14200, 22300],
                [100, 141, 14200],
                [100, 141, 22300],
                [100, 141],
                [100, 111111, 14200, 22300],
                [100, 111111, 14200],
                [100, 111111, 22300],
                [100, 111111],
                [100, 14200, 22300],
                [100, 14200],
                [100, 22300],
                [100],
                [141, 111111, 14200, 22300],
                [141, 111111, 14200],
                [141, 111111, 22300],
                [141, 111111],
                [141, 14200, 22300],
                [141, 14200],
                [141, 22300],
                [141],
                [111111, 14200, 22300],
                [111111, 14200],
                [111111, 22300],
                [111111],
                [14200, 22300],
                [14200],
                [22300],
                [],
            ],
        ),
    ],
)
def test_task2_bigger_numbers(
    budget: int, ints: list[int], expected: list[list[int]]
) -> None:
    assert_equal_task2(task2.affordable_subsequences(budget, ints), expected)


## TASK 3


def assert_equal_task3(
    dict1: dict[str, list[int]], dict2: dict[str, list[int]]
) -> None:
    # Sort to make comparison easier
    for key in dict1:
        dict1[key].sort()
    for key in dict2:
        dict2[key].sort()
    assert dict1 == dict2


d1 = {"id": 1, "favorite_num": 1, "scoops_of_ice_cream": 1}

d2 = {"id": 2, "favorite_num": 142, "scoops_of_ice_cream": 3}

d3 = {"id": 3, "scoops_of_ice_cream": 3}

d4 = {"id": 4, "favorite_num": 142, "year": 2026}


def test_task3_0() -> None:
    assert_equal_task3(task3.merge_dictionaries([]), {})


def test_task3_1() -> None:
    actual = task3.merge_dictionaries([d1])
    expected = {"id": [1], "favorite_num": [1], "scoops_of_ice_cream": [1]}
    assert_equal_task3(actual, expected)


def test_task3_1234() -> None:
    actual = task3.merge_dictionaries([d1, d2, d3, d4])
    expected = {
        "id": [1, 2, 3, 4],
        "favorite_num": [1, 142],
        "scoops_of_ice_cream": [1, 3],
        "year": [2026],
    }
    assert_equal_task3(actual, expected)


def test_task3_1234_reordered() -> None:
    actual = task3.merge_dictionaries([d1, d2, d3, d4])
    expected = {
        "year": [2026],
        "favorite_num": [142, 1],
        "id": [4, 1, 3, 2],
        "scoops_of_ice_cream": [1, 3],
    }
    assert_equal_task3(actual, expected)


d5 = {"id": 34, "red": 100, "green": 123, "blue": 255, "alpha": 255}

d6 = {"id": 77, "green": 253}

d7 = {"id": 85, "red": 200}

d8 = {"id": 99, "blue": 0}


def test_task3_5678() -> None:
    actual = task3.merge_dictionaries([d5, d6, d7, d8])
    expected = {
        "id": [34, 77, 85, 99],
        "red": [100, 200],
        "green": [123, 253],
        "blue": [255, 0],
        "alpha": [255],
    }
    assert_equal_task3(actual, expected)


def test_task3_5678_reordered() -> None:
    actual = task3.merge_dictionaries([d5, d6, d7, d8])
    expected = {
        "blue": [0, 255],
        "id": [77, 34, 99, 85],
        "alpha": [255],
        "red": [200, 100],
        "green": [253, 123],
    }
    assert_equal_task3(actual, expected)


def test_task3_empty() -> None:
    actual = task3.merge_dictionaries([])
    assert_equal_task3(actual, {})


def test_task3_singleton() -> None:
    actual = task3.merge_dictionaries([d8])
    expected = {"id": [99], "blue": [0]}
    assert_equal_task3(actual, expected)


def test_task3_duplicate() -> None:
    actual = task3.merge_dictionaries([d8, d8])
    expected = {"id": [99], "blue": [0]}
    assert_equal_task3(actual, expected)


## TASK 4


def test_task4_no_overlapping_features() -> None:
    """
    Write a test that creates two cards with no overlapping feature names.
    Check that conflicting_features returns the correct value (which is
    the empty dictionary).
    """
    card5 = Card({"color": "green", "shade": "light", "num": "8"})
    card6 = Card({"hat": "yellow", "food": "pasta", "bell": "no"})
    assert card5.conflicting_features(card6.features) == {}


def test_task4_no_conflicting_features() -> None:
    """
    Write a test that creates two cards with one common feature and
    no conflicting features. Check that conflicting_features returns
    the correct value (which is the empty dictionary).
    """
    card5 = Card({"hat": "green", "shade": "light", "num": "8"})
    card6 = Card({"hat": "green", "food": "pasta", "bell": "no"})
    assert card5.conflicting_features(card6.features) == {}


def test_task4_one_conflicting_feature() -> None:
    """
    Write a test that creates two cards with two common feature names,
    called "shape" and "number". The two cards should have the same value,
    "square", for "shape". That is, {"shape": "square"} is a common feature.
    For "number", the two cards should have different values, "1" and "7".
    Check that conflicting_features returns a dictionary that maps "number"
    to a pair with "1" and "7".
    """
    card5 = Card({"shape": "square", "number": "1", "num": "8"})
    card6 = Card({"shape": "square", "number": "7", "bell": "no"})
    assert card5.conflicting_features(card6.features) == {"number": ("1", "7")}


def test_task4_two_conflicting_features() -> None:
    """
    Write a test that creates two cards with three conflicting features,
    and check that conflicting_features returns the correct value.
    """
    card5 = Card({"hat": "green", "number": "8", "space": "yes", "num": "8"})
    card6 = Card(
        {"hat": "top_hat", "number": "20", "space": "no", "bell": "no"}
    )
    assert card5.conflicting_features(card6.features) == {
        "hat": ("green", "top_hat"),
        "number": ("8", "20"),
        "space": ("yes", "no"),
    }
