import bank_account

print(bank_account.default_welcome_message)
current_balance = float(input("Please enter starting balance: "))

# call the function to deposit x pounds
current_balance = bank_account.deposit(current_balance)

# call the function to withdraw x pounds
current_balance = bank_account.withdraw(current_balance)

# call the above function (give it a name) passing it the current balance
print(bank_account.comment_on_balance(current_balance))
