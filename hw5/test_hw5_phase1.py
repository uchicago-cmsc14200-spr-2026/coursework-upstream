"""
CMSC 14200, Spring 2026
Homework 5, Phase 1 Tests
"""

import pytest
import os
import pandas as pd
import numpy as np

import task1
import task2
import task3


def read_expected(file: str) -> pd.DataFrame:
    return pd.read_csv(f"expected-phase1/{file}.csv").reset_index(drop=True)


## TASK 1:


def test_task1_1() -> None:
    df = task1.get_players_by_partial_name("Homer Simpson")
    assert len(df) == 0


def test_task1_3() -> None:
    df = task1.get_players_by_partial_name("curry").reset_index(drop=True)
    expected = pd.DataFrame(
        {
            "personId": {0: 201939, 1: 203552, 2: 2201},
            "personName": {
                0: "Stephen Curry",
                1: "Seth Curry",
                2: "Eddy Curry",
            },
        }
    )
    cols = ["personId", "personName"]
    pd.testing.assert_frame_equal(df[cols], expected[cols])


def test_task1_6() -> None:
    ppg = task1.get_ppg_by_name("Seth Curry")
    assert pytest.approx(ppg) == np.float64(8.890459363957596)


def test_task1_7() -> None:
    ppg = task1.get_ppg_by_name("Stephen Curry")
    assert pytest.approx(ppg) == np.float64(24.579470198675498)


def test_task1_9() -> None:
    min = task1.total_minutes_played("Seth Curry")
    assert pytest.approx(min) == np.float64(11315.483333333334)


def test_task1_10() -> None:
    min = task1.total_minutes_played("Stephen Curry")
    assert pytest.approx(min) == np.float64(29827.98333333333)


## TASK 2:


def test_task2_2() -> None:
    pf = task2.top_n_scorers_by_team("UTA", 1)
    assert pf is not None  # placate mypy

    pf = pf.reset_index(drop=True)
    expected = read_expected("uta1")
    cols = ["personId", "personName"]
    pd.testing.assert_frame_equal(pf[cols], expected[cols])


def test_task2_3() -> None:
    pf = task2.top_n_scorers_by_team("BOS", 24)
    assert pf is not None  # placate mypy

    pf = pf.reset_index(drop=True)
    expected = read_expected("bos24")
    cols = ["personId", "personName"]
    pd.testing.assert_frame_equal(pf[cols], expected[cols])


def test_task2_5() -> None:
    pf = task2.player_for("MIN")
    assert pf is not None  # to placate mypy

    pf = pf.reset_index(drop=True)
    expected = read_expected("played_for_MIN")
    cols = ["personId", "personName"]
    pd.testing.assert_frame_equal(
        pf[cols].sort_values("personId").reset_index(drop=True),
        expected[cols].sort_values("personId").reset_index(drop=True),
        check_like=True,
    )


def test_task2_6() -> None:
    pf = task2.player_for("SAS")
    assert pf is not None  # to placate mypy

    pf = pf.reset_index(drop=True)
    expected = read_expected("played_for_SAS")
    cols = ["personId", "personName"]
    pd.testing.assert_frame_equal(
        pf[cols].sort_values("personId").reset_index(drop=True),
        expected[cols].sort_values("personId").reset_index(drop=True),
        check_like=True,
    )


def test_task2_8() -> None:
    s = task2.played_for_both("DAL", "MEM")
    expected = {
        "Vince Carter",
        "Brandan Wright",
        "O.J. Mayo",
        "Wayne Ellington",
        "Jae Crowder",
        "Courtney Lee",
        "James Johnson",
        "Chandler Parsons",
        "Justin Holiday",
        "Seth Curry",
        "Delon Wright",
        "Jarrod Uthoff",
        "Tyler Dorsey",
        "Tyrell Terry",
    }
    assert s == expected


## TASK 3:


def test_task3_2() -> None:
    s = task3.played_on_date("2012-12-01")
    expected = read_expected("played_20121201")
    t = set(expected["personName"].values)
    assert s == t
