Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 23:09:28) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = 10
\
>>> b=17.5
>>> c = "lohitha"
>>> print(a,b,c)
10 17.5 lohitha
>>> print('a=',a)
a= 10
>>> #we are getting space becuase when we seperate the things with comma then we will get space
>>> print("a=",a,'b=',b,'c=',c)
a= 10 b= 17.5 c= lohitha
>>> print("a=",a,"b=",b,"c=",c,sep='')
a=10b=17.5c=lohitha
>>> #sep removes all the spaces
>>> print("a=",a,"b=",b,"c=",c,sep='\n')
a=
10
b=
17.5
c=
lohitha
>>> #\n is for new line
>>> print("a=",a,"b=",b,"c=",c,sep='\t')
a=	10	b=	17.5	c=	lohitha
>>> #\t is for tab space
>>> print("a=",a,"b=",b,"c=",c,sep='\t',end = '\n\n')
a=	10	b=	17.5	c=	lohitha

>>> #end works on last part
>>> print("a=",a,"b=",b,"c=",c,sep='',end = '@')
a=10b=17.5c=lohitha@
>>> #this is all comma seperation
>>> #next one f-string
>>> print(f"a={a} b={b} c={c}")
a=10 b=17.5 c=lohitha
>>> #In f-string there is no comma's
>>> print('a = %d b=%f c=%s' %(a,b,c))
a = 10 b=17.500000 c=lohitha
>>> print('a={} b ={} c={}'.format(a,b,c))
a=10 b =17.5 c=lohitha
>>> print('a={} b ={} c={}'.format(c,a,b))
a=lohitha b =10 c=17.5
>>> print('a={0} b ={1} c={2}'.format(b,c,a))
a=17.5 b =lohitha c=10
>>> print('a={2} b ={0} c={1}'.format(a,b,c))
a=lohitha b =10 c=17.5
>>> 
