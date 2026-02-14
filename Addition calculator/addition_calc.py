# Addition Calculator
# Emmanuel Project

def add_numbers(num1, num2):
    return num1 + num2

# Get input from user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Calculate and display result
result = add_numbers(num1, num2)
print(f"Result: {num1} + {num2} = {result}")