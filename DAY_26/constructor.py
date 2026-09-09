#Constructor - special method, called automatically whenever we create a object

class Instagram:
    def __init__(self,username,password):
        self.username = username
        self.password = password
        print(f"Welcome to the Instagram {self.username}!")

lohitha = Instagram('lohitha','1234567') 
harsha = Instagram('Harsha', '8798754639')       
        
        