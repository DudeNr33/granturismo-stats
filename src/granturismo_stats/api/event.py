"""
Author: Andreas Finkler
Created: 11.12.2020
"""

from granturismo_stats.api.base import BaseRequest, JOB
from granturismo_stats.entities.event import EventDetails, EventCalendar
from granturismo_stats.entities.race import SportsMode


EVENT_ID_CSV = "event_id_csv"
CHANNEL_ID_CSV = "channel_id_csv"

JOB_ID_EVENT_DETAILS = 1
JOB_ID_EVENT_CALENDAR = 3


class EventRequest(BaseRequest):
    """
    Base class for /event endpoint.
    """
    URI = "event/"


class EventDetailsRequest(EventRequest):
    """
    Query the details for one or more specific events.
    """
    def __init__(self, event_id):
        """
        :param event_id: ID of the individual race event.
        """
        super(EventDetailsRequest, self).__init__()
        self.form_data[JOB] = JOB_ID_EVENT_DETAILS
        self.form_data[EVENT_ID_CSV] = str(event_id)

    def _convert_response(self, response_data):
        return EventDetails.from_json(response_data)


class EventCalendarRequest(EventRequest):
    """
    Current event calendar request.
    """
    def __init__(self):
        super(EventCalendarRequest, self).__init__()
        self.form_data[JOB] = JOB_ID_EVENT_CALENDAR
        self.form_data[CHANNEL_ID_CSV] = ",".join(str(sports_mode.value) for sports_mode in SportsMode)

    def _convert_response(self, response_data):
        return EventCalendar.from_json(response_data)
