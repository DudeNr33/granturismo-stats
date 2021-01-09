"""
Author: Andreas Finkler
Created: 13.12.2020
"""
from enum import Enum, IntEnum


class DriverRating(IntEnum):
    E = 1
    D = 2
    C = 3
    B = 4
    A = 5
    A_PLUS = 6

    @classmethod
    def from_driver_class(cls, driver_class):
        mapping = {
            1: cls.E,
            2: cls.D,
            3: cls.C,
            4: cls.B,
            5: cls.A,
            6: cls.A_PLUS,
        }
        return mapping[int(driver_class)]


class SportsmanshipRating(Enum):
    S = "S"
    A = "A"
    B = "B"
    C = "C"
    D = "D"
    E = "E"

    @classmethod
    def from_manner_points(cls, points):
        points = int(points)
        if points >= 80:
            return cls.S
        elif points >= 65:
            return cls.A
        elif points >= 40:
            return cls.B
        elif points >= 20:
            return cls.C
        elif points >= 10:
            return cls.D
        else:
            return cls.E
