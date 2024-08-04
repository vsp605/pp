# Input lists
list1 = [10, 10, 0, 0, 10]
list2 = [10, 10, 10, 0, 0]

# Check if lengths are equal
if len(list1) != len(list2):
    print(False)
else:
    # Concatenate list1 with itself
    concatenated_list = list1 + list1
    # Initialize a flag
    circularly_identical = False
    # Check for sublist
    for i in range(len(list1)):
        if concatenated_list[i:i+len(list2)] == list2:
            circularly_identical = True
            break
    print(circularly_identical)
