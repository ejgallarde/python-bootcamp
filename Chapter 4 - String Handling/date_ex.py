#! /usr/bin/env python3
# Name:        unicode.py
# Author:      Earl John Gallarde
# Revision:    v1.0
# Description: Example of working with Dates and Times.
"""
    DocString: Example of working with Dates and Times.
"""

import datetime

# ISO 8601 standard most significant-> least significant.
# YYY-MM-DD HH:MM:SS (rather than US Vs Euro format)

d1 = datetime.date(year=2023, month=3, day=22)
d2 = datetime.time(hour=7, minute=7, second=23)
d3 = datetime.datetime(year=2023, month=3, day=22, hour=7, minute=7, second=23)

print(d1)
print(d2)
print(d3)

print(f"Today is {datetime.date.today()}")
print(f"Now is {datetime.datetime.now()}")

# If you want to work with Timezones then install python-dateutil
