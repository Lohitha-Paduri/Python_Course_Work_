Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 23:09:28) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #input formatting
>>> a = input()
codegnan
>>> a
'codegnan'
>>> a = input()
45
>>> a
'45'
>>> a = input("Enter the number:")
Enter the number:45
>>> a
'45'
>>> #Here we are getting numbers in string form, to convert string into integer we use int(input())
>>> marks = int(input("Enter the marks:"))
Enter the marks:99
>>> marks
99
>>> #for float values we use float(input())
>>> cgpa = float(input("Enter the cgpa:"))
Enter the cgpa:9.9
>>> cgpa
9.9
>>> #split() default value is split, and it defaultly seperates when there is space
>>> names = input().split()
lohitha harsha babitha
>>> names
['lohitha', 'harsha', 'babitha']
>>> list.split()
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    list.split()
AttributeError: type object 'list' has no attribute 'split'
>>> list(names)
['lohitha', 'harsha', 'babitha']
>>> names = lohitha,harsha,babitha
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    names = lohitha,harsha,babitha
NameError: name 'lohitha' is not defined
>>> >>> names = 'lohitha,harsha,babitha'
SyntaxError: invalid syntax
>>> names = 'lohitha,harsha,babitha'
>>> names.split(',')
['lohitha', 'harsha', 'babitha']
>>> names = 'lohitha babitha harsha'
>>> names.split()
['lohitha', 'babitha', 'harsha']
>>> courses = 'c++-java-python'
>>> courses.split('-')
['c++', 'java', 'python']
>>> names = tuple(input("Enter the names:").split())
Enter the names:lohitha harsha 
>>> names
('lohitha', 'harsha')
>>> names = tuple(input("Enter the names:"))
Enter the names:harsha babitha
>>> names
('h', 'a', 'r', 's', 'h', 'a', ' ', 'b', 'a', 'b', 'i', 't', 'h', 'a')
>>> #here we are getting names in single letter becuase we didn't use split() here
>>> names = set(input("Enter the names:").split())
Enter the names:lohitha munni jenni
>>> names
{'munni', 'lohitha', 'jenni'}
>>> marks = input.split()
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    marks = input.split()
AttributeError: 'builtin_function_or_method' object has no attribute 'split'
>>> marks = input().split()
12 34 45 56
>>> marks
['12', '34', '45', '56']
>>> map(int,marks)
<map object at 0x000002C6440A5E10>
>>> list(map(int,marks))
[12, 34, 45, 56]
>>> marks = list(map(int,input("Enter the marks:").split()))
Enter the marks:23 34 45 56 78 90
>>> marks
[23, 34, 45, 56, 78, 90]
>>> marks = tuple(map(int,input("Enter the marks:").split()))
Enter the marks:90 89 98 87 89
>>> marks
(90, 89, 98, 87, 89)
>>> cgpa = list(map(float,input("Enter the cgpa:").split()))
Enter the cgpa:9.8 8.7 6.7 9.0
>>> cgpa
[9.8, 8.7, 6.7, 9.0]
>>> marks = set(map(int,input("Enter the marks:").split()))
Enter the marks:12 23 24 25 21
>>> marks
{12, 21, 23, 24, 25}
>>> #we need to write list,set,tuple before map becuase it gives object reference
>>> #How packing &unpacking uses here
>>> a,b = [1,2]
>>> a
1
>>> b
2
>>> a,b,c=(23,43,'str')
>>> a
23
>>> b
43
>>> c
'str'
>>> email,password = input("Enter the password:").split())
SyntaxError: invalid syntax
>>> email,password = input("Enter the password:").split()
Enter the password:hello@email.com 123
>>> email
'hello@email.com'
>>> password
'123'
>>> name,marks = input("Enter name,marks:").split()
Enter name,marks:lohitha 98
>>> a,b,c = list(map(int,input("Enter a,b,c :").split()))
Enter a,b,c :12 23 34
>>> a
12
>>> b
23
>>> c
34
>>> #eval function is used to take a string and calculate it as a Python expression.
>>> status = eval(input())
True
>>> status
True
>>> type(status)
<class 'bool'>
>>> status = eval(input))
SyntaxError: invalid syntax
>>> status = eval(input())
2+3j
>>> type(status)
<class 'complex'>
>>> status = eval(input())
status = eval(input())
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    status = eval(input())
  File "<string>", line 1
    status = eval(input())
           ^
SyntaxError: invalid syntax
>>> status
(2+3j)
>>> status = eval(input())
{1,2,3,4}
>>> status
{1, 2, 3, 4}
>>> type(status)
<class 'set'>
>>> status = eval(input())
lohitha
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    status = eval(input())
  File "<string>", line 1, in <module>
NameError: name 'lohitha' is not defined
>>> #by using eval() we cannot convert string, because it do not consider string as code
>>> num = eval(input())
{1:1,2:2,3:3}
>>> num
{1: 1, 2: 2, 3: 3}
>>> type(num)
<class 'dict'>
>>> 
num = eval(input())
[1,2,3,4]
>>> num
[1, 2, 3, 4]
>>> 
