from turtle import *

shape('turtle')

def poly(num):
 degree=360/num
 for j in range(num):
    forward(26)
    
    right(degree)
    
poly(31)
