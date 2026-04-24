"""
CMSC 14200, Spring 2026
Homework 5, Task 2

People consulted:
   List anyone (other than the course staff) that you consulted about
   this assignment.

Online resources consulted:
   List the URLs of any online resources other than the course text and
   the official Python language documentation that you used to complete
   this assignment.
"""

# Task 2: Team-related queries

import pandas as pd
from load_data import load_data

# load in data
data = load_data()


def player_for(team: str) -> pd.DataFrame:
    """
    Returns a DataFrame of any players who have been a player for the
    specified team.

    Raise a ValueError if the team does not exist.

    Inputs:
        team (str): The team tricode identifier (e.g., 'CHI', 'MIN').

    Returns (pd.DataFrame): A DataFrame with columns 'personId' and
    'personName', containing all unique players for the team.
    """
    raise NotImplementedError("TODO")


def played_for_both(team1: str, team2: str) -> set[str]:
    """
    Returns the names of all players who have played on both specified
    teams.

    Raise a ValueError if either team does not exist.

    Inputs:
        team1 (str): The first tricode team identifier.
        team2 (str): The second tricode team identifier.

    Returns (set[str]): A set of player names of the unique
    individuals who have played on both team1 and team2.
    """
    raise NotImplementedError("TODO")


def top_n_scorers_by_team(team: str, n: int) -> pd.DataFrame:
    """
    Returns the N top scoring players for a given team by each
    player's points per game (PPG) while playing on that team.

    Raise a ValueError if the team does not exist or if n < 1.

    Inputs:
        team (str): The team tricode identifier (e.g., 'CHI', 'MIN').
        n (int): The number of top scorers to return.

    Returns (pd.DataFrame): A DataFrame containing the columns
    'personId', 'personName', and 'ppg', sorted by 'ppg' in descending
    order. Contains at most N rows (or fewer if fewer than n players
    are present).
    """
    raise NotImplementedError("TODO")
