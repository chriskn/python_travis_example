#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Calculates a leaderboard from results."""

import os

import numpy as np
import pandas as pd

RESULTS = pd.DataFrame(
    [["tom", 3], ["nick", 5], ["tom", 8]], columns=["Name", "Points"]
)


def calculate(data):
    """
    Calculate leaderboard
    data: Pandas dataframe
        columns: ["Name", "Points"]
    return: leaderboard
        columns: ["Rank", "Name", "Points"]
    """
    board = data.groupby(["Name"], as_index=False).sum()
    board.sort_values("Points", ascending=False, inplace=True)
    board.index = np.arange(1, len(board) + 1)
    board.index.name = "Rank"
    return board


def write(data, folder, filename, sheetname):
    filepath = os.path.join(folder, filename)
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    writer = pd.ExcelWriter(filepath)
    data.to_excel(writer, sheetname)
    writer.save()


if __name__ == "__main__":
    # disable invalid name check
    # pylint: disable = C0103
    leaderboard = calculate(RESULTS)
    write(leaderboard, "results", "leaderboard.xls", "Leaderboard")
    print(leaderboard)
