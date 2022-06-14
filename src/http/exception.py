import requests


class BadResponseException(Exception):
    def __init__(self, response: requests.Response):
        self.status_code = response.status_code
        self.message = response.text


class BadRequestException(Exception):
    def __init__(self, response: requests.Response):
        self.status_code = response.status_code
        self.message = response.text
