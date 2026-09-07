Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 23:09:28) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = 10
>>> float(a)
10.0
>>> str(a)
'10'
>>> complex(a)
(10+0j)
>>> bool(a)
True
>>> list(a)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    list(a)
TypeError: 'int' object is not iterable
>>> #cannot convert int into list, tuple,set, dictionary because they contain collection of elements
>>> f = 13.4
>>> int(f)
13
>>> complex(f)
(13.4+0j)
>>> str(f)
'13.4'
>>> bool(f)
True
>>> a = 0
>>> bool(a)
False
>>> c = 12+3j
>>> int(c)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    int(c)
TypeError: can't convert complex to int
>>> float(c)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    float(c)
TypeError: can't convert complex to float
>>> str(c)
'(12+3j)'
>>> bool(c)
True
>>> list(c)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    list(c)
TypeError: 'complex' object is not iterable
>>> s = 'codegnan'
>>> a = '83456'
>>> int(s)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    int(s)
ValueError: invalid literal for int() with base 10: 'codegnan'
>>> int(a)
83456
>>> float(a)
83456.0
>>> complex(a)
(83456+0j)
>>> bool(a)
True
>>> list(a)
['8', '3', '4', '5', '6']
>>> tuple(a)
('8', '3', '4', '5', '6')
>>> set(a)
{'4', '6', '8', '3', '5'}
>>> l = [3, 45, 67, 32, 243]
>>> int(l)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    int(l)
TypeError: int() argument must be a string, a bytes-like object or a number, not 'list'
>>> float(l)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    float(l)
TypeError: float() argument must be a string or a number, not 'list'
>>> str(l)
'[3, 45, 67, 32, 243]'
>>> bool(l)
True
>>> tuple(l)
(3, 45, 67, 32, 243)
>>> set(l)
{32, 67, 3, 45, 243}
>>> dict(l)
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    dict(l)
TypeError: cannot convert dictionary update sequence element #0 to a sequence
>>> #list can be converted into str, bool, tuple, set
>>> t = (1,2,3,4,5)
>>> bool(t)
True
>>> str(t)
'(1, 2, 3, 4, 5)'
>>> list(t)
[1, 2, 3, 4, 5]
>>> set(t)
{1, 2, 3, 4, 5}
>>> #tuple can be converted into str, bool, list, set
>>> #set can be converted into str, bool, list,tuple
>>> s = {1, 2, 3, 5, 4}
>>> str(s)
'{1, 2, 3, 4, 5}'
>>> bool(s)
True
>>> list(s)
[1, 2, 3, 4, 5]
>>> tuple(s)
(1, 2, 3, 4, 5)
>>> int(s)
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    int(s)
TypeError: int() argument must be a string, a bytes-like object or a number, not 'set'
>>> #dict can be converted into bool, list, tuple, set, str
>>> dict= {1:1,2:2,3:3}
>>> float(dict)
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    float(dict)
TypeError: float() argument must be a string or a number, not 'dict'
>>> str(dict)
'{1: 1, 2: 2, 3: 3}'
>>> list(dict)
[1, 2, 3]
>>> set(dict)
{1, 2, 3}
>>> tuple(dict)
(1, 2, 3)
>>> bool(dict)
True
>>> bool = True
>>> int(bool)
1
>>> float(bool)
1.0
>>> str(bool)
'True'
>>> complex(bool)
(1+0j)
>>> 
