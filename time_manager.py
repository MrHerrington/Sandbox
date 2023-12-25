"""Организатор расписаний (урок по 45 минут, перерыв по 10 минут"""


from datetime import datetime, timedelta


start = datetime.strptime(input(), '%H:%M')
end = datetime.strptime(input(), '%H:%M')
while start + timedelta(minutes=45) <= end:
    print(f'{start.strftime("%H:%M")} - {(start + timedelta(minutes=45)).strftime("%H:%M")}')
    start = start + timedelta(minutes=55)
