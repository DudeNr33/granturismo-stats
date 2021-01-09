"""
Author: Andreas Finkler
Created: 11.12.2020
"""

from granturismo_stats.api import event
from granturismo_stats.entities.event import EventCalendar, EventDetails


def test_event_calendar_request(gtsport_api):
    """
    When the request can be executed successfully, an EventCalendar entity must be returned.
    """
    result = event.EventCalendarRequest().execute()
    assert isinstance(result, EventCalendar)


def test_event_details_request(gtsport_api):
    """
    When the request can be executed successfully, an EventCalendar entity must be returned.
    """
    result = event.EventDetailsRequest(event_id="24377").execute()
    assert isinstance(result, EventDetails)


def test_event_details_passes_correct_form_data(gtsport_api):
    """
    An EventDetailsRequest must pass the event id in the request.
    """
    event_id = 24377
    _ = event.EventDetailsRequest(event_id=event_id).execute()
    assert "job=1&event_id_csv={}".format(event_id) == gtsport_api.last_request.text
