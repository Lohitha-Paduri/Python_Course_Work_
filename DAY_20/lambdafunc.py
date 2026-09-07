'''
A lambda function is an anonymous (nameless), one-line function in Python that is used to perform a simple operation.
var = lambda arguments: expression


wish = lambda name: f"Welcome to the course, {name}"
print(wish("lohitha"))
print(wish("usha"))


gst = lambda price: price+price*0.18
print(gst(1000))
print(gst(234))


avg = lambda a,b,c : (a+b+c)/3
print(avg(1,2,3))
print(avg(7,34, 54))


iseven = lambda n: "Even" if n%2==0 else "Odd"
print(iseven(40))
print(iseven(79))


largest = lambda a,b,c: a if a>b and a>c else (b if b>c else c)
print(largest(10,20,45))
print(largest(89, 76, 98))


isvowel = lambda s: "Vowel" if s in "aeiouAEIOU" else "consonant"
print(isvowel("A"))
print(isvowel("b"))
print(isvowel("e"))
print(isvowel("D"))


l = [1,2,3,4,5]
update = list(map(lambda i : i+10,l))
print(update)


t = (23, 34, 45, 56)
discount = list(map(lambda i:i-i*0.3,t ))
print(discount)


l = [1,2,3,4,5]
update = list(filter(lambda i: i%2!=0,l))
print(update)


t = (9788, 234, 4535, 232, 4566)
update = tuple(filter(lambda i: i>1000,t))
print(update)


l= ['lohitha@codegnan.com','lohitha@yahoo.com','lohitha@outloock.com']
result = list(map(lambda i:i.split('@')[-1],l))
print(result)


l= ['lohitha@codegnan.com','lohitha@yahoo.com','lohitha@outloock.com']
result = list(map(lambda i:i.split('@')[-1].split('.')[0],l))
print(result)


#reduce() is used to take many values and combine them into one value.
from functools import reduce
l = [4,5,23,56,234]
result = reduce(lambda sum,i: sum+i,l)
print(result)

result1 = reduce(lambda product,i : product*i,l)
print(result1)


seats = {'s1':True,
         's2':False,
         's3':False,
         's4':False,
         's5':True,
         's6':True
         }
result = list(filter(lambda i:seats[i]!=True,seats))
print(result)


products = {
    'eggs':40,
    'rice':100,
    'butter':50,
    'salt':30,
    'sugar':45 
}
result = list(filter(lambda i: products[i]>50,products))
print(result)


'''
products = {
    'eggs':40,
    'rice':100,
    'butter':50,
    'salt':30,
    'sugar':45 
}

print(dict(sorted(products.items())))
print(dict(sorted(products.items(),key = lambda i:i[1])))
print(dict(sorted(products.items(),key = lambda i:i[1],reverse = True)))



