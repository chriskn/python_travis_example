#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Dummy Class."""

import os

import numpy as np
import pandas as pd

RESULTS = pd.DataFrame([
    ['tom', 3],
    ['nick', 5],
    ['juli', 19],
    ['tom', 8],
], columns=['Name', 'Points'])


def calculate_leaderboard(data):
    """Caluclates Leaderboard"""
    board = data.groupby(['Name'], as_index=False).sum()
    board.sort_values('Points', ascending=False, inplace=True)
    board.index = np.arange(1, len(board)+1)
    board.index.name = "Rank"
    return board


def write_leaderboard(data, filepath, sheetname):
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    writer = pd.ExcelWriter(filepath)
    data.to_excel(writer, sheetname)
    writer.save()


if __name__ == '__main__':
    # disable invalid name check
    # pylint: disable = C0103
    leaderboard = calculate_leaderboard(RESULTS)
    output_path = os.path.join("results", "leaderboard.xls")
    write_leaderboard(leaderboard, output_path, "Leaderboard")
    print(leaderboard)
