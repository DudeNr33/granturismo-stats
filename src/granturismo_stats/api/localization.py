"""
Author: Andreas Finkler
Created: 06.02.2021
"""
from functools import lru_cache

import requests

URL_PATTERN = "https://www.gran-turismo.com/{country}/gtsport/module/community/localize"


@lru_cache(maxsize=None)
def get_localization_reference(country="us"):
    response = requests.get(URL_PATTERN.format(country=country))
    return response.json()


def get_track_name_by_course_code(code, country="us"):
    reference = get_localization_reference(country)
    prefix = "gt7sp.game.COMMON.CourseName."
    return reference[prefix + str(code)]
