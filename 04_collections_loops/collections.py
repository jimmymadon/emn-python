# Below four lines show 3 disconnected individual variables.
# Hence, for related data, we use Collections (Lists, Tuples, Sets, Dictionaries)
# bankBalance1 = 10.00
# bankBalance2 = 503.87
# bankBalance98 = 11001.90
# print(bankBalance1, bankBalance2, bankBalance98)

# Below we create a list
print("*** Creating a list with 4 elements ***")
bank_balances = [10.00, 503.87, 11001.90, 1000.00]
print(bank_balances)
print()

# Accessing individual items of a list using their index
print("*** Accessing items of our list ***")
print("Second item (Index 1):", bank_balances[1])
print("First item: (Index 0):", bank_balances[0])
print("Fourth item: (Index 3):", bank_balances[3])
print()

# Inserting items to the END of the list using the append() function
print("*** Appending items the END of our list ***")
bank_balances.append(965.00)
bank_balances.append(987.00)
print("After appending two items:", bank_balances)
print()

# Finding the size of a list
size_of_bank_balances = len(bank_balances)
print("Size of list:", size_of_bank_balances)
print()

# Accessing the LAST item of a list
# print(bank_balances[4])
# print(bank_balances[-1])
# print(bank_balances[size_of_bank_balances-1])

# Below lines show that lists can contain any type of items
print("Type of bank_balances is:", type(bank_balances))
first_item = bank_balances[0]
print("Type of the first item is:", type(first_item))
print()

# You can edit individual items by reassigning new values to them
# bank_balances[1] = 502.87
# print(bank_balances[1])

# Inserting items to the middle of the list
print("*** Inserting an item 1000 at index 2 (third element) ***")
print("Before:", bank_balances)
bank_balances.insert(2, 1000)
print("After:", bank_balances)
print()

# Create another list
bank_balances2 = [35, 98.79, 23.40]
print("*** Attaching bank_balance2 to bank_balances ***")
bank_balances.extend(bank_balances2)
print(bank_balances)

# Deleting items from a list
print("*** Deleting item at index 2 (third item) from the list ***")
bank_balances.pop(2)
print(bank_balances)
