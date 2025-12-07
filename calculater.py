'''
GOLDEN QUESTION: 
FINAL QUESTION (Real-World Calculator Program using Input + If–Elif–Else) 
Q: Create a Python program that works as a complete calculator. 

'''
print("Calculator for basic operations.")

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Operations you can perform:\n( + , - , * , / , % , // , ** )")
user_input = input("Enter here: ")

try:
    if user_input == "+":
        result = a + b
        print("Result:", result)

    elif user_input == "-":
        result = a - b
        print("Result:", result)

    elif user_input == "*":
        result = a * b
        print("Result:", result)

    elif user_input == "/":
        result = a / b
        print("Result:", result)

    elif user_input == "%":
        result = a % b
        print("Result:", result)

    elif user_input == "//":
        result = a // b
        print("Result:", result)

    elif user_input == "**":
        result = a ** b
        print("Result:", result)

    else:
        print("Error: Invalid command!")

except ZeroDivisionError:
    print("Error: Division by zero is not allowed!")
