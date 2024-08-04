# Initialize an empty list to represent the stack
stack = []

# Input the number of elements to push onto the stack
n = int(input("Enter the number of elements to push: "))

# Push elements onto the stack
for i in range(n):
    element = int(input("Enter an element: "))
    stack.append(element)

# Display the stack after pushing elements
print("Stack after pushing elements:", stack)

# Peek at the top element of the stack
if len(stack) > 0:
    print("Top element:", stack[-1])
else:
    print("Stack is empty")

# Pop an element from the stack
if len(stack) > 0:
    popped_element = stack.pop()
    print("Popping element:", popped_element)
else:
    print("Stack is empty")

# Display the stack after popping an element
print("Stack after popping an element:", stack)

# Check if the stack is empty
if len(stack) == 0:
    print("Stack is empty")
else:
    print("Stack is not empty")

# Display the size of the stack
print("Size of stack:", len(stack))
