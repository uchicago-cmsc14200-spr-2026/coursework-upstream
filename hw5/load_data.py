"""
CMSC 14200, Spring 2026
Homework 5

Do not modify this file.
"""

import pandas as pd

def load_data() -> dict[str, pd.DataFrame]:
    return {
        'cities': pd.read_csv("data_nba/cities.csv"),
        'players': pd.read_csv("data_nba/players.csv"),
        'teams': pd.read_csv("data_nba/teams.csv"),
        'divisions': pd.read_csv("data_nba/divisions.csv"),
        'games': pd.read_csv("data_nba/games.csv"),
        'box': pd.read_csv("data_nba/box.csv"),
    }
