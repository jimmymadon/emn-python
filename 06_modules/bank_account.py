default_welcome_message = "Hello dear bank user"


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
