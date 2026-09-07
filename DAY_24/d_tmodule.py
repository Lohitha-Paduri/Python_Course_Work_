'''
from datetime import date,time,datetime,timedelta


t = date.today()
print(t)
print(t.day)
print(t.month)
print(t.year)
print(t.weekday())

year,month,day = list(map(int,input('[YYYY-MM-DD]').split("-")))
print(date(year,month,day))

#ACcessing time
tm = time(23,7,24)
print(tm)
print(tm.hour)
print(tm.minute)
print(tm.second)



dt = datetime.now()
print(dt)

print(dt.strftime('%d-%m-%y'))
print(dt.strftime('%d-%m-%Y'))
print(dt.strftime('%d-%m-%Y %H:%M:%S'))
print(dt.strftime('%d-%m-%Y %H:%M:%S %p'))
print(dt.strftime('%d-%m-%Y %I:%M:%S %p'))
print(dt.strftime('%d-%b-%Y %I:%M:%S %p'))
print(dt.strftime('%d-%B-%Y %I:%M:%S %p'))
print(dt.strftime('%a, %d-%B-%Y %I:%M:%S %p'))
print(dt.strftime('%A, %d-%B-%Y, %I:%M:%S %p'))



dt = datetime.now()
t = date.today()

t7 = t + timedelta(days=7)
m15 = dt + timedelta(minutes=15)

print(t7,m15)


from itertools import permutations,combinations
s = 'abc'
print(list(permutations(s,2)))
print(list(combinations(s,2)))

'''
from itertools import permutations,combinations
s = 'abc'

res1 = list(permutations(s,2))
res2 = list(combinations(s,2))

print([''.join(i) for i in res1])
print([''.join(i) for i in res2])