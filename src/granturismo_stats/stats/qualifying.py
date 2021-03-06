"""
Author: Andreas Finkler
Created: 23.12.2020

Statistics for qualifying times.
"""
from operator import attrgetter

import numpy as np

from granturismo_stats.entities.ranking import Leaderboard


class QualifyingTimes:
    """
    Statistics of the qualifying results for a given race.
    """
    def __init__(self, leaderboard: Leaderboard):
        self.leaderboard = leaderboard

    @property
    def scores(self):
        return [entry.score for entry in self.leaderboard]

    @property
    def fastest(self):
        return min(self.leaderboard, key=attrgetter("score"))

    @property
    def slowest(self):
        return max(self.leaderboard, key=attrgetter("score"))

    @property
    def median(self):
        return np.median(self.scores)

    @property
    def mean(self):
        return np.mean(self.scores)

    @property
    def standard_deviation(self):
        return np.std(self.scores)

    def percentile(self, percent):
        return np.percentile(self.scores, percent)
