# Step 1: Create the dictionary of students with their marks
students = {
    '2ba17cs011': {'Math': 50, 'Phy': 80, 'Chem': 65},
    '2ba17cs012': {'Math': 85, 'Phy': 75, 'Chem': 90},
    '2ba17cs013': {'Math': 95, 'Phy': 85, 'Chem': 80},
    '2ba17cs014': {'Math': 70, 'Phy': 60, 'Chem': 75},
    # Add more students as needed
}

# Step 2: Find the student who scored highest in each subject
highest_math = max(students, key=lambda x: students[x]['Math'])
highest_phy = max(students, key=lambda x: students[x]['Phy'])
highest_chem = max(students, key=lambda x: students[x]['Chem'])

print(f"Highest in Math: {highest_math} with {students[highest_math]['Math']}")
print(f"Highest in Physics: {highest_phy} with {students[highest_phy]['Phy']}")
print(f"Highest in Chemistry: {highest_chem} with {students[highest_chem]['Chem']}")

# Step 3: Convert the dictionary to a list of tuples
students_list = [
    (usn, sum(marks.values()), sum(marks.values()) / len(marks))
    for usn, marks in students.items()
]

# Print the list of tuples
print(students_list)
