Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 23:09:28) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #TUPLES
>>> t = ()
>>> t = tuple()
>>> t = (1,2,45)
>>> t
(1, 2, 45)
>>> t = (1)
>>> t
1
>>> #the number is not considering as tuple, it is getting as integer
>>> t = (1,)
>>> t
(1,)
>>> t = (1,1,1,1)
>>> t
(1, 1, 1, 1)
>>> t = (1,12.3,"str",[1,2,3],{1,2,3},{1:2,2:3,3:4})
>>> t
(1, 12.3, 'str', [1, 2, 3], {1, 2, 3}, {1: 2, 2: 3, 3: 4})
>>> #homeogenous can contain multiple datatypes init
>>> type(t)
<class 'tuple'>
>>> #same operators as str,list
>>> (1,2,3)+(3,4,5)
(1, 2, 3, 3, 4, 5)
>>> (1,2,3)*4
(1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3)
>>> t = (1,12.3,"str",[1,2,3],{1,2,3},{1:2,2:3,3:4},True)
>>> t[0]
1
>>> t[5]
{1: 2, 2: 3, 3: 4}
>>> t[3:7]
([1, 2, 3], {1, 2, 3}, {1: 2, 2: 3, 3: 4}, True)
>>> t[-1]
True
>>> t[::-1]
(True, {1: 2, 2: 3, 3: 4}, {1, 2, 3}, [1, 2, 3], 'str', 12.3, 1)
>>> t[:3]
(1, 12.3, 'str')
>>> t[-5:-2]
('str', [1, 2, 3], {1, 2, 3})
>>> 'str' in t
True
>>> 2 not in t
True
>>> 3 in t
False
>>> #tuple is immutable we dont have append,insert, extend
>>> t = (12, 35, 45, 7788, 322, 23, 45, 7456, 45, 989, 45)
>>> sorted(t)
[12, 23, 35, 45, 45, 45, 45, 322, 989, 7456, 7788]
>>> min(t)
12
>>> max(t)
7788
>>> len(t)
11
>>> t
(12, 35, 45, 7788, 322, 23, 45, 7456, 45, 989, 45)
>>> t.index(7788)
3
>>> t.count(45)
4
>>> all((1,2,3))
True
>>> all((1,2,3,00,0))
False
>>> any((1,2,3,00,0))
True
>>> t = 1,2,3
>>> t
(1, 2, 3)
>>> a,b,c = t
>>> a
1
>>> b
2
>>> c
3
>>> t = (1,2,3,[1,2,3],5)
>>> t
(1, 2, 3, [1, 2, 3], 5)
>>> t[4]
5
>>> t[3].append(4)
>>> t
(1, 2, 3, [1, 2, 3, 4], 5)
>>> #here the list gets added, when there is a list inside a tuple then we can do chnages on list.
>>> t = (1,2,3,4,5)
>>> sumt(t)
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    sumt(t)
NameError: name 'sumt' is not defined
>>> sum(t)
15
>>> s = {}
>>> type(s)
<class 'dict'>
>>> s = set()
>>> type(s)
<class 'set'>
>>> #set
>>> s = {1,2,3,4,5,6,7}
>>> s
{1, 2, 3, 4, 5, 6, 7}
>>> s = {1,2,3,4,5,6,234,657,243534,8967,43}
>>> s
{1, 2, 3, 4, 5, 6, 8967, 234, 43, 243534, 657}
>>> s = {1,1,1,1,1}
>>> s
{1}
>>> #set is unordered and do not allows duplicates
>>> s = set()
>>> s.add(1)
>>> a.add(12.3)
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    a.add(12.3)
AttributeError: 'int' object has no attribute 'add'
>>> s.add(15.5)
>>> s.add("str")
>>> s.add([1,2,3])
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    s.add([1,2,3])
TypeError: unhashable type: 'list'
>>> s.add((1,2,3))
>>> s.add({1,2,3})
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    s.add({1,2,3})
TypeError: unhashable type: 'set'
>>> 
>>> #in set we can add immutable elements but not mutable elements.
>>> s.add(True)
>>> s
{1, 'str', (1, 2, 3), 15.5}
>>> s.add(True)
>>> s
{1, 'str', (1, 2, 3), 15.5}
>>> s.add(False)
>>> s
{False, 1, (1, 2, 3), 15.5, 'str'}
>>> #set operations do not have concatenation, repetition, indexing, slicing
>>> a = {1,2,3,4,5}
>>> b = {3,4,5,6,7}
>>> 2 in a
True
>>> 10 not in a
True
>>> a | b
{1, 2, 3, 4, 5, 6, 7}
>>> a & b
{3, 4, 5}
>>> a - b
{1, 2}
>>> b - a
{6, 7}
>>> a ^ b
{1, 2, 6, 7}
>>> #set has union(|), intersection(&), difference(-), symmetrical difference(^)
>>> a
{1, 2, 3, 4, 5}
>>> {1}<=a
True
>>> #to check subset we need to use <=
>>> #for superset >=
>>> a
{1, 2, 3, 4, 5}
>>> {1,2,3}<=a
True
>>> {12,34}<=a
False
>>> {4,5,6}>=a
False
>>> {4,5}>=a
False
>>> {1,2,3}>=a
False
>>> (1,2,3,4,5}>=a
SyntaxError: invalid syntax
>>> {1,2,3,4,5}>=a
True
>>> {1,2,3,4,5,6)>=a
SyntaxError: invalid syntax
>>> {1,2,3,4,5,6}>=a
True
>>> m = {1,2,3}
>>> n = {3,4,5}
>>> n.isdisjoint(m)
False
>>> n = {5,6,7}
>>> n.isdisjoint(m)
True
>>> #disjoint checks whether two sets have no common elements
>>> a = {1, 34, 465, 75, 2, 45}
>>> a.count(1)
Traceback (most recent call last):
  File "<pyshell#117>", line 1, in <module>
    a.count(1)
AttributeError: 'set' object has no attribute 'count'
>>> 
>>> 
>>> #set do not have count because it only contains unique elements
>>> all({12, 34, 45, 56})
True
>>> any({0,''})
False
>>> any({0,'',(),True})
True
>>> a
{1, 2, 34, 75, 45, 465}
>>> sum(a)
622
>>> a = {1,2,3}
>>> b = a
>>> b.add(4)
>>> a
{1, 2, 3, 4}
>>> b
{1, 2, 3, 4}
>>> c = a.copy()
>>> a
{1, 2, 3, 4}
>>> c
{1, 2, 3, 4}
>>> c.add(5)
>>> c
{1, 2, 3, 4, 5}
>>> a
{1, 2, 3, 4}
>>> a = {123,431,1,3,45}
>>> sorted(a)
[1, 3, 45, 123, 431]
>>> max(a)
431
>>> min(a)
1
>>> len(a)
5
>>> a.add(5)
>>> a
{1, 3, 5, 45, 431, 123}
>>> a.add(100)
>>> a
{1, 3, 100, 5, 45, 431, 123}
>>> a.update({99,67,43,2,})
>>> a
{1, 2, 3, 100, 5, 67, 99, 43, 45, 431, 123}
>>> a.pop()
1
>>> a
{2, 3, 100, 5, 67, 99, 43, 45, 431, 123}
>>> a.pop()
2
>>> a
{3, 100, 5, 67, 99, 43, 45, 431, 123}
>>> a.pop()
3
>>> a.remove(67)
>>> a.remove(431)
>>> a
{100, 5, 99, 43, 45, 123}
>>> a.remove(5)
>>> a
{100, 99, 43, 45, 123}
>>> a.remove(5)
Traceback (most recent call last):
  File "<pyshell#158>", line 1, in <module>
    a.remove(5)
KeyError: 5
>>> a
{100, 99, 43, 45, 123}
>>> a.discard(99)
>>> a
{100, 43, 45, 123}
>>> a.discard(99)
>>> a
{100, 43, 45, 123}
>>> a.clear()
>>> a
set()
>>> a = frozenset({1,2,3,4})
>>> a
frozenset({1, 2, 3, 4})
>>> 
