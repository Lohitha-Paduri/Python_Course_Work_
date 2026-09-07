#str, list, tuple,set,dict, range(these we can take for iteration)
'''
s = "Python programming"
for name in s:
    print(name)


l = [1,2,3,4,5]
for i in l:
    print(i)    


t = (1,2,3,45)  
for i in t:
    #print(t) it repeats (1,2,3,45) for 4 times, because we have 4 elements in it. 
    print(i)  


s = {'lohitha', 'harsha','babitha'}
for i in s:
    print(i)   


dict = {1:2,3:4,5:6,7:8}
for d in dict:
    print(d) #gives only keys
    #print(dict) 
    #print(d,dict[d]) gives key and values
------------------------------------------------------------------------------    

#range(start, end+1,step): (0,,1) used for generating numeric value

for i in range(1,11):
    print(i)


for i in range(2,21,2):
    print(i)  


for i in range(5,101,5):
    print(i)    


for i in range(5,0,-1):
    print(i) 


for i in range(21,0,-2):
    print(i) 


name = "Python programming"
for i in range(18):
    print(i,name[i])   #name[i] gives index along with characters              
    

name = "Python programming"
for i in range(len(name)):
    print(i,name[i]) 
    
#indexing is only str, list, tuple


l = [1,2,3,4,5]
for i in range(len(l)):
    print(i,l[i])    



t = (1,2,3,4,5)
for i in range(len(t)):
    print(i,t[i]) 
    

#enumerate- gives sequence of numbers       

s = "python programming"
for i in enumerate(s):
    print(i)  #i[0] gives only sequence of number, i[0],i[1] give sequence along with s


l = [1,2,3,4]
for i in enumerate(l):
    print(i) 


t = (1,2,3,4)
for i in enumerate(t):
    print(t)


s = {1,2,3,1,2,3}
for i in enumerate(s):
    print(i)    


d = {1:2,3:4,4:5}
for i in enumerate(d):
    print(i,i[0],d[i[1]])  


for i in range(1,11):
    if i == 5:
        break
    print(i)  


for i in range(1,11):
    if i==5:
        continue #skips the loop and then it continues
    print(i) 


#for with else - if there is no break statement executed then the else block will execute, if the break statement executes then the else loop will not executes

for i in range(1,11):
    if i == 16:
        break
    print(i)
else:
    print("End of loop")




l = [12,2,34,45]
for i in l:
    if i==2:
        print(i,"found")             
        
    
l = [12,2,34,45]
for i in l:
    if i==2:
        print(i,"found")
    else:
        print(i,"not found")

l = [12,2,34,45]
n=45
for i in l:
    if i==n:
        print(n,"found")
else:
    print(n,"not found")
     

l = [12,2,34,45]
n=78
for i in l:
    if i==n:
        print(n,"found")
        break
else:
    print(n,"not found") 
    


pin = 7890
for i in range(5):
    epin = int(input("Enter the pin:"))
    if epin == pin:
        print("Phone unlocked")
        break
    else:
        print("Try Again")              
else:
    print("Try Again after 30 Seconds")   
 
'''
 

         