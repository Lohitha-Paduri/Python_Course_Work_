'''
l = []
for i in range(1,11):
    l.append(i)
print(l)  


#using list compression
l = [i for i in range(1,11)]  
print(l)


#printing even numbers
l = [i for i in range(2,11,2)]
print(l)


#divisible by number or not
n=16
l = [i for i in range(1,n+1) if n%i==0]
print(l)

#print even numbers, in place of odd numbers print '0'
x = [1,2,3,4,5,6]
y = [i if i%2==0 else 0 for i in x]
print(y)


#print nested list
x = [[j for j in range(1,4)]for i in range(3)]
print(x)


x = [[i for i in range(j,j+3)] for j in range(1,10,3)]
print(x)

#set
n=16
s = {i for i in range(1,n+1) if n%i==0}
print(s)
'''
#dictionary
s = {i:i*i for i in range(1,11)}
print(s)
