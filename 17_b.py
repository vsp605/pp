# Input list of tuples
tuples_list = [(6, 7), (2, 3), (7, 6), (9, 8), (10, 2), (8, 9)]

# Initialize a set to keep track of seen tuples
seen = set()
# Initialize a list to store symmetric tuples
symmetric_tuples = []

# Iterate through each tuple in the list
for tpl in tuples_list:
    # Check if the reverse of the tuple is already in the seen set
    if (tpl[1], tpl[0]) in seen:
        # Add the tuple to the symmetric tuples list
        symmetric_tuples.append(tpl)
    else:
        # Add the tuple to the seen set
        seen.add(tpl)

print("Original List:", tuples_list)
print("Symmetric Tuples:", symmetric_tuples)
