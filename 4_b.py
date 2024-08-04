n = int(input("Enter a number: "))
m = [2, 3, 5]
for i in m:
    while n % i == 0:
        n //= i
if n == 1:
    print("true")
else:
    print("false")
