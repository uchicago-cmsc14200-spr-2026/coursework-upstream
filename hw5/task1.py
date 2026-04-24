"""
CMSC 14200, Spring 2026
Homework 5, Task 1

People consulted:
   List anyone (other than the course staff) that you consulted about
   this assignment.

Online resources consulted:
   List the URLs of any online resources other than the course text and
   the official Python language documentation that you used to complete
   this assignment.
"""

# Task 1: Player-related queries

import pandas as pd
from load_data import load_data

# load in data
data = load_data()


def get_players_by_partial_name(fragment: str) -> pd.DataFrame:
    """
    Look up players whose names contain a given substring.

    Finds all players whose names include the specified fragment
    (case insensitive).

    Inputs:
        fragment (str): Substring to search for within player names.

    Returns (pd.DataFrame): A DataFrame containing 'personId' and
    'personName' columns of matching players.
    """
    raise NotImplementedError("TODO")


def get_ppg_by_name(name: str) -> float:
    """
    Retrieve the average points per game (PPG) for a player with an
    exact name match (case sensitive). Assume that every player name
    in the data set is unique.

    Raise a ValueError if there is no such player in the data set.

    Inputs:
        name (str): The exact name of the player (case sensitive).

    Returns (float): Average points per game for the matching player.
    """
    raise NotImplementedError


def total_minutes_played(name: str) -> float:
    """
    Calculate the total minutes played for a player with an exact name
    match (case sensitive). Assume that every player name in the data
    set is unique.

    Raise a ValueError if there is no such player in the data set.

    Inputs:
        name (str): The exact name of the player (case sensitive).

    Returns (float): The total number of minutes the player has played,
    expressed as a whole number and fraction. (i.e., a second is 1/60th
    of a minute)
    """
    raise NotImplementedError("TODO")
