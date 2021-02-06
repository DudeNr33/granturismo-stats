"""
Author: Andreas Finkler
Created: 12.12.2020
"""
import json
from dataclasses import dataclass

from granturismo_stats.entities.race import SportsMode
from granturismo_stats.api import localization


@dataclass
class EventDetails:
    """Detailed information of a single race event."""
    sports_mode: SportsMode
    track: str
    laps: int
    maximum_players: int
    start_type: str
    car_category: list
    leaderboard_id: str
    raw_data: dict = None

    @classmethod
    def from_json(cls, json_data):
        """Construct EventDetails from JSON data received from the web API"""
        event_infos = json_data["event"][0]["value"][0]["GameParameter"]["events"][0]
        track_infos = json_data["event"][0]["value"][0]["GameParameter"]["tracks"][0]
        instance = cls(
            sports_mode=SportsMode.from_one_line_title(event_infos["information"]["one_line_title"]["US"]),
            track=localization.get_track_name_by_course_code(track_infos["course_code"]),
            laps=event_infos["race"]["race_limit_laps"],
            maximum_players=event_infos["race"]["entry_max"],
            start_type=event_infos["race"]["start_type"],
            car_category=event_infos["regulation"]["car_category_types"],
            leaderboard_id=event_infos["ranking"]["board_id"]
        )
        instance.raw_data = json_data
        return instance

    def dump_json(self, filename):
        """Dump the raw json data to a file"""
        if self.raw_data is None:
            raise ValueError("No raw data stored (probably not created from json), cannot dump")
        with open(filename, "w") as outfile:
            json.dump(self.raw_data, outfile)


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
