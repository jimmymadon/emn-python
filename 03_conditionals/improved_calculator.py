# Taking string input and casting (converting) them to int
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
print("""
Menu:
1: Addition
2: Subtraction
3: Multiplication
4: Division
""")
chosen_operation = int(input("Enter a number from the above menu: "))

# print(chosen_operation=1) # This does not work because it is a assignment statement!
# print(chosen_operation == 1)  # This is a correct conditional statement checking for equality

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
