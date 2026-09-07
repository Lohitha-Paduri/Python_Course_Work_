'''
#sys module is used to interact with the Python interpreter and system-specific information.
import sys

print(sys.argv)
print(sys.argv[-1])
print(sys.path)
print(sys.version)
print("start")
sys.exit()
print("End")


#platform module is used to get information about the computer/system and operating system.
import platform

print(platform.system())
print(platform.release())
print(platform.processor())


#math module is used for mathematical calculations.
import math

print(math.pi)
print(math.e)
print(math.log(2,2))
print(math.sin(30))
print(math.cos(30))
print(math.tan(30))
print(math.degrees(30))
print(math.radians(30))
print(math.factorial(5))
print(math.gcd(12,24))
print(math.sqrt(49))
print(math.pow(2,3))



import math

print(round(12.00001))
print(round(12.3))
print(round(12.6666))
print(round(12.99998))

print(math.ceil(12.00001))
print(math.ceil(12.3))
print(math.ceil(12.6666))
print(math.ceil(12.99998))

print(math.floor(12.0001))
print(math.floor(12.3))
print(math.floor(12.6666))
print(math.floor(12.99998))



#random module is used to generate random values.
import random

random.seed(9)

print(random.random())
print(random.randint(1,20))
print(random.uniform(1,6))

l = ['r','p','s']
print(random.choice(l))

lang = ['python', 'html','css','js']
print(random.choices(lang,k =2))

random.shuffle(lang)
print(lang)


#counting frequency using dict
text = input("Enter the word: ")
dict = {}
for i in text:
    if i in dict:
        dict[i]+=1
    else:
        dict[i]=1 
        
print(dict) 


#counting frequency using Counter method
#Counter is a class from the collections module. 
# It is used to count how many times each item occurs in a list, string, tuple, etc.

from collections import Counter

text = input("Enter the word: ")
result = Counter(text)
print(result)

   

#defaultdict is used when you want a default value automatically when a key does not exist, instead of getting a KeyError.
from collections import Counter,defaultdict

products = ['milk', 'rice', 'sugar']
res = defaultdict(list)
for i in products:
    res[i].append(['price','quan','bill'])
print(res)    

text ='python programming'
dict = defaultdict(int)
for i in text:
    dict[i]+=1
print(dict)  


#deque is used when you need to add or remove elements efficiently from both the beginning and the end of a sequence.
from collections import Counter,defaultdict,deque

l = deque([])    

l.append(10)
l.append(20)
l.append(30)
l.append(40)
l.popleft()
l.popleft()
l.append(50)
l.append(60)

print(l)  
    
'''

from collections import Counter,defaultdict,deque

l = deque([])    

l.appendleft(10)
l.appendleft(20)
l.appendleft(30)
l.appendleft(40)
l.pop()
l.pop()
l.appendleft(50)
l.appendleft(60)

print(l)
    