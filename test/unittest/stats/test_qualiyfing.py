"""
Author: Andreas Finkler
Created: 23.12.2020
"""
import json

import pytest
import numpy as np

from granturismo_stats.entities.ranking import Leaderboard, QualifyingResult
from granturismo_stats.stats.qualifying import QualifyingTimes


@pytest.fixture(scope="module", name="raw_data")
def fixture_raw_data(resource_dir):
    json_file = resource_dir / "responses" / "ranking" / "leaderboard_batch_1-1000.json"
    return json.loads(json_file.read_text(encoding="utf-8"))


@pytest.fixture(scope="module", name="leaderboard")
def fixture_leaderboard(raw_data):
    return Leaderboard.from_json(raw_data)


@pytest.fixture(scope="function", name="qualifying_times")
def fixture_qualifying_times(leaderboard):
    return QualifyingTimes(leaderboard)


def test_fastest(raw_data, qualifying_times):
    """
    It must be possible to get the fastest qualifying result.
    """
    assert qualifying_times.fastest == QualifyingResult.from_json(raw_data["ranking"][0])


def test_slowest(raw_data, qualifying_times):
    """
    It must be possible to get the slowest qualifying result.
    """
    assert qualifying_times.slowest == QualifyingResult.from_json(raw_data["ranking"][-1])


def test_median(raw_data, qualifying_times):
    """
    It must be possible to get the median time of the qualifying results.
    """
    assert qualifying_times.median == np.median(
        [int(entry["score"]) for entry in raw_data["ranking"]]
    )


def test_mean(raw_data, qualifying_times):
    """
    It must be possible to get the mean time of the qualifying results.
    """
    assert qualifying_times.mean == np.mean(
        [int(entry["score"]) for entry in raw_data["ranking"]]
    )


@pytest.mark.parametrize("percentile", [5, 10, 50])
def test_percentile(raw_data, qualifying_times, percentile):
    """
    It must be possible to get percentiles from the qualifying results.
    """
    assert qualifying_times.percentile(percentile) == np.percentile(qualifying_times.scores, percentile)


def test_50th_percentile_equals_median(qualifying_times):
    """
    The 50th percentile is the same as the median.
    """
    assert qualifying_times.percentile(50) == qualifying_times.median
