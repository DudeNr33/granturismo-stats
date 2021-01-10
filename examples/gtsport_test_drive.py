"""
Author: Andreas Finkler
Created: 06.01.2021
"""
import shelve
import time
from copy import deepcopy

from granturismo_stats import api
from granturismo_stats.stats.qualifying import QualifyingTimes
from granturismo_stats.entities.rating import DriverRating, SportsmanshipRating

# TODOS:
# leaderboard: filter
# leaderboard: find_by_name
# QualifyingResult and Stats: score as mm:ss.millis
# leaderboard: cache on disk


def get_leaderboard(sports_mode):
    with shelve.open("leaderboard_cache") as db:
        current_time = time.time()
        last_read_time = db.get(f"last_read_{sports_mode}", 0)
        if current_time - last_read_time > 3600:
            # if entry is older than one hour, renew the entry
            db[f"leaderboard_{sports_mode}"] = api.get_event_leaderboard(sports_mode)
            db[f"last_read_{sports_mode}"] = time.time()
        return db[f"leaderboard_{sports_mode}"]


for sports_mode in (api.SportsMode.DAILY_A, api.SportsMode.DAILY_B, api.SportsMode.DAILY_C):

    print("------", sports_mode, "------\n")
    leaderboard = get_leaderboard(sports_mode)
    for entry in leaderboard.entries:
        if entry.user.name == "dudenr33":
            print(f"Your time: {entry.score}s")
            break
    else:
        print("You have not set a time yet.")
    qualifying_times = QualifyingTimes(deepcopy(leaderboard))
    print(f"Entries: {len(qualifying_times.leaderboard.entries):>10}")
    print(f"Best:    {qualifying_times.fastest.score:>10}s")
    print(f"Mean:    {qualifying_times.mean:>10.1f}s")
    print(f"Median:  {qualifying_times.median:>10.1f}s")

    print("\nRestricted to Driver Rating B and Sportsmanship Rating S:")
    qualifying_times.leaderboard.entries = [
        entry
        for entry in qualifying_times.leaderboard.entries
        if entry.user.driver_rating is DriverRating.B
        and entry.user.sportsmanship_rating is SportsmanshipRating.S
    ]
    print(f"Entries: {len(qualifying_times.leaderboard.entries):>10}")
    print(f"Best:    {qualifying_times.fastest.score:>10}s")
    print(f"Mean:    {qualifying_times.mean:>10.1f}s")
    print(f"Median:  {qualifying_times.median:>10.1f}s")

    print("\n\n")
