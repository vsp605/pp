# Original list
matrix = [[4, 5, 6], [2, 4, 5], [6, 7, 5]]

# Pair elements with the rear element in each row
paired_matrix = [[[a, row[-1]] for a in row[:-1]] for row in matrix]

# Display the result
print("The list after pairing is:", paired_matrix)
