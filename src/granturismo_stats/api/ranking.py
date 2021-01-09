"""
Author: Andreas Finkler
Created: 11.12.2020
"""
import os
from copy import copy
from concurrent import futures
from operator import itemgetter

from gtsport.api.base import BaseRequest, JOB
from gtsport.entities.ranking import Leaderboard, QualifyingResult


BOARD_ID = "board_id"
USER_NO = "user_no"
BEGIN = "begin"
END = "end"

JOB_ID_LEADERBOARD = 3
JOB_ID_USER_RANKING = 1

MAX_WORKERS = (os.cpu_count() or 1) * 5
BATCH_SIZE = 1000


class RankingRequest(BaseRequest):
    """Base request for endpoint ranking/"""
    URI = "ranking/"


class UserRankingRequest(RankingRequest):
    """Get the qualifying result for a given user."""
    def __init__(self, board_id, user_no):
        super(UserRankingRequest, self).__init__()
        self.form_data = {
            JOB: JOB_ID_USER_RANKING,
            BOARD_ID: board_id,
            USER_NO: user_no,
        }

    def _convert_response(self, response_data):
        return QualifyingResult.from_json(response_data["ranking"][0])


class LeaderboardRequest(RankingRequest):
    """Get the leaderboard of a specific event"""
    def __init__(self, board_id):
        super(LeaderboardRequest, self).__init__()
        self.form_data = {
            JOB: JOB_ID_LEADERBOARD,
            BOARD_ID: board_id,
        }
        self.result = []

    def execute(self):
        begin = 1
        end = BATCH_SIZE
        with futures.ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
            while True:
                future_list = []
                for _ in range(MAX_WORKERS):
                    future_list.append(executor.submit(self._get_batch, begin, end))
                    begin += BATCH_SIZE
                    end += BATCH_SIZE
                for future in futures.as_completed(future_list):
                    self.result.extend(future.result())
                if len(self.result) < end - BATCH_SIZE:
                    break
        return self._convert_response({"ranking": sorted(self.result, key=itemgetter("score"))})

    def _get_batch(self, begin, end):
        form_data = copy(self.form_data)
        form_data["begin"] = begin
        form_data["end"] = end
        response = self._send_request(form_data)
        return response.json()["ranking"]

    def _convert_response(self, response_data):
        return Leaderboard.from_json(response_data)
