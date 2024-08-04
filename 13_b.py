# Sample list of tuples
sample_list = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
# Replace the last value of each tuple with 100
modified_list = [t[:-1] + (100,) for t in sample_list]
# Display the result
print("Modified list:", modified_list)
