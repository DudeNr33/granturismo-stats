"""
Author: Andreas Finkler
Created: 12.12.2020
"""

import enum


class SportsMode(enum.IntEnum):
    """
    Enumeration of the different online race events of the sports mode.
    The integer values are the corresponding values used in the web request to the GTSport API.
    """
    DAILY_A = 1
    DAILY_B = 2
    DAILY_C = 3
    NATIONS = 11
    MANUFACTURERS = 12

    @classmethod
    def from_one_line_title(cls, title):
        """Convert the "one line title" attribute to a class instance."""
        title_to_instance = {
            "A": cls.DAILY_A,
            "B": cls.DAILY_B,
            "C": cls.DAILY_C,
            "Manufacturer Series": cls.MANUFACTURERS,
            "Nations Cup": cls.NATIONS,
        }
        return title_to_instance[title]
