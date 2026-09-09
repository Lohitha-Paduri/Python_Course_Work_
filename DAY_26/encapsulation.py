'''
public ->inclass, child class, outside 
private -> inclass __
protected ->inclass, child class, outside (not recommended) _

'''

class Instagram:
    def __init__(self,username,password):
        self.username = username
        self.__password = password
        self._post = []
        
    def getpassword(self):
        return self.__password   
    
     
    def setpassword(self,password):
        self.__password = password
        
    
    @property
    def getpost(self):
        return self._post
    
    @getpost.setter
    def getpost(self,newpost):
        self._post.append(newpost)
    
lohitha = Instagram('Lohitha','1234556')

print(lohitha.username)
print(lohitha.getpassword())
print(lohitha.getpost)

lohitha.username = 'Lohitha_123'
print(lohitha.username)

lohitha.setpassword('Lohitha@123')
print(lohitha.getpassword())


lohitha.getpost = 'Python Intro'
lohitha.getpost = 'Sequential Data types'
lohitha.getpost = 'Fucntions'
lohitha.getpost = 'Modules'
print(lohitha.getpost)
