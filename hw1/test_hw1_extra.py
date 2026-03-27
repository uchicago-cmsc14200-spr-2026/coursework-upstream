"""
CMSC 14200, Spring 2026
Homework 1, Extra Tests
"""

import pytest

import task1
import task2
import task3
from task4 import Card


## TASK 1
## Write your own extra tests here


## TASK 2
## Write your own extra tests here


## TASK 3
## Write your own extra tests here


## TASK 4
## Write your own extra tests here


def test_task4_no_overlapping_features() -> None:
    """
    Write a test that creates two cards with no overlapping feature names.
    Check that conflicting_features returns the correct value (which is
    the empty dictionary).
    """
    raise NotImplementedError("TODO: test_no_overlapping_features")


def test_task4_no_conflicting_features() -> None:
    """
    Write a test that creates two cards with one common feature and
    no conflicting features. Check that conflicting_features returns
    the correct value (which is the empty dictionary).
    """
    raise NotImplementedError("TODO: test_no_conflicting_features")


def test_task4_one_conflicting_feature() -> None:
    """
    Write a test that creates two cards with two common feature names,
    called "shape" and "number". The two cards should have the same value,
    "square", for "shape". That is, {"shape": "square"} is a common feature.
    For "number", the two cards should have different values, "1" and "7".
    Check that conflicting_features returns a dictionary that maps "number"
    to a pair with "1" and "7".
    """
    raise NotImplementedError("TODO: test_one_conflicting_feature")


def test_task4_two_conflicting_features() -> None:
    """
    Write a test that creates two cards with three conflicting features,
    and check that conflicting_features returns the correct value.
    """
    raise NotImplementedError("TODO: test_two_conflicting_features")
