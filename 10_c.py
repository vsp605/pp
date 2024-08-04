units = {
    "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4,
    "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9
}
teens = {
    "ten": 10, "eleven": 11, "twelve": 12, "thirteen": 13,
    "fourteen": 14, "fifteen": 15, "sixteen": 16,
    "seventeen": 17, "eighteen": 18, "nineteen": 19
}
tens = {
    "twenty": 20, "thirty": 30, "forty": 40, "fifty": 50,
    "sixty": 60, "seventy": 70, "eighty": 80, "ninety": 90
}
multipliers = {
    "hundred": 100, "thousand": 1000, "million": 1000000
}
word = input("Enter a number in words: ")
words = word.lower().split()
number = 0
current_number = 0
for w in words:
    if w in units:
        current_number += units[w]
    elif w in teens:
        current_number += teens[w]
    elif w in tens:
        current_number += tens[w]
    elif w in multipliers:
        if current_number == 0:
            current_number = 1
        number += current_number * multipliers[w]
        current_number = 0
number += current_number
print("Numeric value:", number)
