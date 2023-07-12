#! /usr/bin/env python3
# Name:         breakfast.py
# Author:       Earl John Gallarde
# Version:      1.0
# Description:  This exercise carries out some basic operations on variables.

"""
    This exercise carries out some basic operations on variables.

     If I leave my house at 6:52 am and run 1 mile at an easy pace (8:15 per mile), then 3 miles at
    tempo (7:12 per mile) and 1 mile at easy pace again, what time do I get home for breakfast?
"""
import math

time_running_1 = (8*60 + 15)  # in seconds
print('1st pace', time_running_1)

time_running_2 = 3*(7*60 + 12)
print('2nd pace', time_running_2)

time_running_3 = (8*60 + 15)
print('3rd pace', time_running_3)

total_run_time_in_seconds = time_running_3 + time_running_2 + time_running_1
print('Total run time in seconds:', total_run_time_in_seconds)

total_run_time_in_mins = total_run_time_in_seconds // 60
print('Total run time in mins:', total_run_time_in_mins)

excess_seconds = total_run_time_in_seconds - total_run_time_in_mins * 60
print('Excess in seconds:', excess_seconds)

hours_to_be_added = (52 + total_run_time_in_mins) // 60
print('Hours added:', hours_to_be_added)

excess_minutes = abs(total_run_time_in_mins - hours_to_be_added * 60)
print('Excess mins:', excess_minutes)

# TODO: needs fixing
print('Time arrived at home:')
