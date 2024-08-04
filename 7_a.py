n = input("Enter a string: ")
if n.isalpha():
    if n.startswith('T') or n.startswith('t'):
        print("The string starts with the letter 'T'.")
    else:
        print("The string does not start with the letter 'T'.")
    cc = 0
    for char in n:
        if char.lower() not in 'aeiou' and char.isalpha():
            cc += 1
    print(f"The total number of consonants in the string is: {cc}")
elif n.isdigit():
    reversed_digits = n[::-1]
    print(f"The reversed digits are: {reversed_digits}")
else:
    print("The string contains a mix of alphabetic characters and digits or other characters.")
