'''
1. You use an abstract class
Python provides ABC (Abstract Base Class).

2. An abstract method must be implemented by the child class

3. You cannot create an object of an abstract class
lohitha = payment() is not allowed

4. If a child doesn't implement all abstract methods, it also remains abstract

Eg: Suppose your parent has two abstract methods:
Every child must implement BOTH paymentprocess() and paymentstatus()
Suppose HDFC only implements one: HDFC is still abstract, So this won't work:
Error, because HDFC hasn't fulfilled the complete contract of the parent.

If HDFC implements both paymentprocess() and paymentstatus() it works
Because HDFC has implemented all abstract methods.

Abstract parent:
"I define what the child MUST do."

Child:
"I implement what the parent told me to do."

'''


from abc import ABC, abstractmethod

class payment(ABC):
    def source(self):
        print("Scanner/upiid/Mobile Number")
    def amount(self):
        print("Enter the amount")
    def bank(self):
        print("Select the bank")    
    def pin(self):
        print("Select the pin")
        
    @abstractmethod    
    def paymentprocess(self):
        pass
    def paymentstatus(self):
        print("Payment is Success/Fail")  
        
class HDFC(payment):
    def paymentprocess(self):
        print("Payment is processed from HDFC bank")
        
class ICICI(payment):
    def paymentprocess(self):
            print("Payment is processed from ICIC bank")    
            
class SBI(payment):
    def paymentprocess(self):
            print("Payment is processed from SBI bank")  
            
class Canara(payment):
    def paymentprocess(self):
            print("Payment is processed from Canara bank")                            
         
                  
harsha = HDFC() 
harsha.source()   
harsha.amount()           
harsha.bank()       
harsha.pin()       
harsha.paymentprocess()       
harsha.paymentstatus() 
print()      
                
Lohitha = ICICI() 
Lohitha.source()   
Lohitha.amount()           
Lohitha.bank()       
Lohitha.pin()       
Lohitha.paymentprocess()       
Lohitha.paymentstatus()
print()   

Jenni = SBI()    
Jenni.source()   
Jenni.amount()           
Jenni.bank()       
Jenni.pin()       
Jenni.paymentprocess()       
Jenni.paymentstatus() 
print()         

Karthik = SBI()    
Karthik.source()   
Karthik.amount()           
Karthik.bank()       
Karthik.pin()       
Karthik.paymentprocess()       
Karthik.paymentstatus() 
print()         