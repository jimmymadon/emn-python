def user_enter_premiums():
    print()
    while True:
        try:
            number_of_policies = int(
                input("How many Insurance Premiums do you want to calculate? (Enter a number) "))
        except ValueError:
            print("Invalid option, please try again")
            continue

        premiums = []
        for number_of_policies in range(number_of_policies):
            while True:
                try:
                    premium = float(
                        input("Please insert your Insurance Premium : ",))
                    premiums.append(premium)
                except ValueError:
                    print("Invalid option, please try again")
                    continue
                break

        result = 0
        largest = 0
        for premium in premiums:
            result = result + premium
            if largest < premium:
                largest = premium

        average = result/len(premiums)

        print()
        print("The sum of all your premiums is:", result, "pounds")
        print("The average of all your premiums is:", average, "pounds")
        print("Your largest premium is:", largest, "pounds")
        print()
        break
