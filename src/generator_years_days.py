from datetime import date


def years_days(year, month=1, day=1):
    result = (date.fromordinal(_day)
              for _day in range(date.toordinal(date(year, month, day)),
                                date.toordinal(date(year + 1, month, day))))
    return result


dates = years_days(2022)
print(next(dates))
print(next(dates))
print(next(dates))
print(next(dates))
