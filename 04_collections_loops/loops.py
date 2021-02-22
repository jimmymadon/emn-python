bank_balances = [10.00, 503.87, 11001.90, 1000.00]

# The below way to print all items of a list is very repetitive
# and it requires duplicate code!

# print(bank_balances[0])
# print(bank_balances[1])
# print(bank_balances[2])
# print(bank_balances[3])
# print()


# Thus, we can use a for loop to go through all items with just 2 lines!
# Line 17 will run as many times as there are items in the bank_balances list
print("*** Printing all items in a list ***")
for balance in bank_balances:
    print(balance)

print()  # Print an Empty line

# To sum all the balances together, we can create a 'counter' variable result
# This counter variable stores the sum after each iteration
# In below example, lines 27 and 28 will repeat as many times as there are items in our list
print("*** Adding all items in a list ***")
result = 0
for balance in bank_balances:
    result = result + balance
    print("Result at end of each iteration:", result)
print("Sum of all balances:", result)

average = result / len(bank_balances)
print("Average of all balances:", average)
print()

# Finding the largest number in a list
# For every iteration, we check if the current number is larger than the previous largest number
bank_balances = [10.00, 503.87, 11001.90, 1000.00]
largest = 0
for balance in bank_balances:
    if largest < balance:
        largest = balance
        print(largest)
print("Largest number:", largest)
