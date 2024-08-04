n = int(input("Enter a number: "))
m = False
while n != 0:
    digit = n % 10
    if digit == 0:
        m = True
        break
    n = n // 10
if m==True:
    print("yes")
else:
    print("no")
