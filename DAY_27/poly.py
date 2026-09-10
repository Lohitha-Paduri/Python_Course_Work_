'''

Method overloading means using the same method name to perform different operations with different numbers or types of arguments.
⚠️ Python does not support traditional method overloading directly, so we usually use default arguments or *args.


Method overriding means a child class provides its own implementation of a method that is already defined in the parent class.

'''
#Method Overriding
class Hotstar:
    def __init__(self, name):
        print(f'---------Welcome to the hotstar, {name}---------')
    def auth(self):
        print("Welcome to the hotstar")
    def dashboard(self):
        print("You can see the dashboard")
    def search(self):
        print("Youc can search")  
    def history(self):
        print("You can see the history")
    def playcontrollers(self):
        print("You can resume the video") 
    def ads(self):
        print("Ads will be run")
    def quality(self):
        print("You have limited Quality")        
    def download(self):
        print("You can't download the video")   
    def devices(self):
        print("Limited Login access") 
    def access(self):
        print("Limited Access")
                  
        
        
class PremiumSubscription:
    def __init__(self, name):
        print(f'---------Welcome to the Hotstar Premium, {name}---------')
    def auth(self):
        print("Welcome to the hotstar")
    def dashboard(self):
        print("You can see the dashboard")
    def search(self):
        print("Youc can search")  
    def history(self):
        print("You can see the history")
    def playcontrollers(self):
        print("You can resume the video")
    def ads(self):
        print("No ads are played")
    def quality(self):
        print("You have HD Quality")        
    def download(self):
        print("You can download the video")   
    def devices(self):
        print("Multiple devices can login") 
    def access(self):
        print("Multiple devices can access")       
                       
                       
harsha = Hotstar("Harsha")
harsha.auth()
harsha.dashboard()
harsha.search()
harsha.history()
harsha.playcontrollers()
harsha.ads()
harsha.quality()
harsha.download()
harsha.devices()
harsha.access()
print()                       
  

varsha = PremiumSubscription("Varsha")
varsha.auth()
varsha.dashboard()
varsha.search()
varsha.history()
varsha.playcontrollers()
varsha.ads()
varsha.quality()
varsha.download()
varsha.devices()
varsha.access()
print()                       
                                