'''
#match()-Checks for a match at the beginning of a string.

import re
pattern = r'[0-9]'
text = '25Codegnan2026'
res = re.match(pattern,text)
print(res.group() if res else "Match not found")


#re.search()- Searches for the first occurrence of a pattern anywhere in the string.
import re
pattern = r'[0-9]'
text = 'Codegnan2026'
res = re.search(pattern,text)
print(res.group() if res else "Match not found")


#re.findall()- Returns all matching occurrences as a list.

import re
pattern = r'[0-9]'
text = 'Codegnan2026'
res = re.findall(pattern,text)
print(res)


#re.finditer() - Returns an iterator containing match objects for all occurrences.
import re
pattern = r'[0-9]'
text = 'Codegnan2026'
res = re.finditer(pattern,text)
for i in res:
    print(i.group(), i.start())
   

#re.fullmatch() - Checks whether the entire string matches the specified pattern.   
import re
pattern = r'[0-9]{10}'
text = '9876543210'
res = re.fullmatch(pattern,text)
print(res.group() if res else "Match not found")
 

 #re.split()- Splits a string wherever the specified pattern matches.
import re
pattern = r'[,@:;_&]'
text = 'java,python@c:flask_mysql&django'
res = re.split(pattern,text)
print(res)



#re.sub() - Replaces matching patterns with another string.
import re
pattern = r'[aeiou0-9]'
text = 'java 29 python 45 c 89 flask 12 mysql 09 django'
res = re.sub(pattern, '*', text)
print(res)


import re
pattern = r'h.t'
text = 'hand loom hat hit hot horse dog'
res = re.findall(pattern, text)
print(res) 


 
import re
pattern = r'^[a-z]' #^ is used for starts with smallcase of atoz if we gives caps shows empty
text = 'hat hood wood shood hand hit loom hot'
res = re.findall(pattern,text) 
print(res)



import re
pattern = r'[a-z]$' #$ is used for ends with smallcase of atoz if we gives caps shows empty
text = 'hat hood wood shood hand hit loom hot'
res = re.findall(pattern,text)
print(res)


import re
pattern = r'ab*'
text = 'a ab aab abbb aaabbbbb'
res = re.findall(pattern,text) 
print(res)


import re
pattern = r'^(91|0)'
text = '91165677238'
res = re.findall(pattern,text) 
print(res)


import re
pattern = r'[a-zA-Z0-9]'
text = 'dshafgkrSDFGSA40751$TEGHs'
res = re.findall(pattern,text) 
print(res)


import re
pattern = r'(ae)'
text = 'dshafgkraeSDFGSA4075AE1$TEGHs'
res = re.findall(pattern,text) 
print(res)


import re
pattern = r'[0-9]{2}'
text = 'dshafgkraeSDFGSA40725AE1$TEGHs'
res = re.findall(pattern,text) 
print(res)


import re
pattern = r'\S'
text = 'dsha fgkr aeSDFGSA 40725AE1 $TEGHs'
res = re.findall(pattern,text) 
print(res)


import re
pattern = r'\s'
text = 'dsha fgkr aeSDFGSA 40725AE1 $TEGHs'
res = re.findall(pattern,text) 
print(res)


import re
name = input("Enter the name:")
pattern = r'^[a-zA-z]{2,25}([a-zA-Z]{2,25})+$'

res = re.fullmatch(pattern,name) 
print("valid Name" if res else "Invalid Name")



import re
email = input("Enter your email :")
pattern = r'^[a-zA-Z._0-9]+@[a-zA-Z._0-9]+\.[A-Za-z]{2,}$'  
res = re.fullmatch(pattern,email)
print("Valid email "if res else "Invalid email ")

import re
phone = input("Enter your phonno :")
pattern = r'^[6-9]\d{9}'  
res = re.fullmatch(pattern,phone)
print("Valid phone"if res else "Invalid phone")

'''
import re
PAN = input("Enter your PANCARD :")
pattern = r'^[A_z]{6}\d{4}[A-z]{1}'  
res = re.fullmatch(pattern,PAN)
print("Valid PAN"if res else "Invalid PAN")