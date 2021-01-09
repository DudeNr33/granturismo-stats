"""
Author: Andreas Finkler
Created: 12.12.2020

This module contains integration tests with the real GTSport API and its endpoints.
The tests verify that the requests can be made and the data gets converted.
"""
import pytest

from gtsport import api
from gtsport.entities.race import SportsMode


@pytest.mark.parametrize(
    "mode",
    [
        SportsMode.DAILY_A,
        # SportsMode.DAILY_B,
        # SportsMode.DAILY_C,
        # SportsMode.NATIONS,
        # SportsMode.MANUFACTURERS
    ]
)
def test_get_event_details(mode):
    """
    Query the events/ endpoint for a specific race.
    """
    result = api.get_event_details(mode)
    assert result.sports_mode == mode
