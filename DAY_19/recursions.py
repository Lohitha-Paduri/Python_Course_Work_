'''
#This prints 1-10 numbers
def display(n):
    if n==11:
        return
    print(n)
    display(n+1)
    
display(1) 

  
#This prints numbers from 10-1, The recursive call happens first, and print(n) happens after that call finishes
def display(n):
    if n==11:
        return
    display(n+1)
    print(n)
    
display(1) 


def display(s,n):
    if n==len(s):
        return
    display(s,n+1)
    print(s[n])
    
display("Codegnan",0)    



def display(s,ind,w):
    if len(s)-w+1 < ind:
        return
    print(s[ind:ind+w])
    display(s,ind+1,w)
    
s = input()
w = int(input())
display(s,0,w)  



#Take a list of elements and print its sum using recursion
def display(lst, ind):
    if ind == len(lst):       
        return 0
    return lst[ind] + display(lst, ind + 1)   

lst = list(map(int, input("Enter list elements: ").split()))
print(display(lst,0))
      


#take sum of digits and print its sum using recursion
def display(num):
    if num == 0:
        return 0
    return (num % 10) + display(num // 10)

num = int(input())
print(display(num)) 

   
#Reverse a number
def display(num):
    if num == 0:
        return 1
    return (num % 10) * display(num // 10)

num = int(input())
print(display(num))  


#Factorial of a num
def factorial(n):
    if n==0:
        return 1
    return n*factorial(n-1)
print(factorial(5))
print(factorial(1))
print(factorial(7)) 

'''
#fibonacci series
def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    return fibonacci(n-1)+fibonacci(n-2)

for i in range(10):
    print(fibonacci(i))