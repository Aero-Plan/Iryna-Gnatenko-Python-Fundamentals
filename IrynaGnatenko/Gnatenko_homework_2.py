# Read two numbers from the user
a = float(input("Enter the first number"))
b = float(input("Enter the second number"))

# Print the results
print(f"a + b = {a+b}")
print(f"a - b = {a-b}")
print(f"a * b = {a*b}")
print(f"a ** b = {a**b}")

# Handle division by 0, print the results
if b != 0:
    print(f"a / b = {a / b}")
    print(f"a // b = {a // b}")
    print(f"a % b = {a % b}")
else:
    print("a / b = undefined (can't divide by zero)")
    print("a // b = undefined (can't divide by zero)")
    print("a % b = undefined (can't divide by zero)")
