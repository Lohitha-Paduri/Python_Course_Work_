'''
u_n = input("Enter the username: ")
pswd = input("Enter the password: ")

if u_n == 'admin' and pswd == 'admin123':
    print("login successfull")
else:
    print("Invalid credentials")   


products = ["Laptop", "mouse", "keyboard", "bag", "bottle"]
s_p = input("Enter the product: ")
if s_p in products:
    print(f"{s_p} found")
else:
    print(f'{s_p} not found')   
'''

price = int(input("Enter the price: "))
if price>99:
    print("No delivery charges")
else:
    print("Original cost + delivery fee:", price+30)             