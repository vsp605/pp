n = int(input("Enter the number of elements: "))
if n < 2:
    print("Need at least 2 numbers to compute moving average.")
else:
    prev = float(input("Enter number 1: "))
    for i in range(2, n + 1):
        curr = float(input(f"Enter number {i}: "))
        avg = (prev + curr) / 2
        print(f"Moving average after {i} numbers: {avg}")
        prev = curr
