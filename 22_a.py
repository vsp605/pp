def replace_words(input_string, lookup_dict):
    """
    Replace words in the input_string based on the lookup_dict.
    
    Args:
    input_string (str): The string where words need to be replaced.
    lookup_dict (dict): Dictionary where keys are words to be replaced and values are replacements.
    
    Returns:
    str: The string with words replaced according to lookup_dict.
    """
    words = input_string.split()
    replaced_words = []
    
    for word in words:
        # Use the dictionary to replace words; if not found, keep the original word
        if word in lookup_dict:
            replaced_words.append(lookup_dict[word])
        else:
            print(f"Replacement for '{word}' is not possible.")
            replaced_words.append(word)
    
    return ' '.join(replaced_words)

def main():
    # Read the input string from the keyboard
    input_string = input("Enter the string to be processed: ")
    
    # Read the lookup dictionary from the keyboard
    lookup_dict = {}
    while True:
        try:
            num_entries = int(input("Enter the number of dictionary entries: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    for _ in range(num_entries):
        key = input("Enter the word to replace: ").strip()
        value = input("Enter the replacement word: ").strip()
        lookup_dict[key] = value
    
    # Replace words in the input string based on the lookup dictionary
    result = replace_words(input_string, lookup_dict)
    
    print("Processed string:")
    print(result)

if __name__ == "__main__":
    main()
