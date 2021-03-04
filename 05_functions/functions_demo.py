# This is an example of copy-pasting (or repeating) code which can be solved better by functions
# print("Hi, the class of M2 students!")
# print("Hope you are having fun learning Python!")

# print("Hi, the class of M2 students!")
# print("Hope you are having fun learning Python!")

# print("Hi, the class of M2 students!")
# print("Hope you are having fun learning Python!")

# print("Hi, the class of M2 students!")
# print("Hope you are having fun learning Python!")

# Function definition - we are DEFINING a function
# This function RETURNS (output) nothing (void function)
def greeting():
    print("Hi, the class of U2 students!")
    print("Hope you are having fun learning Python!")


# Function definition - we are DEFINING a function
# This function RETURNS (outputs) a value which is a string
def greeting_with_return():
    return "This function is returning a string."


# Below, we are CALLING (using) a function
greeting()
greeting()
greeting()

# Below we are CALLING
print(greeting_with_return())


# Function definition that returns an Integer (Functions can return any data type value, e.g. string, boolean, int, float)
def large_integer():
    return 1022343


# Example of using the RETURN value (output) of a function call
some_number = large_integer() + 1
print(some_number)


# Definition of a function that has a PARAMETER (input)
def personal_greeting(name):
    print("Hi,", name)
    print("Hope you are having fun learning Python!")


# Examples of calling a function with a parameter.
# Below, "Jimmy", 12, "Camille" are ARGUMENTS
personal_greeting("Jimmy")
personal_greeting(12)
personal_greeting("Camille")


# Definition of a function that has both, parameter (input) and a return value (output)
def personal_greeting_with_return(name):
    return "Hello, " + str(name)


# We are calling a function that has an argument "Mayla", for the name parameter and it returns a string
print(personal_greeting_with_return("Mayla"))


# Function terminology
# INPUT = PARAMETER (When defining a function)
# OUTPUT = RETURN
# USING a function = 'CALLING' a function
# When CALLING a function, the VALUE of a PARAMETER = "ARGUMENT"


# Example of a function with arbitrary ARGUMENTS
# In this example, balances is an automatic list which will contain
# items that are passed as arguments
def display_balances_args(*balances, account_name):
    for balance in balances:
        print(balance)


display_balances_args(12, 34, 33, 67, 56, account_name="Jimmy Madon")


# Example of a function with a simple list argument
# In this example, balances is an automatic list which will contain
# items that are passed as arguments
def display_balances_list(balances, account_name, security_password, welcome_message="Hello user"):
    print(account_name)
    print(security_password)
    for balance in balances:
        print(balance)


balances_list = [12, 34, 33, 67, 56]
display_balances_list(balances_list, "J1mmy", "Jimmy Madon", "Hello Jimmy")
