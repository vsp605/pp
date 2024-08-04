N = int(input("Enter the starting value (N): "))
M = int(input("Enter the ending value (M): "))
primes = []
for i in range(N, M + 1):
    if i > 1:
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                break
        else:
            primes.append(i)
print("Prime numbers between", N, "and", M, "are:", ' '.join(map(str, primes)))
