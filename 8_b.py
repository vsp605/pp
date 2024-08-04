n = int(input("Enter the value of n: "))
a = 0.0
for i in range(1, n + 1):
   a += 1 / i
print(f"The sum of the series 1 + 1/2 + 1/3 + ... + 1/{n} is: {a}")
b = 0
for i in range(1, n + 1):
    term = int(i * i) / i
    b += term
print(f"The sum of the series 1/1 + 22/2 + 33/3 + ... + nn/n is: {b}")
