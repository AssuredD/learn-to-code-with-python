# Declare a titanic variable pointing to a date object representing April 14th, 1912
# Declare an independence_day variable pointing to a date object representing July 4th, 1776
# Declare an alarm_clock variable set to a time object representing 05:45:00AM
# Declare a one_second_away variable set to a time object representing 11:59:59PM

from datetime import date, time


titanic = date(year=1912, month=4, day=14)

independence_day = date(year=1776, month=7, day=4)

alarm_clock = time(hour=5, minute=45)

one_second_way = time(hour=23, minute=59, second=59)

print(titanic)
print(alarm_clock)
print(one_second_way)
