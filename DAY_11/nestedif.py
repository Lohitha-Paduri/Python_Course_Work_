'''
fa = eval(input("Follows Account:"))
if fa:
    cf = eval(input("Close Friend List: "))
    if cf:
        print("Story Visible")
    else:
        print("Not in close friends list")
else:
    print("Follow Account First") 


registered = eval(input("Registration status: "))
entry_fee = eval(input("Payment status: "))
if registered:
    if entry_fee:
        print("Entry Confirmed")
    else:
        print("Pay the Fee")
else:
    print("Registration required") 


link_a = eval(input("Link status: "))
Per = eval(input("Permission Status: ")) 
if link_a:
    if Per:
        print("File opened successfully")
    else:
        print("Permission not granted")
else:
    print("Invalid File link")    
'''

data = {
    'lohitha':{'status':True,'python':95,'mysql':90,'flask':97},
    'harsha':{'status':True,'python':89,'mysql':56,'flask':45},
    'shiva':{'status':True,'python':90,'mysql':87,'flask':79},
    'harshitha':{'status':False,'python':None,'mysql':None,'flask':None},
    'sindhu':{'status':True,'python':34,'mysql':45,'flask':25},

}

name = input("Enter your name:")
if name in data:
    if data[name]['status']:
        sum = data[name]['python']+data[name]['mysql']+data[name]['flask']
        avg = sum/3
        print(f"Hello {name}!!!")
        print(f"Your avg score is {avg}")
        if avg>90:
            print("outstanding")
        elif avg>80:
            print("Very good")
        elif avg>70:
            print("Good")
        elif avg>30:
            print("Focus on Exams")    
        else:
            print("Failed the exam")            
        
    else:
        print(f"{name} didn't write the exam")    
else:
    print(f'{name} not found in the data')    

                                         