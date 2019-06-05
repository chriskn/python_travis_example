# -*- coding: utf-8 -*-

import os
import unittest

import pandas as pd

from leaderboard import leaderboard as sut
import pytest


class TestLLoadAndWrite(unittest.TestCase):
    test_data = pd.DataFrame(
        [
            ["tom", 10],
            ["nick", 15],
            ["juli", 14],
            ["tom", 3],
            ["nick", 15],
            ["juli", 20],
            ["peter", 20],
            ["peter", 20],
        ],
        columns=["Name", "Points"],
    )
    expected_leaderboard = pd.DataFrame(
        [[1, "peter", 40], [2, "juli", 34], [3, "nick", 30], [4, "tom", 13]],
        columns=["Rank", "Name", "Points"],
    )

    @pytest.mark.integration
    def test_write_leaderboard(self):
        expected_path = os.path.join("test_results", "leaderboard.xls")
        leaderboard = sut.calculate(self.test_data)

        sut.write(leaderboard, "test_results", "leaderboard.xls", "Leaderboard")

        self.assertTrue(os.path.isfile(expected_path))

    @pytest.mark.integration
    def test_write_and_load_leaderboard(self):
        exp_path = os.path.join("test_results", "leaderboard.xls")
        exp_sheetname = "Leaderboard"
        leaderboard = sut.calculate(self.test_data)
        sut.write(leaderboard, "test_results", "leaderboard.xls", exp_sheetname)

        loaded_leaderboard = pd.ExcelFile(exp_path).parse(exp_sheetname)

        pd.testing.assert_frame_equal(loaded_leaderboard, self.expected_leaderboard)
