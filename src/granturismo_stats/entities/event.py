"""
Author: Andreas Finkler
Created: 12.12.2020
"""
from dataclasses import dataclass

from granturismo_stats.entities.race import SportsMode


@dataclass
class EventDetails:
    """Detailed information of a single race event."""
    sports_mode: SportsMode
    leaderboard_id: str

    @classmethod
    def from_json(cls, json_data):
        """Construct an EventCalendar from JSON data received from the web API"""
        event_infos = json_data["event"][0]["value"][0]["GameParameter"]["events"][0]
        return cls(
            sports_mode=SportsMode.from_one_line_title(event_infos["information"]["one_line_title"]["US"]),
            leaderboard_id=event_infos["ranking"]["board_id"]
        )


class EventCalendar:
    """Overview of currently available events"""
    # pylint: disable=too-many-arguments
    def __init__(self, daily_a=None, daily_b=None, daily_c=None, nations=None, manufacturers=None):
        self.races = {
            SportsMode.DAILY_A: daily_a,
            SportsMode.DAILY_B: daily_b,
            SportsMode.DAILY_C: daily_c,
            SportsMode.NATIONS: nations,
            SportsMode.MANUFACTURERS: manufacturers
        }

    @classmethod
    def from_json(cls, json_data):
        """Construct an EventCalendar from JSON data received from the web API"""
        instance = cls()
        for entry in json_data["event_calendar"]:
            sports_mode = SportsMode(int(entry["channel_id"]))
            instance.races[sports_mode] = CalendarEntry(
                sports_mode=sports_mode,
                event_id=entry["event_id"]
            )
        return instance


@dataclass
class CalendarEntry:
    """Single entry in a Event Calendar"""
    event_id: str
    sports_mode: SportsMode
