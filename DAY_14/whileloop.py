'''
i = 1
while i<=10:
    print(i)
    i+=1
    

i = 10
while i>0:
    print(i)
    i-=1   
    

i = 5
while i<=50:
    print(i)
    i+=5  
    

s = 'while loop'
i=0
while i<len(s):
    print(s[i])  
    i+=1 
       

s = 'while loop'
i=len(s)-1
while i>=0:
    print(s[i])  
    i-=1
 

l = [6547, 32345, 8778]
i = 0

while i < len(l):
    print(l[i])
    i += 1    
  


n = 5678
while n>0:
    print(n%10)
    n//=10
    
   

n = 5678
sum = 0
while n>0:
    sum = sum+n%10
    n//=10
print(sum)


n = 5678
prod = 1
while n>0:
    prod *= n%10
    n//=10
print(prod)


 
n = 8765
rev = 0
while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n = n // 10
print( rev)




n = 5678
sum = 0
while n > 0:
    digit = n % 10
    if digit % 2 == 0:
        sum = sum + digit
    n = n // 10
print(sum)


l = [12, 23, 7, 4, 0, 0, 5, 6]
i =0
while i<len(l):
    if l[i]==0:
        l.remove(0)
    else:
        i += 1
print(l)        

l = [12, 23, 7, 4, 0, 0, 5, 6]
while 0 in l:
    l.remove(0)
print(l)    
'''

l = [12, 23, 7, 4,1, 0, 0, 5, 6]
i=0
j=len(l)-1

while i<=j:
    if i == j:
        print(l[i])
    else:
        print(l[i]+l[j])
    i+=1
    j-=1        
              