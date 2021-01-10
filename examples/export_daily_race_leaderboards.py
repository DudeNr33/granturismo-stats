"""
Author: Andreas Finkler
Created: 10.01.2021
"""
from datetime import datetime

from granturismo_stats import api


week_number = datetime.now().isocalendar()[1]

for mode in (api.SportsMode.DAILY_A, api.SportsMode.DAILY_B, api.SportsMode.DAILY_C):
    event_details = api.get_event_details(mode)
    with open(f"event_details_daily{mode.value}_week{week_number}.txt", "w") as outfile:
        outfile.writelines(
            [
                f"Mode: Daily Race {event_details.sports_mode.value}",
                f"Leaderboard ID: {event_details.leaderboard_id}",
            ]
        )
    leaderboard = api.get_event_leaderboard(mode)
    filename = f"leaderboard_daily{mode.value}_week{week_number}.csv"
    leaderboard.to_csv(filename)
