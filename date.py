import datetime

year, month, day = map(int, input().split())
curDate = datetime.datetime(year, month, day)

days = int(input())
endDate = curDate + datetime.timedelta(days)
print(endDate.strftime('%Y %m %d').replace(' 0', ' '))
