import random

name = input("Enter name: ")
dob = input("Enter DOB[DD-MM-YY]: ")

spc = ['@','!','#','$','%','*','.',',']

pwd = name+random.choice(spc)+dob[-4:]

print("Generated Password:", pwd)

