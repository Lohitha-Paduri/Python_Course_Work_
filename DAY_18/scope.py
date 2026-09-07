"""
#Local Variables - Declared inside a function, method, or block and can generally be accessed only within that scope.

def display():
    n=10
    print("Inside Function: ",n)
    
display()   
print("Outside Function:",n) 


#Global Variables - Declared outside functions/blocks and can generally be accessed from multiple parts of the program.
def display():
    print("Inside Function: ",n)
   
n=10
display()
print("Outside Function: ",n)    


#To access the local variable outside we need to use 'Global' keyword.
def display():
    global n
    n=10
    print("Inside Function: ",n)
  
display()
print("Global Variable: ",n)  


#whenever we use gloabl keyword for a variable, we should not pass it as parameters.
def display():
    global n
    n+=10
    print("Inside Function:",n)
    
n=10
display()
print("Outside Function: ",n)  


def display():
    course = "PFS"
    def update():
        course = "JFS"
        print("Inside Function: ",course)
    update()
    print("Outside Function: ",course)
    
display()


#nonlocal = change the outer function's variable.
def display():
    course = "PFS"
    def update():
        nonlocal course
        course = "JFS"
        print("Inside Function: ",course)
    update()
    print("Outside Function: ",course)
    
display()


#built-in methods cannot be declared as a variable, If you declare a built-in function/method name as a variable, you replace (shadow) the original built-in name in that scope.
l=[1,2,3,4,5]
print(sum(l))

sum = 20
print(sum(l))   


l=[1,2,3,4,5]
print(sum(l))

sum = 20
print(sum)        

"""
     