# define a function to deposit a given amount to the balance
def deposit(balance):
    deposited_amount = float(input("Enter amount to be deposited: "))
    updated_balance = balance + deposited_amount
    print("Amount deposited: ", deposited_amount)
    print("Updated_balance: ", updated_balance)
    return updated_balance


# define a function to withdraw a given amount from the balance
def withdraw(balance):
    withdrawn_amount = float(input("Enter amount to be withdrawn: "))
    updated_balance = balance - withdrawn_amount
    print("Amount withdrawn: ", withdrawn_amount)
    print("Updated_balance: ", updated_balance)
    return updated_balance


# define a function that takes the balance and it returns a string:
# if balance > 10, return "You are rich!"
# if balance < 10, return "Work harder!"
def comment_on_balance(balance):
    if balance > 10:
        return "You are rich!"
    else:
        return "Work harder!"


current_balance = float(input("Please enter starting balance: "))

# call the function to deposit x pounds
current_balance = deposit(current_balance)

# call the function to withdraw x pounds
current_balance = withdraw(current_balance)

# call the above function (give it a name) passing it the current balance
print(comment_on_balance(current_balance))
