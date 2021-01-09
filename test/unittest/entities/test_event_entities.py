"""
Author: Andreas Finkler
Created: 22.12.2020
"""
import json

import pytest

from granturismo_stats.entities.event import EventDetails, EventCalendar
from granturismo_stats.entities.race import SportsMode


@pytest.mark.parametrize(
    "data,attribute,expected_value",
    [
        ("event_details_daily_a.json", "leaderboard_id", 1030437),
        ("event_details_daily_a.json", "sports_mode", SportsMode.DAILY_A),
        ("event_details_daily_b.json", "leaderboard_id", 1030438),
        ("event_details_daily_b.json", "sports_mode", SportsMode.DAILY_B),
        ("event_details_daily_c.json", "leaderboard_id", 1030439),
        ("event_details_daily_c.json", "sports_mode", SportsMode.DAILY_C),
        ("event_details_manufacturer.json", "leaderboard_id", 1008358),
        ("event_details_manufacturer.json", "sports_mode", SportsMode.MANUFACTURERS),
        ("event_details_nations.json", "leaderboard_id", 1008367),
        ("event_details_nations.json", "sports_mode", SportsMode.NATIONS),
    ]
)
def test_event_details_from_json(resource_dir, data, attribute, expected_value):
    """
    An EventDetails entity can be created from the JSON data provided by the web api.
    """
    json_data = json.loads((resource_dir / "responses" / "event" / data).read_text(encoding="utf-8"))
    event_details = EventDetails.from_json(json_data)
    assert getattr(event_details, attribute) == expected_value


@pytest.mark.parametrize(
    "race,expected_event_id",
    [
        (SportsMode.DAILY_A, "24377"),
        (SportsMode.DAILY_B, "24378"),
        (SportsMode.DAILY_C, "24379"),
        (SportsMode.MANUFACTURERS, "24160"),
        (SportsMode.NATIONS, "24213"),
    ]
)
def test_event_calendar_from_json(resource_dir, race, expected_event_id):
    """
    An EventCalendar entity can be created from the JSON data provided by the web api.
    """
    json_data = json.loads((resource_dir / "responses" / "event" / "event_calendar.json").read_text(encoding="utf-8"))
    event_calendar = EventCalendar.from_json(json_data)
    assert event_calendar.races[race].event_id == expected_event_id
