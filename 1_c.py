s = input("Enter a string:")
if s.isalpha():
    print("String contains only alphabets:")
    if s.isupper():
        print("String in upper case:")
    else:
        print("String in lower case:")
elif s.isdigit():
    print("String contains digits:")
    sum = 0
    for i in s:
        sum += int(i)
    print(sum)
elif s.isalnum():
    print("String contains both numbers and characters:")
else:
    print("String contains special characters:")
    sum1 = 0
    for i in s:
        if not i.isalpha() and not i.isdigit():
            sum1 += 1
    print(sum1)  