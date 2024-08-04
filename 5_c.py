from math import *
# Convert angle to radians
ang = 30
x = radians(ang)
print("Angle in radians:", x)
# Get the number of terms for the series expansion
n = int(input("Enter the number of terms: "))
# Initialize the cosine approximation
cos_app = 0
# Compute the cosine using the Taylor series expansion
for i in range(n):
    term = ((-1)**i * x**(2*i)) / factorial(2*i)
    cos_app += term
    print(f"Term {i+1}: {term}, Current cosine approximation: {cos_app}")
print("Final cosine approximation:", cos_app)
