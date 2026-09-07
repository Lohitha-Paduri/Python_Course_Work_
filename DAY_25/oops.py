'''
#class Creation
class Flipkart:
    pass #creates a empty class

lohitha = Flipkart()
harsha = Flipkart()
varsha = Flipkart()
 
    
#Using Attribute types
class Flipkart:
    discount = 30
    def info(self,name,phne_no,address):
        self.name = name
        self.phne_no = phne_no
        self.address = address
        print(f'Welcome to the flipkart',self.name)
        
lohitha = Flipkart()
lohitha.info('lohitha',9380715476,'hyd')

harsha = Flipkart()
harsha.info('harsha',7465743212,"Hyd")        

'''   

#Using method types
class Flipkart:
    discount = 30
    
    @classmethod
    def updatediscount(cls):
        cls.discount =40
        print("Updated Discount", cls.discount)
        
        
    def info(self,name,phne_no,address):
        self.name = name
        self.phne_no = phne_no
        self.address = address
        print(f'Welcome to the flipkart',self.name)
        
    @staticmethod
    def banner():
        print(f'{Flipkart.discount}% discount is going on, grab the products')
        
lohitha = Flipkart()
lohitha.info('lohitha',9380715476,'hyd')
lohitha.updatediscount()
lohitha.banner()

harsha = Flipkart()
harsha.info('harsha',7465743212,"Hyd")  
harsha.updatediscount()
harsha.banner()