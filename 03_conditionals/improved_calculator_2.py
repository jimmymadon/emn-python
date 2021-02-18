number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
print("""
Menu:
add: Addition
subtract: Subtraction
multiply: Multiplication
divide: Division
""")
chosen_operation = input("Enter a number from the above menu: ")

# Change the below code to work with chosen_operation being a string!

if chosen_operation == 1:
    addition_result = number1 + number2
    print("Addition Result: " + str(addition_result))
if chosen_operation == 2:
    subtraction_result = number1 - number2
    print("Subtraction Result: " + str(subtraction_result))
if chosen_operation == 3:
    multiplication_result = number1 * number2
    print("Multiplication Result: ", multiplication_result)
if chosen_operation == 4:
    division_result = number1 / number2
    print("Division Result: ", division_result)
if chosen_operation < 1 or chosen_operation > 4:
    print("Invalid Option. Please retry!")
