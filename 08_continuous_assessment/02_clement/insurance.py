userName = str(input("Please write your name :"))
print("Welcome to our insurance app", userName)


def choices():
    print("""
    Choose what do you want to do :
    1- Calculate the total cost of the insurance
    2- Calculate the sum, average, and the maximum of your insurance premium
    """)
    choice = int(input("please enter what do you want to do :"))

    if choice == 1:
        print("""
        Choice of your insurance policy:

        Car insurance, premium is 500€ per year
        Home Insurance, premium  is 1000€ per year
        Mobile Insurance, premium is 10€ per month

        """)

        """ Input of the different elements """

        insurancePolicy = input(
            str("please right: carInsurance, homeInsurance, mobileInsurance : "))
        if insurancePolicy == "mobileInsurance":
            duration = int(
                input("Please enter the number of month(s) you want the insurance : "))
        else:
            duration = int(
                input("Please enter the number of year(s) you want the insurance : "))

        print("""
        The fee(s) related to the payment type are:
        - Bank transfer: 0% fee
        - Paypal: 10% of the base premium
        - Credit card: 20% of the base premium
        """)

        paymentType = input("""
        PLEASE RIGHT (you can find the fees related above)

        - "bank" for a bank transfer
        - "payPal" for a payment with Paypal
        - "credit card" for a payment with a credit car :

        -->  """)

        """ Dictionarie of the insurancePolicy and the premium """

        insuranceDictionarie = {"carInsurance": 500,
                                "homeInsurance": 100, "mobileInsurance": 10}
        paymentDictionarie = {"bank": 0, "payPal": 0.1, "credit card": 0.2}

        def totalCost():
            if insurancePolicy == "mobileInsurance":
                premiumPrice = insuranceDictionarie[insurancePolicy]*duration
                paymentFee = paymentDictionarie[paymentType] * \
                    insuranceDictionarie[insurancePolicy]
                total = premiumPrice+(paymentFee*duration)
                print("your premium for ", duration,
                      " month(s) is ", premiumPrice, "€")
                print("Your transaction fee(s) equal to ",
                      paymentFee, "€ per month")
                print("The total cost of your insurance will be ",
                      total, "€ for the", duration, "month(s)")
                menu = input(
                    "Do you want to return to the menu ? Y for yes N for no : ")
                if menu == "Y":
                    choices()
                else:
                    print("Thank you")

            elif insurancePolicy == "carInsurance":
                premiumPrice = insuranceDictionarie[insurancePolicy]*duration
                paymentFee = paymentDictionarie[paymentType] * \
                    insuranceDictionarie[insurancePolicy]
                total = premiumPrice+(paymentFee*duration)
                print("your premium for ", duration,
                      " year(s) is ", premiumPrice, "€")
                print("Your transaction fee(s) equal to ",
                      paymentFee, "€ per year")
                print("The total cost of your insurance will be ",
                      total, "€ for the", duration, "year(s)")
                menu = input(
                    "Do you want to return to the menu ? Y for yes N for no : ")
                if menu == "Y":
                    choices()
                else:
                    print("Thank you")

            elif insurancePolicy == "homeInsurance":
                premiumPrice = insuranceDictionarie[insurancePolicy]*duration
                paymentFee = paymentDictionarie[paymentType] * \
                    insuranceDictionarie[insurancePolicy]
                total = premiumPrice+(paymentFee*duration)
                print("your premium for ", duration,
                      " year(s) is ", premiumPrice, "€")
                print("Your transaction fee(s) equal to ",
                      paymentFee, "€ per year")
                print("The total cost of your insurance will be ",
                      total, "€ for the", duration, "year(s)")
                menu = input(
                    "Do you want to return to the menu ? Y for yes N for no : ")
                if menu == "Y":
                    choices()
                else:
                    print("Thank you")

        totalCost()

    if choice == 2:
        premiumComparaison = []
        premiumNumber = int(
            input("For how many premium you want the sum/average/maximum : "))
        for premiumUser in range(0, premiumNumber):
            premiumChoice = float(input("Enter the premium : "))

            premiumComparaison.append(premiumChoice)

        print("You choose to have the sum, average and maximum of : ",
              premiumComparaison)

        premiumSum = sum(premiumComparaison)
        print("The sum of your premium is ", premiumSum, "€")

        premiumAverage = premiumSum / len(premiumComparaison)
        print("The average of the premium is ", premiumAverage, "€")

        premiumMax = max(premiumComparaison)
        print("The maximum premium is ", premiumMax, "€")

        menu = input(
            "Do you want to return to the menu ? Y for yes N for no : ")
        if menu == "Y":
            choices()
        else:
            print("Thank you")

    else:
        menu = input(
            "Do you want to return to the menu ? Y for yes N for no : ")
        if menu == "Y":
            choices()
        else:
            print("Thank you")


choices()
