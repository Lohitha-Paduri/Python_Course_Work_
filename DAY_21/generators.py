#Generator - A generator is a Python object that generates and provides values one at a time using yield, 
# instead of storing and returning all values at once.
'''
def reels():
    data = ['1..100','2..200','3..300','4..400']
    for i in data:
        yield i

result = reels()

print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))



def countdown():
     yield 5
     yield 4
     yield 3
     yield 2
     yield 1
 
result = countdown()

for i in result:
    print(i)             
    

def fact(n):
    for i in range(1, n+1):
        if n%i ==0:
            yield i 
            
result = fact(12)
for i in result:
    print(i)

'''
def prime(n):
    for i in range(2,n+1):
        for j in range(2,i//2+1):
            if i%j ==0:
                break
        else:
            yield i
result = prime(12)  
for i in result:
    print(i, end = " ")                             