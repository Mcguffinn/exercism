import unittest
from datetime import datetime
from datetime import timedelta

def add_gigasecond(birth_date):
    gigtime = birth_date + timedelta(seconds=1000000000)

    return gigtime
