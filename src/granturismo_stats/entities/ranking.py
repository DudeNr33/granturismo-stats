"""
Author: Andreas Finkler
Created: 13.12.2020
"""
from collections import UserList
from csv import DictWriter
from dataclasses import dataclass
from operator import attrgetter
from typing import List

from granturismo_stats.entities.profile import User
from granturismo_stats.entities.rating import DriverRating, SportsmanshipRating


@dataclass()
class QualifyingResult:
    """Data class for a single entry in the qualification leaderboard."""
    user: User
    score: int  # qualifying time in seconds
    ranking_id: int
    _raw_data: dict = None

    @classmethod
    def from_json(cls, json_data):
        user = User(
            name=json_data["user_id"],
            number=json_data["user_no"],
            country=json_data["user_country"],
            driver_rating=DriverRating.from_driver_class(json_data["driver_class"]),
            sportsmanship_rating=SportsmanshipRating.from_manner_points(json_data["manner_point"])
        )
        score = int(json_data["score"])
        ranking_id = int(json_data["ranking_id"])
        instance = cls(user, score, ranking_id)
        instance._raw_data = json_data
        return instance

    def to_json(self):
        return self._raw_data


class Leaderboard(UserList):
    """Data class for a qualification leaderboard."""

    def __init__(self, entries=None):
        super().__init__(initlist=entries)

    @classmethod
    def from_json(cls, json_data):
        entries = [
            QualifyingResult.from_json(entry)
            for entry in json_data["ranking"]
        ]
        entries.sort(key=attrgetter("score"))
        return cls(entries)

    def to_csv(self, filename):
        """
        Save the leaderboard to a CSV file.
        :param filename: Filename or full path to file
        :return: None
        """
        with open(filename, "w", newline="") as outfile:
            writer = DictWriter(
                outfile,
                fieldnames=[
                    "user_id",
                    "user_no",
                    "profile_photo_id",
                    "driver_display_name",
                    "create_time",
                    "board_id",
                    "user_country",
                    "driver_class",
                    "driver_star",
                    "manner_point",
                    "score",
                    "ranking_id",
                    "replay",
                ],
                delimiter=";"
            )
            writer.writeheader()
            for entry in self:
                writer.writerow(entry.to_json())
