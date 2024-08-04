input_string = "hello world this is a test"

words = input_string.split()
capitalized_words = []

for word in words:
    if len(word) > 1:
        capitalized_word = word[0].upper() + word[1:-1] + word[-1].upper()
    else:
        capitalized_word = word.upper()
    capitalized_words.append(capitalized_word)

result = ' '.join(capitalized_words)
print(result)  # Output: "HellO WorlD ThiS IS A TesT"
