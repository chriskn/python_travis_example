#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

import pandas as pd

from example import leaderboard


class TestLeaderboard(unittest.TestCase):

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

    def test_leaderboard_groups_by_name(self):
        result = leaderboard.calculate_leaderboard(self.test_data)
        self.assertEqual(set(result["Name"]), set(["tom", "nick", "juli", "peter"]))

    def test_leaderboard_sums_up_by_name(self):
        result = leaderboard.calculate_leaderboard(self.test_data)
        self.assertEqual(set(result["Points"]), set([13, 34, 40, 30]))

    def test_leaderboard_is_sorted_by_points(self):
        result = leaderboard.calculate_leaderboard(self.test_data)
        self.assertEqual(list(result["Name"]), ["peter", "juli", "nick", "tom"])
        self.assertEqual(list(result["Points"]), [40, 34, 30, 13])
