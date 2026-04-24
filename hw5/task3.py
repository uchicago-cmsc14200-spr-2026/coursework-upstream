"""
CMSC 14200, Spring 2026
Homework 5, Task 3

People consulted:
   List anyone (other than the course staff) that you consulted about
   this assignment.

Online resources consulted:
   List the URLs of any online resources other than the course text and
   the official Python language documentation that you used to complete
   this assignment.
"""

# Task 3: Calendar-related query

import pandas as pd
from load_data import load_data

# load in data
data = load_data()


def played_on_date(date: str) -> set[str]:
    """
    Returns the set of unique player names for all players who
    participated in a game on a specific date, according to the data
    set.

    It is not necessary to test that the date is in a particular span
    of time or that it is well-formatted; validation of input format
    and date range is the responsibility of the caller.

    Inputs:
        date (str): The date of interest in 'YYYY-MM-DD' format
        (e.g., '2024-02-03').

    Returns (set[str]): A set containing the names of all unique
    players who played on the specified date.
    """
    raise NotImplementedError("TODO")
