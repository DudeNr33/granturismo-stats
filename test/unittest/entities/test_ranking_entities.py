"""
Author: Andreas Finkler
Created: 22.12.2020
"""
import pytest

from granturismo_stats.entities.ranking import Leaderboard, QualifyingResult


@pytest.fixture(name="example_json_data")
def fixture_example_json_data():
    return {
        "ranking": [
            {
                "user_id":      "User1",
                "user_no":      1,
                "user_country": "de",
                "driver_class": 5,
                "manner_point": 99,
                "score":        1234,
                "ranking_id":   1,
            },
            {
                "user_id":      "User2",
                "user_no":      2,
                "user_country": "de",
                "driver_class": 4,
                "manner_point": 79,
                "score":        5678,
                "ranking_id":   2,
            },
            {
                "user_id":      "User3",
                "user_no":      3,
                "user_country": "de",
                "driver_class": 3,
                "manner_point": 64,
                "score":        4714,
                "ranking_id":   3,
            }
        ]
    }


@pytest.fixture(name="example_leaderboard")
def fixture_example_leaderboard(example_json_data):
    return Leaderboard.from_json(example_json_data)


def test_from_json(example_json_data):
    leaderboard = Leaderboard.from_json(example_json_data)
    assert len(leaderboard.entries) == 3
    assert all(isinstance(entry, QualifyingResult) for entry in leaderboard.entries)


def test_to_csv(tmpdir, example_leaderboard):
    filename = tmpdir / "example_leaderboard.csv"
    example_leaderboard.to_csv(filename=filename)
    content = filename.read_text(encoding="utf-8")
    assert content == "user_id;user_no;profile_photo_id;driver_display_name;create_time;board_id;user_country;" \
                      "driver_class;driver_star;manner_point;score;ranking_id;replay\n" \
                      "User1;1;;;;;de;5;;99;1234;1;\n" \
                      "User3;3;;;;;de;3;;64;4714;3;\n" \
                      "User2;2;;;;;de;4;;79;5678;2;\n"
