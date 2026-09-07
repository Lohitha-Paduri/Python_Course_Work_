Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 23:09:28) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = 10
>>> a=b=c=10
>>> a
10
>>> b
10
>>> c
10
>>> a,b,c=10,20,30
>>> a
10
>>> b
20
>>> c
30
>>> a,b = b,a
>>> a
20
>>> b
10
>>> del a
>>> a
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    a
NameError: name 'a' is not defined
>>> b,c
(10, 30)
>>> b.a
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    b.a
AttributeError: 'int' object has no attribute 'a'
>>> b,a
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    b,a
NameError: name 'a' is not defined
>>> 
