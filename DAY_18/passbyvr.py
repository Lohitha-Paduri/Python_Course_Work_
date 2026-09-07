'''
#Pass by value - changing the parameter inside the function does not change the original variable.

#int
def display(n):
    n+=10
    print("Inside the Function: ",n)
    
n=10
display(n)
print("Outside the function: ",n) 


#float
def display(n):
    n+=10.5
    print("Inside the Function: ",n)
    
n=10.7
display(n)
print("Outside the function: ",n) 


#string
def display(n):
    n+="language"
    print("Inside the Function: ",n)
    
n="python"
display(n)
print("Outside the function: ",n) 


#complex
def display(n):
    n+=7
    print("Inside the Function: ",n)
    
n=10+5j
display(n)
print("Outside the function: ",n) 


#tuple
def display(n):
    n+=(5,)
    print("Inside the Function: ",n)
    
n=(1,2,3,4)
display(n)
print("Outside the function: ",n)

#bool
def display(n):
    n = False
    print("Inside the Function: ",n)
    
n=True
display(n)
print("Outside the function: ",n)


#Pass by Reference - changing the object inside the function can affect the original object.

#list
def display(n):
    n.append(5)
    print("Inside the Function: ",n)
    
n=[1,2,3,4]
display(n)
print("Outside the function: ",n) 


#set
def display(n):
    n.add(5)
    print("Inside the Function: ",n)
    
n={1,2,3,4}
display(n)
print("Outside the function: ",n)


#dict
def display(n):
    n[5]=6
    print("Inside the Function: ",n)
    
n={1:2,3:4}
display(n)
print("Outside the function: ",n) 

'''

def display(n):
    n[5]=6
    print("Inside the Function: ",n)
    
n={1:2,3:4}
display(n)
print("Outside the function: ",n) 