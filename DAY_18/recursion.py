'''
def func_name(arg):
    if base:
        return
    func_name(up ) 
  
func_name(par)  


def display(n):
    if n==11:
        return
    print(n)
    display(n+1)
    
display(1)  


def display(n):
    if n==0:
        return
    print(n)
    display(n-1)
    
display(10)    
'''

def display(s,n):
    if n==len(s):
        return
    print(s[n])
    display(s,n+1)
   
display("python",0)       
