'''
#super() is used in a child class to access the parent class's methods or constructor.
class whatsappv1:
    def status(self):
        print("You can upload the status for 24hrs")

class whatsappv2(whatsappv1):
    def status(self):
        super().status()
        print("You can add music and react")
        
a = whatsappv1()
a.status()
print()     

b = whatsappv2()
b.status()           

'''
class whatsappv1:
    def status(self):
        print("You can upload the status for 24hrs")

class whatsappv2:
    def status(self):
        print("You can add music and react")
        
class whatsappv3(whatsappv1,whatsappv2):
    def status(self):
        whatsappv1.status(self)
        whatsappv2.status(self)
        print("You can add to the cross platforms")         
        
a = whatsappv1()
a.status()
print()     

b = whatsappv2()
b.status() 
print()

c = whatsappv3()
c.status()        
