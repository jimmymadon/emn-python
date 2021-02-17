# Examples of a variable changing its data-type
myVariable = 10  # int - integer
print(myVariable)

myVariable = True  # bool - boolean
print(myVariable)

myVariable = "Hello World!"  # str - string (text)
print(myVariable)


# The below two ways can be used to create multiWord variables
account_balance = (2 * 2) + (10 / 2)
accountBalance = 20
print(account_balance)
print(accountBalance)


# The following example shows why Strict type checking (in Java)
# can be helpful
accountBalance = 20
accountBalance = "Error!"  # Changing from int to str causes issues on next line!
balance = 10 + accountBalance
print(balance)
