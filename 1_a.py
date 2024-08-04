import cmath 
a=int(input("Enter a value:"))
b=int(input("Enter a value:"))
c=int(input("Enter a value:"))
d=b*b-(4*a*c)
if(d==0):
    print("Roots sre equal:")
    root=-b/2*a
    print(root)
elif(d>0):
    print("Roots are real ")
    root1=-b+cmath.sqrt(d)/2*a
    root2=-b-cmath.sqrt(d)/2*a
    print(root1,root2)
else:
    print("Roots are imaginary:")
    root3=-b+cmath.sqrt(d)/2*a
    root4=-b-cmath.sqrt(d)/2*a
    print(complex(root3),complex(root4))
    