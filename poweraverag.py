from math import *

def powave(num):
    sum1=0
    for j in range(1,num+1):
        sum1=(num**-2.5 +sum1)/j
    return sum1    
x=powave(1000)
print(x)
