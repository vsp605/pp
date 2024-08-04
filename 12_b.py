# Read dimensions of the first matrix
rows_A = int(input("Enter the number of rows for the first matrix: "))
cols_A = int(input("Enter the number of columns for the first matrix: "))

# Initialize the first matrix
A = []
print("Enter the first matrix:")
for i in range(rows_A):
    row = list(map(int, input().split()))
    A.append(row)

# Read dimensions of the second matrix
rows_B = int(input("Enter the number of rows for the second matrix: "))
cols_B = int(input("Enter the number of columns for the second matrix: "))

# Initialize the second matrix
B = []
print("Enter the second matrix:")
for i in range(rows_B):
    row = list(map(int, input().split()))
    B.append(row)

# Ensure the matrices can be multiplied
if cols_A != rows_B:
    print("Matrices cannot be multiplied due to incompatible dimensions.")
else:
    # Initialize the result matrix with zeros
    result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]

    # Perform matrix multiplication
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]

    # Display the result
    print("Resultant matrix after multiplication:")
    for row in result:
        print(row)
