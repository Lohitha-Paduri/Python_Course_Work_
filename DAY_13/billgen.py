data = {
    'sugar' : 40,
    'milk' : 80,
    'curd' : 60,
    'potato' : 30,
    'cooking oil' : 180,
    'munch' : 20,
    'rice' : 2000,
    'wheat' : 80,
    'mixed Dryfruits' : 120,
    'butter' : 50
}

for i in data:
    print(i.ljust(20),data[i])
    
prods = input("Enter the Products: ").split(",")
print("-------------------BILL----------------")
bill = 0
for j in prods:
    print(j.ljust(20), data[j])
    bill += data[j]
print("Total bill".ljust(20),bill)    
        
   
  