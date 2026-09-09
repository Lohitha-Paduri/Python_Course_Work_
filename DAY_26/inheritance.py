'''
#Inheritance - Acquiring properties from parent to child class, Used to reuse the code

#Single Inheritance - One child class inherits from one parent class.

class Whatsappv1:
    def message(self):
        print("You can send a message")
        
class Whatsappv2(Whatsappv1):
    def status(self):
        print("You can upload the status for 24 hours")        
        
lohitha = Whatsappv1()
lohitha.message()      

harsha = Whatsappv2()
harsha.message()
harsha.status()  



#Multilevel inheritance - inheritance happens in multiple levels, like a chain. A->B->C

class Whatsappv1:
    def message(self):
        print("You can send a message")
        
class Whatsappv2(Whatsappv1):
    def status(self):
        print("You can upload the status for 24 hours")      
        
class Whatsappv3(Whatsappv2):
    def groups(self):
        print("You can create group and speak with multiple people")          
        
lohitha = Whatsappv1()
lohitha.message()      

harsha = Whatsappv2()
harsha.message()
harsha.status()

babitha = Whatsappv3()
babitha.message()
babitha.status()
babitha.groups()



#Multiple - Many parents, single child
#Hybrid - Many childs, Single child
class Whatsappv1:
    def message(self):
        print("You can send a message")
        
class Whatsappv2(Whatsappv1):
    def status(self):
        print("You can upload the status for 24 hours")      
        
class Whatsappv3:
    def groups(self):
        print("You can create group and speak with multiple people")  
        
class Whatsappv4:
    def communities(self):
        print("You can merge multiple groups")
        
class Whatsappv5(Whatsappv2,Whatsappv3,Whatsappv4):
    def channels(self):
        print("You can message in large number of people")                        
        
lohitha = Whatsappv1()
lohitha.message()   
print()   

harsha = Whatsappv2()
harsha.message()
harsha.status()
print()

babitha = Whatsappv5()
babitha.message()
babitha.status()
babitha.groups()
babitha.communities()
babitha.channels()
print()


'''
#Hierarchical - Single parent, multiple childs

class Whatsappv1:
    def message(self):
        print("You can send a message")
        
class Whatsappv2(Whatsappv1):
    def status(self):
        print("You can upload the status for 24 hours")      
        
class Whatsappv3(Whatsappv1):
    def groups(self):
        print("You can create group and speak with multiple people")  
        
class Whatsappv4(Whatsappv1):
    def communities(self):
        print("You can merge multiple groups")
                            
        
lohitha = Whatsappv1()
lohitha.message()   
print()   

harsha = Whatsappv2()
harsha.message()
harsha.status()
print()

babitha = Whatsappv3()
babitha.message()
babitha.groups()
print()

rani = Whatsappv4()
rani.message()
rani.communities()
print()




