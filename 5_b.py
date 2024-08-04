product = 1
while True:
    number = int(input("Enter a number (press -1 to stop): "))
    if number == -1:
        break
    product *= number
print(f"The product of all entered numbers is: ",product)
