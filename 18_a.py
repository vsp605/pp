# Input reading
n = int(input("Enter the number of integers: "))
numbers = input("Enter the integers separated by spaces: ").split()
# Convert input strings to integers
for i in range(n):
    numbers[i] = int(numbers[i])

# Creating the frequency dictionary
frequency = {}

# Populate the frequency dictionary
for num in numbers:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

# Print the frequency dictionary
print("Frequency of each number:")
print(frequency)
