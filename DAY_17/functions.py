'''
def function_name(args):
    #stmts
    return(optional)

function_name(paramters)    
    
'''

'''

def gst(price):
    print("Original price: ", price)
    print("After adding GST: ",price+price*0.18)
   
gst(1500)
gst(459)
gst(2000)
gst(900)
gst(1300)    




def table(n):
    print(f"{n}-Table")
    print("------------------")
    for i in range(1,11):
        print(f"{n} * {i} = {n*i}")
       
table(5)     


#printing multiple tables at once
def table(n):
    print()
    print(f"{n}-Table")
    print("------------")
    for i in range(1,11):
        print(f"{n} * {i} = {n*i}")
   

for i in range(1,21):       
    table(i)     
   


def isleap(year):
    if year%400==0 or (year%4==0 and year%100!=0):
        return "Leap Year"
    else:
        return "Not a leap year"

print(isleap(2004))  
print(isleap(2005))
print(isleap(1900))  



def prime(n):
    for i in range(2,n):
        if n%i==0:
            return "Not a prime Number"
        else:
            return "Prime number" #I can directly return this to for
        
print(prime(5))
print(prime(6))
print(prime(17))



#Positional Arguments - arguments passed to a function based on their position/order.
#The first argument goes to the first parameter, the second argument goes to the second parameter, and so on.

def display(name,email,pwd):
    print("Name: ",name)
    print("Email: ",email)
    print("Password: ",pwd)
    
display('lohitha','lohitha@gmail.com','lohitha@123')
display('lohitha@gmail.com','lohitha@123','lohitha')
display('lohitha@123','lohitha','lohitha@gmail.com')


#Keyword Arguments - arguments passed to a function using the parameter name.
#Instead of depending on the position, we specify which parameter should receive each value.
def display(name,email,pwd):
    print("Name: ",name)
    print("Email: ",email)
    print("Password: ",pwd)
    
display(name = 'lohitha', email= 'lohitha@gmail.com', pwd = 'lohitha@123')
display(email = 'lohitha@gmail.com', pwd= 'lohitha@123', name = 'lohitha')    
display(pwd = 'lohitha@123', email = 'lohitha@gmail.com',name = 'lohitha') 


#Default Arguments - A default argument is a parameter that already has a default value.
If the user does not provide a value for that parameter, Python automatically uses the default value.  

def display(name,email,pwd=None):
    print("Name: ",name)
    print("Email: ",email)
    print("Password: ",pwd)
    
display('lohitha','lohitha@gmail.com')
display('lohitha@gmail.com','lohitha@123','lohitha')



def display(email,pwd=None,name = None):
    print("Name: ",name)
    print("Email: ",email)
    print("Password: ",pwd)
    
display(name = 'lohitha', email= 'lohitha@gmail.com')
display(email = 'lohitha@gmail.com', pwd= 'lohitha@123', name = 'lohitha')    
display(pwd = 'lohitha@123', email = 'lohitha@gmail.com') 


def greet(name='harsha'):
    print("Name: ",name)
    
greet("lohitha") 
greet()


#Variable-length Arguments - used when we don't know in advance how many arguments will be passed to a function.

def display(*name):
    print(name)
    
display("lohitha")
display("lohitha",'harsha')
display("lohitha","harsha","babitha") 

'''
#Use ** for key value pairs
def display(**name):
    print(name)
    
display(n1 = "lohitha")
display(n1 = "lohitha",n2 = 'harsha')
display(m1 = "lohitha",m2 = "harsha",m3 = "babitha")    

   