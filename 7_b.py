n = input("Enter a number: ")
if n.startswith('0') or not n.isdigit():
    print(f"{n} is not a Duck Number.")
else:
    if '0' in n:
        print(f"{n} is a Duck Number.")
    else:
        print(f"{n} is not a Duck Number.")
