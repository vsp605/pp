main_string = input("Enter the main string: ")
substring = input("Enter the substring to check: ")
new_string = input("Enter the new string to replace with: ")
if substring in main_string:
    modified_string = main_string.replace(substring, new_string)
else:
    mid_index = len(main_string) // 2
    modified_string = main_string[:mid_index] + substring + main_string[mid_index:]
print("Modified string:", modified_string)
