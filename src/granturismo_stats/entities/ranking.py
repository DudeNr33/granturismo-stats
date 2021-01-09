"""
Author: Andreas Finkler
Created: 13.12.2020
"""
from dataclasses import dataclass
from typing import List

from granturismo_stats.entities.profile import User
from granturismo_stats.entities.rating import DriverRating, SportsmanshipRating


@dataclass()
class QualifyingResult:
    """Data class for a single entry in the qualification leaderboard."""
    user: User
    score: int  # qualifying time in seconds
    ranking_id: int

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
        return cls(user, score, ranking_id)


@dataclass
class Leaderboard:
    """Data class for a qualification leaderboard."""
    entries: List[QualifyingResult]

    @classmethod
    def from_json(cls, json_data):
        entries = [
            QualifyingResult.from_json(entry)
            for entry in json_data["ranking"]
        ]
        return cls(entries)
