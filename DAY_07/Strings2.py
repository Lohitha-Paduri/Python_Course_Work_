Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 23:09:28) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #strings
>>> #whitespace and trimming
>>> name = '   lohitha    paduri'
>>> name = '    lohitha   paduri   '
>>> name.strip()
'lohitha   paduri'
>>> name.lstrip()
'lohitha   paduri   '
>>> name.rstrip()
'    lohitha   paduri'
>>> #strip is used to remove spaces, it only removes side spaces not in between spaces
>>> #splitting and joining methods
>>> name.replace(' ','')
'lohithapaduri'
>>> s = 'python-java-sql-javascript-c-fastapi'
>>> s.split('-')
['python', 'java', 'sql', 'javascript', 'c', 'fastapi']
>>> s.split('-',2)
['python', 'java', 'sql-javascript-c-fastapi']
>>> s.rsplit('-',2)
['python-java-sql-javascript', 'c', 'fastapi']
>>> names = """lohitha
harsha
babitha
usha
"""
>>> names.splitlines()
['lohitha', 'harsha', 'babitha', 'usha']
>>> s = ['python','sql','java','flask']
>>> text = "I am a python trainee"
>>> text.split()
['I', 'am', 'a', 'python', 'trainee']
>>> s
['python', 'sql', 'java', 'flask']
>>> ''.join(c)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    ''.join(c)
NameError: name 'c' is not defined
>>> ''.join(s)
'pythonsqljavaflask'
>>> ' '.join(s)
'python sql java flask'
>>> ', '.join(s)
'python, sql, java, flask'
>>> '@'.join(s)
'python@sql@java@flask'
>>> '-'.join(('1','2','3'))
'1-2-3'
>>> '-'.join({'1','2','3'})
'3-1-2'
>>> s
['python', 'sql', 'java', 'flask']
>>> a = 'string.py.java.png.txt')
SyntaxError: invalid syntax
>>> a = 'string.py.java.png.txt'
>>> a
'string.py.java.png.txt'
>>> a.partition('.')
('string', '.', 'py.java.png.txt')
>>> a.rpartition('.')
('string.py.java.png', '.', 'txt')
>>> #String testing
>>> name = "lohitha paduri"
>>> name.startswith('loh')
True
>>> name.endswith('uri')
True
>>> name.startswith('harsha')
False
>>> 'hello'.islower()
True
>>> 'Hello'.islower()
False
>>> 'HELLO',isupper()
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    'HELLO',isupper()
NameError: name 'isupper' is not defined
>>> 'HELLO'.isupper()
True
>>> 'HEllo'.isupper()
False
>>> 'sdhjgfs'.isaplha()
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    'sdhjgfs'.isaplha()
AttributeError: 'str' object has no attribute 'isaplha'
>>> 'sgaffgre'.isalpha()
True
>>> "GRAZRTGE".isalpha()
True
>>> 'SGARWAR$desas$'.isalpha()
False
>>> #because of special character
>>> 'AGFRefsdfr'.isalpha()
True
>>> '4765184'.isalnum()
True
>>> '326541@4%'.isalnum()
False
>>> 'sdfa374528'.isalnum()
True
>>> '       '.isspace()
True
>>> '      kkh  L'.isspace()
False
>>> 'Lohitha Paduri'.istitle()
True
>>> 'LOhitha paduri'.istitle()
False
>>> 'my_var'.isidentifier()
True
>>> 'my#var'.isidentifier()
False
>>> 'if'.isidentifier()
True
>>> 'else'.isidentifier()
True
>>> 'while'.isidentifier()
True
>>> 'false'.isidentifier()
True
>>> 'False'.isidentifier()
True
>>> #isdecimal(),isnumeric(),isdigit()
>>> '241321'.isdecimal()
True
>>> 'DSAFEF34'.isdecimal()
False
>>> '865387'.isdigit()
True
>>> #isdigit is used for subscript and superscript
>>> 'VII'.isnumeric()
False
>>> '8335482'.isnumeric()
True
>>> #isnumeric() also works for roman numbers
>>> 
