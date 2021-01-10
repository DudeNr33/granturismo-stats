"""
Author: Andreas Finkler
Created: 13.12.2020
"""
from csv import DictWriter
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

    def to_json(self):
        return {
            "name": self.user.name,
            "number": self.user.number,
            "country": self.user.country,
            "driver_rating": self.user.driver_rating.value,
            "sportsmanship_rating": self.user.sportsmanship_rating.value,
            "score": self.score,
            "ranking_id": self.ranking_id,
        }


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
                    "name",
                    "number",
                    "country",
                    "driver_rating",
                    "sportsmanship_rating",
                    "score",
                    "ranking_id",
                ],
                delimiter=";"
            )
            writer.writeheader()
            for entry in self.entries:
                writer.writerow(entry.to_json())
