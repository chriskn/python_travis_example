
import pandas as pd
import numpy as np
import os
import xlwt


results = pd.DataFrame([
    ['tom', 10],
    ['nick', 15],
    ['juli', 14],
    ['tom', 3],
    ['nick', 15],
    ['juli', 20],
    ['peter', 20],
    ['peter', 20]
], columns=['Name', 'Points'])


def calculate_leaderboard(data):
    leaderboard = data.groupby(['Name'], as_index=False).sum()
    leaderboard.sort_values('Points', ascending=False, inplace=True)
    leaderboard.index = np.arange(1, len(leaderboard)+1)
    leaderboard.index.name = "Rank"
    return leaderboard


def write_data_frame(data, filepath, sheetname):
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    writer = pd.ExcelWriter(filepath)
    data.to_excel(writer, sheetname)
    writer.save()


if __name__ == '__main__':
    leaderboard = calculate_leaderboard(results)
    output_path = os.path.join("results2","leaderboard.xls")
    write_data_frame(leaderboard, output_path, "Leaderboard")
    print(leaderboard)
