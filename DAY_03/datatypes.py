Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 23:09:28) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Numeric data types
>>> a = 12
>>> type(a)
<class 'int'>
>>> b = 15.6
>>> type(b)
<class 'float'>
>>> c = 12+4j
>>> type(c)
<class 'complex'>
>>> c = 12+4J
>>> c
(12+4j)
>>> #str, list, tuple
>>> s = 'Codegnan'
>>> id(s)
2087113537392
>>> s += 'Python'
>>> s
'CodegnanPython'
>>> id(s)
2087113536688
>>> s = 'aaaaaaaa'
>>> s
'aaaaaaaa'
>>> type(s)
<class 'str'>
>>> l = [1,2,3,4,5,5,6]
>>> type(l)
<class 'list'>
>>> id(l)
2087113864072
>>> l.append(12)
>>> l
[1, 2, 3, 4, 5, 5, 6, 12]
>>> id(l)
2087113864072
>>> l = [1,12.3,"str",[1,23]]
>>> l
[1, 12.3, 'str', [1, 23]]
>>> type(l)
<class 'list'>
>>> t = (1,2,3,4,5)
>>> type(t)
<class 'tuple'>
>>> t = (1,1,1,1)
>>> t
(1, 1, 1, 1)
>>> t = (1,2,3.4,"char")
>>> t
(1, 2, 3.4, 'char')
>>> #set, dict
>>> s = {12, 35, 67, 34, 78, 98, 98, 35}
>>> s
{34, 67, 35, 98, 12, 78}
>>> id(s)
2087113630440
>>> s.add(20)
>>> s
{34, 67, 35, 98, 12, 78, 20}
>>> id(s)
2087113630440
>>> a = {45, 'str', 12.3}
>>> a
{'str', 12.3, 45}
>>> type(s)
<class 'set'>
>>> d = {'Productname':'laptop','price':'54000','stock':'True'}
>>> d
{'Productname': 'laptop', 'price': '54000', 'stock': 'True'}
>>> s = {1,2,3,4}
>>> s = frozenset({1,1,2,3,3,45,67,43})
>>> s
frozenset({1, 2, 67, 3, 43, 45})
>>> a = True
>>> b = False
>>> type(a)
<class 'bool'>
>>> a = {}
>>> b = []
>>> c = ()
>>> s = ''
>>> b = None
>>> type(b)
<class 'NoneType'>
>>> 
