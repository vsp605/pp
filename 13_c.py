import math
# Fixed values
C = 50
H = 30
# Input sequence
input_sequence = input("Enter the comma-separated values: ")
# Split the input sequence into a list of numbers
D_values = input_sequence.split(',')
# Calculate Q for each D and store the results
Q_values = []
for D in D_values:
    D = float(D)
    Q = math.sqrt((2 * C * D) / H)
    Q_values.append(int(round(Q)))

# Print the results as a comma-separated string
print("Output:", ','.join(map(str, Q_values)))
