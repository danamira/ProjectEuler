# You are given the following information, but you may prefer to do some research for yourself.
#
# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
def getMonths(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                feb = 29
            feb = 28
        else:
            feb = 29
    else:
        feb = 28
    return [31, feb, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def firstDayOfMonth(year, month):
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    step = 0
    if year == 1900 and month == 1:
        return 'Monday'
    else:
        for i in range(1900, year):
            step += sum(getMonths(i))
    m = getMonths(year)[0:month - 1]
    step += sum(m)
    x = (step % 7)
    return days[x]


count = 0
for i in range(1901, 2001):
    for x in range(1, 13):
        if (firstDayOfMonth(i, x) == 'Sunday'):
            count = count + 1
print(count)
