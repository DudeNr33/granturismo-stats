"""
Author: Andreas Finkler
Created: 13.12.2020
"""

from gtsport import api
from gtsport.entities.race import SportsMode


def test_get_leaderboard():
    result = api.get_event_leaderboard(SportsMode.DAILY_B)
    assert len(result.entries) > 0
