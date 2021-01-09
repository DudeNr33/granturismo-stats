"""
Author: Andreas Finkler
Created: 11.12.2020
"""

from gtsport.entities.race import SportsMode
from gtsport.entities.event import EventDetails, EventCalendar
from gtsport.entities.ranking import Leaderboard
from gtsport.api.event import EventCalendarRequest, EventDetailsRequest
from gtsport.api.ranking import LeaderboardRequest


def get_event_details(sports_mode: SportsMode) -> EventDetails:
    event_id = get_event_id(sports_mode)
    event_details_request = EventDetailsRequest(event_id)
    return event_details_request.execute()


def get_event_id(sports_mode: SportsMode) -> int:
    calendar = get_event_calendar()
    return calendar.races[sports_mode].event_id


def get_event_calendar() -> EventCalendar:
    calendar_request = EventCalendarRequest()
    return calendar_request.execute()


def get_event_leaderboard(sports_mode: SportsMode) -> Leaderboard:
    event_details = get_event_details(sports_mode)
    leaderboard_request = LeaderboardRequest(board_id=event_details.leaderboard_id)
    return leaderboard_request.execute()
