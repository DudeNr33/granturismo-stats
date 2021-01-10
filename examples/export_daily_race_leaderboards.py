"""
Author: Andreas Finkler
Created: 10.01.2021
"""
from datetime import datetime

from granturismo_stats import api


week_number = datetime.now().isocalendar()[1]

for mode in (api.SportsMode.DAILY_A, api.SportsMode.DAILY_B, api.SportsMode.DAILY_C):
    event_details = api.get_event_details(mode)
    event_details.dump_json(f"event_details_daily{mode.value}_week{week_number}.json")
    #leaderboard = api.get_event_leaderboard(mode)
    #leaderboard.to_csv(f"leaderboard_daily{mode.value}_week{week_number}.csv")
