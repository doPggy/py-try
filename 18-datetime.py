# datetime 模块
import datetime as dt

## date 对象
d1 = dt.date(2007, 9, 25)
d2 = dt.date(2008, 9, 25)
print(d1)
print(d1.strftime('%A, %m/%d/%y'))
print(d1.strftime('%a, %m-%d-%y'))
print(d2 - d1)
'''timedelta 对象'''
print(type(d2 - d1))
print(dt.date.today())

## time 对象
t1 = dt.time(15, 38, 22, 1)
t2 = dt.time(18)
print(t1)
print(t1.strftime('%I:%M, %p'))
print(t1.strftime('%H:%M:%S, %p'))

## datetime 对象
d = dt.datetime(2020, 1, 1)
print(d)
d1 = dt.datetime.now()
print(d1)
d2 = d1 + dt.timedelta(30)
print(d2)
print(dt.datetime.strptime('2/10/01', '%m/%d/%y'))