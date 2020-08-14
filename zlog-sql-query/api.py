#! /usr/bin/env python3
from datetime import datetime
from json import dumps
from typing import Union
import auth

import requests


def query(
        nicks: Union[list, str],
        window: str,
        date_start: datetime,
        date_end: datetime
):
    url = auth.url
    headers = {
        'auth': auth.api_key
    }
    payload = {
        'multipleNicks': "False" if type(nicks) is str else "True",
        'nick':          dumps(nicks) if type(nicks) is list else nicks,
        'window':        window,
        'date-start':    date_start,
        'date-end':      date_end
    }
    return requests.request("GET", url, headers=headers, data=payload)
