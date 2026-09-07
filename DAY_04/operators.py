Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 23:09:28) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Python operators
>>> #Arithmetic operators
>>> a = 10
>>> b = 5
>>> a+b
15
>>> a-b
5
>>> a*b
50
>>> a/b
2.0
>>> a//b
2
>>> 10.2//2
5.0
>>> a *** 3
SyntaxError: invalid syntax
>>> a**3
1000
>>> 2**3
8
>>> 15**5
759375
>>> #Comparison operators
>>> a>b
True
>>> a<b
False
>>> a>=b
True
>>> a<=b
False
>>> a>=8
True
>>> a == b
False
>>> a!=b
True
>>> #Assignemnt operators
>>> a = 20
>>> a = a+30
>>> a
50
>>> 
>>> a += 10
>>> a
60
>>> a *= 3
>>> a
180
>>> a = 100
>>> a //= 3
>>> a
33
>>> a **= 2
>>> a
1089
>>> a %= 3
>>> a
0
>>> a = 100
>>> a %= 3
>>> a
1
>>> a -= 1
>>> a
0
>>> #Logical operators
>>> email = True
>>> password = False
>>> email and password
False
>>> email or password
True
>>> not email
False
>>> 7%2==0
False
>>> 7%2 == 0 and 5%3 == 0
False
>>> 6%2==0 or 3%1==5
True
>>> not 6%2 == 0
False
>>> login = False
>>> Displayproducts = True
>>> login or displayproducts
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    login or displayproducts
NameError: name 'displayproducts' is not defined
>>> login or Displayproducts
True
>>> 's' in 'aeiou'
False
>>> 'a' not in 'aeiou'
False
>>> #Membership operator
>>> #str list tuple set dict for these we can apply membership operator
>>> s = 'Python programming'
>>> 'Python' in s
True
>>> 'java' in s
False
>>> 'z' in s
False
>>> 'a' in s
True
>>> 'c++' not in s
True
>>> 'program' not in s
False
>>> a = [1,2,3,4,5]
>>> 3 in l
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    3 in l
NameError: name 'l' is not defined
>>> 3 in a
True
>>> 8 not in a
True
>>> 1 not in a
False
>>> t = (45, 67, 43)
>>> 43 in t
True
>>> 89 in t
False
>>> 45 not in t
False
>>> d = {'name':'lohitha', 'age':21, 'course':'pfs'}
>>> lohitha in d
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    lohitha in d
NameError: name 'lohitha' is not defined
>>> 'lohitha' in d
False
>>> #MO only works for keys not for values
>>> 'name
SyntaxError: EOL while scanning string literal
>>> 'name' in d
True
>>> 21 not in d
True
>>> 'course' not in d
False
>>> l = [1,2,3, 'lohitha']
>>> 'lo' in l
False
>>> #becuase list is collection of strings
>>> 'lohitha' in l
True
>>> #Identity Operators
>>> l = [23, 34, 45,56]
>>> m = [23, 34, 45, 56]
>>> id(l)
2003708129736
>>> id(m)
2003710864840
>>> i is m
Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    i is m
NameError: name 'i' is not defined
>>> l is m
False
>>> a = m
>>> m
[23, 34, 45, 56]
>>> id(m)
2003710864840
>>> m is a
True
>>> a is not m
False
>>> #Bitwise operators
>>> 11&12
8
>>> 34 | 12
46
>>> 89 ^ 12
85
>>> 4<<7
512
>>> 9>>1
4
>>> ~64
-65
>>> 
