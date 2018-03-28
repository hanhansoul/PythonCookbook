"""
class A:
    def __init__(self):
        print("A")


class B:
    def __init__(self):
        print("B")


class C(A, B):
    def __init__(self):
        super(C, self).__init__()
        super(A, self).__init__()
        print("C")


c = C()
"""

"""
datetime.date
year / month / day

datetime.time
hour / minute / second / microsecond / tzinfo

datetime.datetime
date + time

datetime.timedelta

"""

from datetime import datetime
from datetime import timedelta
from datetime import date

delta = timedelta(days=10, hours=20, minutes=15, seconds=30)
year = timedelta(days=365)
another_year = timedelta(weeks=40, days=84, hours=23, minutes=50, seconds=600)
ten_years = 10 * year
print(ten_years, ten_years.days)

"""
datetime.date
date(year, month, day)
date.today()

"""
today = date.today()
today.timetuple()

today.strftime("%d/%m/%Y")