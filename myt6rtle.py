from turtle import *
speed(0)
shape('turtle')

def square(j):
    forward(10+j*2)
    right(90)
    forward(10+j*2)
    right(90)
    forward(j*2+10)
    
    right(90)
    forward(j+10)
    right(90)
for j in range(60):
    length=length +5
    square(length)
    right(5)
   
