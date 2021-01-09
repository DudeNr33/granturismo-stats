"""
Author: Andreas Finkler
Created: 11.12.2020

This module contains the basic logic for executing a request against the Gran Turismo Sport API.
"""

import requests

BASE_URL = "https://www.gran-turismo.com/de/api/gt7sp/"
JOB = "job"


class BaseRequest:
    """
    Base class for http request handling.
    """
    URI = ""

    def __init__(self):
        self.form_data = {}
        self.result = None

    def execute(self):
        response = self._send_request(self.form_data)
        self.result = self._convert_response(response.json())
        return self.result

    def _send_request(self, form_data):
        response = requests.post(BASE_URL + self.URI, data=form_data)
        response.raise_for_status()
        return response

    def _convert_response(self, response_data):
        raise NotImplementedError()
