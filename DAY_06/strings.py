Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 23:09:28) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #strings
>>> name = "lohitha"
>>> name
'lohitha'
>>> type(name)
<class 'str'>
>>> name = 'lohitha'
>>> name = """lohitha"""
>>> name = '''lohitha'''
>>> s = ' '
>>> s
' '
>>> #concatenation
>>> a = 'python'
>>> b = 'programming'
>>> a+b
'pythonprogramming'
>>> a+' '+b
'python programming'
>>> #repetition
>>> a*10
'pythonpythonpythonpythonpythonpythonpythonpythonpythonpython'
>>> 'lohitha'*10
'lohithalohithalohithalohithalohithalohithalohithalohithalohithalohitha'
>>> 
>>> names = 'lohitha harsha babitha'
>>> names
'lohitha harsha babitha'
>>> name
'lohitha'
>>> name[2]
'h'
>>> name[6]
'a'
>>> names[:7]
'lohitha'
>>> #slicing means extracting a part of a string
>>> names[8:14]
'harsha'
>>> names[:14]
'lohitha harsha'
>>> #index,slicing has negative and positive indexing
>>> names[::-1]
'ahtibab ahsrah ahtihol'
>>> names[-8:]
' babitha'
>>> names[-20:-11:-1]
''
>>> names[-19:-11;-1]
SyntaxError: invalid syntax
>>> names[-19:-11:-1]
''
>>> #Membership in strings-is,is not
>>> harsha in names
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    harsha in names
NameError: name 'harsha' is not defined
>>> 'harsha' in names
True
>>> 'babitha' in names
True
>>> 'varsha' not in names
True
>>> 'hari' in names
False
>>> #length
>>> len(names)
22
>>> #ord() is used to return ascii number
>>> #chr() is used to return ascii character
>>> ord('b')
98
>>> ord('B')
66
>>> chr(34)
'"'
>>> chr(56)
'8'
>>> chr(99)
'c'
>>> sorted(names)
[' ', ' ', 'a', 'a', 'a', 'a', 'a', 'b', 'b', 'h', 'h', 'h', 'h', 'h', 'i', 'i', 'l', 'o', 'r', 's', 't', 't']
>>> min(names)
' '
>>> max(names)
't'
>>> name = 'codegnan it solutions'
>>> name.upper()
'CODEGNAN IT SOLUTIONS'
>>> name.lower()
'codegnan it solutions'
>>> name.title()
'Codegnan It Solutions'
>>> name.capitalize()
'Codegnan it solutions'
>>> name.swapcase()
'CODEGNAN IT SOLUTIONS'
>>> #casefold-Converts a string into a case-insensitive lowercase form, mainly for comparison.
>>> name.center(50,-)
SyntaxError: invalid syntax
>>> name.center(50,'-')
'--------------codegnan it solutions---------------'
>>> name.center(20,',')
'codegnan it solutions'
>>> name.codegnan(100,'*')
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    name.codegnan(100,'*')
AttributeError: 'str' object has no attribute 'codegnan'
>>> name.center(100,'*')
'***************************************codegnan it solutions****************************************'
>>> name.ljust(30,'.')
'codegnan it solutions.........'
>>> name.rjust(50,'.')
'.............................codegnan it solutions'
>>> '456'.zfill(5)
'00456'
>>> '45'.zfill(2)
'45'
>>> '3'.zfill(10)
'0000000003'
>>> #find,rfind
>>> name = 'python full stack'
>>> name.find('python')
0
>>> name.find('f')
7
>>> s.find('l')
-1
>>> s.rfind('l')
-1
>>> name.find('l)
	      
SyntaxError: EOL while scanning string literal
>>> name.find('l')
	      
9
>>> name.rfind('l')
	      
10
>>> #rfind searches number from backwards, find searches for the number from starting
	      
>>> #in index when we give unknown value it gives error but in find it do not give error, so find method is more preferable
	      
>>> name.find('z')
	      
-1
>>> name.index('z')
	      
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    name.index('z')
ValueError: substring not found
>>> s.replace('o','2')
	      
' '
>>> name.replace('o','2')
	      
'pyth2n full stack'
>>> name.replace('python','java')
	      
'java full stack'
>>> #fro changing one character to another we use replace, but for many characters we use translate
	      
>>> #for converting into translate we first use maketrans() it converts data into bytes and then to translate
	      
>>> name.maketrans('aeiou','@#$%^')
	      
{97: 64, 101: 35, 105: 36, 111: 37, 117: 94}
>>> name.translate(name.maketrans('aeiou','@#$%^'))
	      
'pyth%n f^ll st@ck'
>>> 
