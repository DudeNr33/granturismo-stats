"""
Author: Andreas Finkler
Created: 22.12.2020
"""
import pytest

from gtsport.entities.rating import DriverRating, SportsmanshipRating


@pytest.mark.parametrize(
    "driver_class,expected_driver_rating",
    [
        ("1", DriverRating.E),
        ("2", DriverRating.D),
        ("3", DriverRating.C),
        ("4", DriverRating.B),
        ("5", DriverRating.A),
        ("6", DriverRating.A_PLUS),
    ]
)
def test_driver_rating_from_driver_class(driver_class, expected_driver_rating):
    """
    It must be possible to construct the DriverRating from the integer value "driver_class" provided by various
    endpoints.
    """
    assert DriverRating.from_driver_class(driver_class) == expected_driver_rating


@pytest.mark.parametrize(
    "manner_points,expected_sportsmanship_rating",
    [
        ("99", SportsmanshipRating.S),
        ("80", SportsmanshipRating.S),
        ("79", SportsmanshipRating.A),
        ("65", SportsmanshipRating.A),
        ("64", SportsmanshipRating.B),
        ("40", SportsmanshipRating.B),
        ("39", SportsmanshipRating.C),
        ("20", SportsmanshipRating.C),
        ("19", SportsmanshipRating.D),
        ("10", SportsmanshipRating.D),
        ("9", SportsmanshipRating.E),
        ("1", SportsmanshipRating.E),
    ]
)
def test_sportsmanship_rating_from_manner_points(manner_points, expected_sportsmanship_rating):
    """
    It must be possible to construct the SportsmanshipRating from the integer value "manner points" provided by various
    endpoints.
    """
    assert SportsmanshipRating.from_manner_points(manner_points) == expected_sportsmanship_rating
