username = input("Enter your name: ")
print("Welcome " + username)

duration = int(input("Enter the duration of the subscription: "))

print("""
Admiral Insurance offers the following policies :
"Car" insurance, price: £500 /year
"House" insurance, price: £1000 /year
"Mobile" insurance, price: £120 /year
""")
chosen_insurance_policy = input("Enter the type of policy you want: ")
valid_options = ["Car", "House", "Mobile"]

if chosen_insurance_policy not in valid_options:
    print("Invalid choice. Please retry!")
    exit()

if chosen_insurance_policy == "Car":
    price = 500 * duration
    print("the cost is :", price)

if chosen_insurance_policy == "House":
    price = 1000 * duration
    print("the cost is :", price)

if chosen_insurance_policy == "Mobile":
    price = 120 * duration
    print("the cost is :", price)

while True:
    print("""
    Chose between the following means of payment:
    bank transfer: 0% transaction fee
    paypal: 10% transaction fee
    credit card: 20% transaction fee
    """)
    mean_of_payment = input("Enter your mean of payment: ")
    valid_options2 = ["bank transfer", "paypal", "credit card"]

    if mean_of_payment in valid_options2:
        break
    else:
        print("Invalid option. Please try again!")

if mean_of_payment == "bank transfer":
    total_cost = price
    print("the total cost is :", total_cost)

if mean_of_payment == "paypal":
    total_cost = price + price * 0.1
    print("the total cost is :", total_cost)

if mean_of_payment == "credit card":
    total_cost = price + price * 0.2
    print("the total cost is :", total_cost)

print("Thank you " + username +
      " for choosing Admiral insurance, here is the recap of your insurance policy:")

print("You susbribed for "+chosen_insurance_policy +
      " insurance for "+str(duration)+" years.")

print("You chose to pay by " + mean_of_payment +
      ", the total cost is: £", total_cost)

print("""


""")

number_of_premiums = int(input("Enter the number of premiums you want: "))

premiums = []

for count in range(number_of_premiums):
    premium = float(input("Please enter a premium: "))
    premiums.append(premium)

print("Here, the list of premiums you entered", premiums)

sum_of_premium = sum(premiums)
print("Here, the sum of premiums you entered: ", sum_of_premium)

max_num = max(premiums)
print("The highest number is :", max_num)

average = sum(premiums)/len(premiums)
print("The average of the premiums you chose: ", average)
