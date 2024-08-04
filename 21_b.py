def compute_gcd(a, b):
    """
    Compute the GCD of two numbers using recursion.
    
    Args:
    a (int): First number.
    b (int): Second number.
    
    Returns:
    int: GCD of the two numbers.
    """
    if b == 0:
        return a
    else:
        return compute_gcd(b, a % b)

# Example usage with predefined values
num1 = 48
num2 = 18
print(f"The GCD of {num1} and {num2} is {compute_gcd(num1, num2)}")

# Example usage with user input
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
print(f"The GCD of {num1} and {num2} is {compute_gcd(num1, num2)}")
