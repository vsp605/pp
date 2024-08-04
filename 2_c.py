n=int(input("Enter a n:"))
f1=0
f2=1
print(f1,end="->")
print(f2,end="->")
c=2
while c<n:
    f3=f1+f2
    print(f3,end="->")
    f1=f2
    f2=f3
    c=c+1