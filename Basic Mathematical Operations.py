# Taking input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
#mathematical operations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
# Handling division
if num2 != 0:
    division = num1 / num2
else:
    division = "undefined (division by zero)"
#results
print(f"Addition: = {addition}")
print(f"Subtraction: = {subtraction}")
print(f"Multiplication: = {multiplication}")
print(f"Division: = {division}")