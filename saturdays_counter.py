from datetime import *


def saturdays_between_two_dates(one, two):
    count = 0
    if one > two:
        one, two = two, one
    while one.toordinal() <= two.toordinal():
        if one.fromordinal(one.toordinal()).isoweekday() == 6:
            count += 1
        one = one.fromordinal(one.toordinal() + 1)
    return count


date1 = date(2021, 11, 1)
date2 = date(2021, 11, 22)
print(saturdays_between_two_dates(date1, date2))
