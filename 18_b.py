def MIRROR_CHARACTER(s):
    # Find the mirror characters of the string
    mirrored_string = s[::-1]
    return mirrored_string

# Example usage
input_string = "hello"
mirrored = MIRROR_CHARACTER(input_string)
print(f"Original string: {input_string}")
print(f"Mirrored string: {mirrored}")
