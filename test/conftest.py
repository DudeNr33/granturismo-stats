"""
Author: Andreas Finkler
Created: 22.12.2020

Common fixtures to use for tests.
"""
import urllib
from pathlib import Path

import pytest


RESOURCE_DIR = Path(__file__).parent / "resources"
BASE_URL = "https://www.gran-turismo.com/de/api/gt7sp/"

PARAM_JOB = "job"


@pytest.fixture(scope="module", name="resource_dir")
def fixture_resource_dir():
    return RESOURCE_DIR


@pytest.fixture(name="gtsport_api")
def fixture_gtsport_api(requests_mock):
    _setup_event_endpoint(requests_mock)
    _setup_ranking_endpoint(requests_mock)
    _setup_localization_endpoint(requests_mock)
    yield requests_mock


def _setup_event_endpoint(api_mock):
    sample_responses = RESOURCE_DIR / "responses" / "event"

    def callback(request, context):  # pylint: disable=unused-argument
        form_data = _parse_request_body(request.body)
        if form_data[PARAM_JOB] == "1":
            event_id_to_response = {
                "24377": "event_details_daily_a.json",
                "24378": "event_details_daily_b.json",
                "24379": "event_details_daily_c.json",
                "24213": "event_details_nations.json",
                "24160": "event_details_manufacturer.json",
            }
            return (sample_responses / event_id_to_response[form_data["event_id_csv"]]).read_text(encoding="utf-8")
        if form_data[PARAM_JOB] == "3":
            return (sample_responses / "event_calendar.json").read_text(encoding="utf-8")
        return "{}"

    endpoint = "event/"
    api_mock.post(BASE_URL + endpoint, text=callback)


def _setup_ranking_endpoint(api_mock):
    endpoint = "ranking/"
    api_mock.post(BASE_URL + endpoint)


def _setup_localization_endpoint(api_mock):
    localization_file = RESOURCE_DIR / "responses" / "localization" / "localization_us.json"
    api_mock.get(
        "https://www.gran-turismo.com/us/gtsport/module/community/localize",
        text=localization_file.read_text(encoding="utf-8")
    )


def _parse_request_body(body):
    parts = urllib.parse.unquote(body).split("&")
    # pylint: disable=unnecessary-comprehension
    return {
        key: value
        for key, value in [
            part.split("=") for part in parts
        ]
    }
