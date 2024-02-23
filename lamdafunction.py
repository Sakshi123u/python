# Define lambda functions for different arithmetic operations
add = lambda x, y: x + y
subtract = lambda x, y: x - y
multiply = lambda x, y: x * y
divide = lambda x, y: x / y
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("Addition of two numbers is:")
print(f"{num1} + {num2} =",add(num1,num2))
print("Substraction of two numbers is:")
print(f"{num1} - {num2} =",subtract(num1,num2))
print("Multiplication of two numbers is :")
print(f"{num1} * {num2} =",multiply(num1,num2))
print("Division of two numbers is :")
print(f"{num1} / {num2} =",divide(num1,num2))



  
