'''
#import the entire logic module into your Python program.
import logic

logic.add(10,20)
logic.sub(10,20)
logic.mul(10,20)
logic.div(10,20)
logic.mod(10,20)
logic.exp(10,20)


#mport the logic module and give it a shorter name (alias) lg
import logic as lg

lg.add(50,40)
lg.sub(50,40)
lg.mul(50,40)
lg.div(50,40)
lg.mod(50,40)
lg.exp(50,40)


#import only the specific functions add, mul, and exp from the logic module.
from logic import add,mul,exp

add(12,23)
mul(23,34)
exp(5,10)

'''
#to import everything from the logic module

from logic import *
add(10,20)
sub(10,20)
mul(10,20)
div(10,20)
mod(10,20)
exp(10,20)