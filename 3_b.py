from math import *
a=int(input("Enter ano:"))
b=int(input("Enter ano:"))
if a%2==0 and b%2==0:
    if a!=b:
        if(a>b):
            print(a)
        else:
            print(b)
elif a%2!=0 and b%2!=0:
    if a!=b:
       a,b=b,a
       print("a=",a,"b=",b)           
else:
    print(factorial(a))
    print(factorial(b))

             