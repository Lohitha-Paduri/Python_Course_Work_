Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 23:09:28) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> l=[]
>>> l = list()
>>> type(l)
<class 'list'>
>>> l = [1,2,3.7,6+9j,"str",True,[1,2,3],(1,2,3),{1,2,3},{1:2,2:3,4:5}]
>>> l
[1, 2, 3.7, (6+9j), 'str', True, [1, 2, 3], (1, 2, 3), {1, 2, 3}, {1: 2, 2: 3, 4: 5}]
>>> l=[1,1,2,2,3,3]
>>> l
[1, 1, 2, 2, 3, 3]
>>> a = [1,2,3]
>>> b = [4,5,6]
>>> a+b
[1, 2, 3, 4, 5, 6]
>>> a*b
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    a*b
TypeError: can't multiply sequence by non-int of type 'list'
>>> a*3
[1, 2, 3, 1, 2, 3, 1, 2, 3]
>>> a+b*3
[1, 2, 3, 4, 5, 6, 4, 5, 6, 4, 5, 6]
>>> a = [56,45,32,78,234]
>>> a[4]
234
>>> a[3]
78
>>> a[0]
56
>>> a[-1]
234
>>> a[:5]
[56, 45, 32, 78, 234]
>>> a[1:3]
[45, 32]
>>> a[::-1]
[234, 78, 32, 45, 56]
>>> a[1::2]
[45, 78]
>>> a[::2]
[56, 32, 234]
>>> a[-1:-5:2]
[]
>>> a[-1:-4:2]
[]
>>> a[-4:-1:2]
[45, 78]
>>> a[:4:-1]
[]
>>> a[:3:-1]
[234]
>>> a
[56, 45, 32, 78, 234]
>>> a[:4:-1]
[]
>>> 56 in a
True
>>> 2321 in a
False
>>> 1489 not in a
True
>>> 32 not in a
False
>>> a[4::-1]
[234, 78, 32, 45, 56]
>>> a[:4:-2]
[]
>>> a[4::-2]
[234, 32, 56]
>>> l = [45, 56, 43, 769, 4354]
>>> max(l)
4354
>>> min(l)
43
>>> sorted(l)
[43, 45, 56, 769, 4354]
>>> len(l)
5
>>> a
[56, 45, 32, 78, 234]
>>> l
[45, 56, 43, 769, 4354]
>>> id(l)
2359022177800
>>> a[0]
56
>>> a[1]=89
>>> a
[56, 89, 32, 78, 234]
>>> id(a)
2359022176072
>>> l
[45, 56, 43, 769, 4354]
>>> l[1]=89
>>> id(l)
2359022177800
>>> l[-1]= 67
>>> l
[45, 89, 43, 769, 67]
>>> l.append(50)
>>> l.append(60)
>>> l
[45, 89, 43, 769, 67, 50, 60]
>>> a.insert(2,49)
>>> l.insert(2,49)
>>> l
[45, 89, 49, 43, 769, 67, 50, 60]
>>> #in insert first we need to give index and the number we want to add
>>> l.extend([1,2,3,4])
>>> l
[45, 89, 49, 43, 769, 67, 50, 60, 1, 2, 3, 4]
>>> #extend adds multiple numbers at the end, append can add only one number
>>> l.pop()
4
>>> l
[45, 89, 49, 43, 769, 67, 50, 60, 1, 2, 3]
>>> l.pop(4)
769
>>> #in pop() we can give with or without index number
>>> a.remove(43)
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    a.remove(43)
ValueError: list.remove(x): x not in list
>>> l.remove(23)
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    l.remove(23)
ValueError: list.remove(x): x not in list
>>> l.remove(43)
>>> del l[1]
>>> l
[45, 49, 67, 50, 60, 1, 2, 3]
>>> del l[1:3]
>>> l
[45, 50, 60, 1, 2, 3]
>>> l.clear()
>>> l
[]
>>> #remove is used when we know what we want to del
>>> #del can remove elements by index, and also by using slice
>>> #clear removes all the elemets from a list
>>> a = [12,23,34,56,67]
>>> a.index(34)
2
>>> #we can find index using numbers by using index() methids
>>> a
[12, 23, 34, 56, 67]
>>> a.count(34)
1
>>> a = [1,2,3,4]
>>> b=a
>>> b
[1, 2, 3, 4]
>>> b.append(7)
>>> b
[1, 2, 3, 4, 7]
>>> a
[1, 2, 3, 4, 7]
>>> #here both are changing for this we use
>>> c = a.copy()
>>> c.append(8)
>>> c
[1, 2, 3, 4, 7, 8]
>>> b
[1, 2, 3, 4, 7]
>>> a
[1, 2, 3, 4, 7]
>>> any([1,'',False,[],(),{},set()])
True
>>> any([0,'',False,[],(),{},set()])
False
>>> all([1,'',False,[],(),{},set()])
False
>>> all([1,2,3,4])
True
>>> a
[1, 2, 3, 4, 7]
>>> a.reverse()
>>> a
[7, 4, 3, 2, 1]
>>> sum(a)
17
>>> 
