from math import *
ang=30
x=radians(ang)
print(x)
n=int(input("Enter a term:"))
sin_app=0
for i in range(n):
    term=((-1)**i*x**(2*i+1))/factorial(2*i+1)
    for i in term:
        sin_app+=float(i)
        print(sin_app)
        
    
    