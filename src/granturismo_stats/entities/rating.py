"""
Author: Andreas Finkler
Created: 13.12.2020
"""
from enum import Enum, IntEnum


class DriverRating(IntEnum):
    """
    Enumeration of driver ratings. The integer values correspond to the ones used in the GTSport API.
    """
    UNKNOWN = 0
    E = 1
    D = 2
    C = 3
    B = 4
    A = 5
    A_PLUS = 6

    @classmethod
    def from_driver_class(cls, driver_class):
        """Construct a class instance from an integer value."""
        mapping = {
            0: cls.UNKNOWN,
            1: cls.E,
            2: cls.D,
            3: cls.C,
            4: cls.B,
            5: cls.A,
            6: cls.A_PLUS,
        }
        return mapping[int(driver_class)]


class SportsmanshipRating(Enum):
    """
    Enumeration of sportsmanship ratings.
    """
    UNKNOWN = "unknown"
    S = "S"
    A = "A"
    B = "B"
    C = "C"
    D = "D"
    E = "E"

    @classmethod
    def from_manner_points(cls, points):
        """Construct a class instance from an integer value."""
        if points is None:
            return cls.UNKNOWN
        points = int(points)
        if points >= 80:
            return cls.S
        if points >= 65:
            return cls.A
        if points >= 40:
            return cls.B
        if points >= 20:
            return cls.C
        if points >= 10:
            return cls.D
        return cls.E
