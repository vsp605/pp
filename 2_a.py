n=int(input("Enteer a no:"))
m=int(input("Enteer a no:"))
ch=input("Enter a choice A for arthematic  B for binary ")
if ch=='A':
   c=input("+ for add \n - for sub\n * for mul\n/for div")
   if c=='+':
        print(m+n)
   elif c=='-':
       print(m-n)
   elif c=='*':
       print(m*n)
   elif c=='/':
       print(m/n)
elif ch=='B':
    cc=input("Enter choice AND\nNOR\nEXOR:")
    if cc=='AND':
        print(bin(m&n))
    elif cc=='OR':
        print(bin(m|n))
    elif cc=='EXOR':
        print(bin(~m),bin(~n))


       
        