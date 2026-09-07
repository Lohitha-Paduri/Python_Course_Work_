'''
#print list of factors using for loop
12 = [1,2,3,4,5,6,12]

n = int(input("Enter the number: "))
res = []
for i in range(1, n+1):
    if n%i==0:
        res.append(i)
print(f"Factors of {n} = {res}")  
      
      

#s = 'python programming'
#{'p':2,'y':1,...}

s = input("Enter the string: ")
freq = {}
for char in s:
    if char in freq:
        freq[char] +=1
    else:
        freq[char] = 1 
print(freq) 
          
          
'''
#aaaabbbbjj  a4b4j2
s = input("Enter the letters: ")
count = 1
res = ''
for i in range(len(s)-1):
    if s[i] ==s[i+1]:
        count+=1
    else:
        res+= s[i]+str(count)
        count =1
print(res+s[i]+str(count))


   