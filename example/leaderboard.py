#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import os
import xlwt


results = pd.DataFrame([
    ['tom', 3],
    ['nick', 5],
    ['juli', 19],
    ['tom', 8],
    ['peter', 20]
], columns=['Name', 'Points'])


def calculate_leaderboard(data):
    leaderboard = data.groupby(['Name'], as_index=False).sum()
    leaderboard.sort_values('Points', ascending=False, inplace=True)
    leaderboard.index = np.arange(1, len(leaderboard)+1)
    leaderboard.index.name = "Rank"
    return leaderboard


def write_leaderboard(data, filepath, sheetname):
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    writer = pd.ExcelWriter(filepath)
    data.to_excel(writer, sheetname)
    writer.save()


if __name__ == '__main__':
    leaderboard = calculate_leaderboard(results)
    output_path = os.path.join("results","leaderboard.xls")
    write_leaderboard(leaderboard, output_path, "Leaderboard")
    print(leaderboard)
