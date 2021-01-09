"""
Author: Andreas Finkler
Created: 13.12.2020
"""
from dataclasses import dataclass

from granturismo_stats.entities.rating import DriverRating, SportsmanshipRating


@dataclass
class User:
    name: str
    number: int
    country: str
    driver_rating: DriverRating
    sportsmanship_rating: SportsmanshipRating
