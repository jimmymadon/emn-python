number1 = float(input("Enter the first number: "))
print("Your first number is:", number1, "and the type is", type(number1))

number2 = float(input("Enter the second number: "))
print("Your second number is:", number2, "and the type is", type(number1))

print("""
Menu:
add: Addition
subtract: Subtraction
multiply: Multiplication
divide: Division
""")
chosen_operation = input("Enter a number from the above menu: ")

valid_options = ["add", "subtract", "multiply", "divide"]

if chosen_operation not in valid_options:
    print("Invalid Option. Please retry!")
    exit()
if chosen_operation == "add":
    addition_result = number1 + number2
    print("Addition Result: " + str(addition_result))
if chosen_operation == "subtract":
    subtraction_result = number1 - number2
    print("Subtraction Result: " + str(subtraction_result))
if chosen_operation == "multiply":
    multiplication_result = number1 * number2
    print("Multiplication Result: ", multiplication_result)
if chosen_operation == "divide":
    division_result = number1 / number2
    print("Division Result: ", division_result)
