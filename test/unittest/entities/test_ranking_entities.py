"""
Author: Andreas Finkler
Created: 22.12.2020
"""
import pytest

from granturismo_stats.entities.rating import DriverRating, SportsmanshipRating
from granturismo_stats.entities.profile import User
from granturismo_stats.entities.ranking import Leaderboard, QualifyingResult


@pytest.fixture(name="example_leaderboard")
def fixture_example_leaderboard():
    return Leaderboard(
        entries=[
            QualifyingResult(
                user=User(
                    name="User1",
                    number=1,
                    country="de",
                    driver_rating=DriverRating.A,
                    sportsmanship_rating=SportsmanshipRating.S,
                ),
                score=1234,
                ranking_id=1,
            ),
            QualifyingResult(
                user=User(
                    name="User2",
                    number=2,
                    country="de",
                    driver_rating=DriverRating.B,
                    sportsmanship_rating=SportsmanshipRating.A,
                ),
                score=5678,
                ranking_id=2,
            ),
            QualifyingResult(
                user=User(
                    name="User3",
                    number=3,
                    country="de",
                    driver_rating=DriverRating.C,
                    sportsmanship_rating=SportsmanshipRating.B,
                ),
                score=4711,
                ranking_id=3,
            )
        ]
    )


def test_to_csv(tmpdir, example_leaderboard):
    filename = tmpdir / "example_leaderboard.csv"
    example_leaderboard.to_csv(filename=filename)
    content = filename.read_text(encoding="utf-8")
    assert content == "name;number;country;driver_rating;sportsmanship_rating;score;ranking_id\n" \
                      "User1;1;de;5;S;1234;1\n" \
                      "User2;2;de;4;A;5678;2\n" \
                      "User3;3;de;3;B;4711;3\n"
