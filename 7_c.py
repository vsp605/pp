for i in range(5):
    for j in range(5 - i - 1):
        print(" ", end=" ")
    value = 1
    for j in range(i + 1):
        print(value, end=" ")
        value = value * (i - j) // (j + 1)
    print()
