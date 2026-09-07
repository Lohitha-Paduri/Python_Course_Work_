Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 23:09:28) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #dictionary
>>> #mutable, ordered, heterogeneous, dynamically sized, unique(Duplicated not aloowed)
>>> d = {}
>>> type(d)
<class 'dict'>
>>> d = {1:2,2:3,3:4}
>>> d
{1: 2, 2: 3, 3: 4}
>>> d = {}
>>> d[1] = 1
>>> d[0.23] = 1
>>> d["str"] =1
>>> d[(1,2,3)]
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    d[(1,2,3)]
KeyError: (1, 2, 3)
>>> d[(1,2,3)] =1
>>> d[2+3j] =1
>>> d[False] = 1
>>> d
{1: 1, 0.23: 1, 'str': 1, (1, 2, 3): 1, (2+3j): 1, False: 1}
>>> d[True] = 1
>>> d
{1: 1, 0.23: 1, 'str': 1, (1, 2, 3): 1, (2+3j): 1, False: 1}
>>> d[[1,2,3]]
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    d[[1,2,3]]
TypeError: unhashable type: 'list'
>>> d[set(1,2,3)]
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    d[set(1,2,3)]
TypeError: set expected at most 1 arguments, got 3
>>> #in dictionary list and set are not allowed because they are mutable
>>> d[1] = 1
>>> d[2] = 2.34
>>> d[3] = "str"
>>> d[4] = 3+7j
>>> d[5] = [1,2,3]
>>> d[6] = (4,5,6)
>>> d[7] = {8,9,0}
>>> d[8] = True
>>> d[9] = frozenset({2,3,4})
>>> d[10] = {1:1,2:2}
>>> d[11] = None
>>> d
{1: 1, 0.23: 1, 'str': 1, (1, 2, 3): 1, (2+3j): 1, False: 1, 2: 2.34, 3: 'str', 4: (3+7j), 5: [1, 2, 3], 6: (4, 5, 6), 7: {8, 9, 0}, 8: True, 9: frozenset({2, 3, 4}), 10: {1: 1, 2: 2}, 11: None}
>>> d = {}
>>> d[1]=2
>>> d
{1: 2}
>>> d[1] = 3
>>> d
{1: 3}
>>> data = {'name':'lohitha','course':'pfs','batch':65}
>>> data
{'name': 'lohitha', 'course': 'pfs', 'batch': 65}
>>> #No concatenation, repetition, indexing, slicing
>>> 'lohitha' in data
False
>>> #because membership only works for keys not for values
>>> 'name' in data
True
>>> data['name']
'lohitha'
>>> data['batch']
65
>>> data['age']
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    data['age']
KeyError: 'age'
>>> data.get('name')
'lohitha'
>>> data.get('age')
>>> data.get('age','key is not present')
'key is not present'
>>> data.get('name','name is not present')
'lohitha'
>>> #in direct accesing if a key is not present we will get error, but in get() method we don't get error and also we can give a statement.
>>> data
{'name': 'lohitha', 'course': 'pfs', 'batch': 65}
>>> data['age']=21
>>> data
{'name': 'lohitha', 'course': 'pfs', 'batch': 65, 'age': 21}
>>> data['phone no']=736517238
>>> data
{'name': 'lohitha', 'course': 'pfs', 'batch': 65, 'age': 21, 'phone no': 736517238}
>>> data.update({'email':'padurilohitha@gmail.com','passout':2026})
>>> data
{'name': 'lohitha', 'course': 'pfs', 'batch': 65, 'age': 21, 'phone no': 736517238, 'email': 'padurilohitha@gmail.com', 'passout': 2026}
>>> #for adding multiple items we use update()
>>> id(data)
2108187480568
>>> data['py']=2027
>>> data
{'name': 'lohitha', 'course': 'pfs', 'batch': 65, 'age': 21, 'phone no': 736517238, 'email': 'padurilohitha@gmail.com', 'passout': 2026, 'py': 2027}
>>> data['age'] = 22
>>> id(data)
2108187480568
>>> #Data changes within same object reference
>>> data.popitem()
('py', 2027)
>>> data
{'name': 'lohitha', 'course': 'pfs', 'batch': 65, 'age': 22, 'phone no': 736517238, 'email': 'padurilohitha@gmail.com', 'passout': 2026}
>>> data.popitem()
('passout', 2026)
>>> data
{'name': 'lohitha', 'course': 'pfs', 'batch': 65, 'age': 22, 'phone no': 736517238, 'email': 'padurilohitha@gmail.com'}
>>> data.pop('email')
'padurilohitha@gmail.com'
>>> del data('course')
SyntaxError: can't delete function call
>>> del data['course']
>>> data
{'name': 'lohitha', 'batch': 65, 'age': 22, 'phone no': 736517238}
>>> data.clear()
>>> data
{}
>>>  data = {'name': 'lohitha', 'course': 'pfs', 'batch': 65, 'age': 22, 'phone no': 736517238, 'email': 'padurilohitha@gmail.com'}
SyntaxError: unexpected indent
>>> data = {'name': 'lohitha', 'course': 'pfs', 'batch': 65, 'age': 22, 'phone no': 736517238, 'email': 'padurilohitha@gmail.com'}
>>> data
{'name': 'lohitha', 'course': 'pfs', 'batch': 65, 'age': 22, 'phone no': 736517238, 'email': 'padurilohitha@gmail.com'}
>>> len(data)
6
>>> data.keys()
dict_keys(['name', 'course', 'batch', 'age', 'phone no', 'email'])
>>> data.values()
dict_values(['lohitha', 'pfs', 65, 22, 736517238, 'padurilohitha@gmail.com'])
>>> max(data)
'phone no'
>>> min(data)
'age'
>>> sorted(d)
[1]
>>> sorted(data)
['age', 'batch', 'course', 'email', 'name', 'phone no']
>>> a = {1:1,2:2}
>>> m = a
>>> m[3]=3
>>> m
{1: 1, 2: 2, 3: 3}
>>> a
{1: 1, 2: 2, 3: 3}
>>> n=a.copy()
>>> n[5]=5
>>> n
{1: 1, 2: 2, 3: 3, 5: 5}
>>> a
{1: 1, 2: 2, 3: 3}
>>> data
{'name': 'lohitha', 'course': 'pfs', 'batch': 65, 'age': 22, 'phone no': 736517238, 'email': 'padurilohitha@gmail.com'}
>>> data.get('passout')
>>> data.setdefault('passout',2026)
2026
>>> data
{'name': 'lohitha', 'course': 'pfs', 'batch': 65, 'age': 22, 'phone no': 736517238, 'email': 'padurilohitha@gmail.com', 'passout': 2026}
>>> data.setdefault('name',2026)
'lohitha'
>>> #Here name won't get updated beacuse it already has name lohitha, if i dont have a value in a key, then the value will be changed
>>> data.setdefault('course',2027)
'pfs'
>>> dict.fromkeys(["Python","mysql","java"])=0
SyntaxError: can't assign to function call
>>> dict.fromkeys(["Python","mysql","java"],0)
{'Python': 0, 'mysql': 0, 'java': 0}
>>> 
