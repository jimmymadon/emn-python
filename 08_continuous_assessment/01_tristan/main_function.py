from menus import policy_type_menu, payment_type_menu, end_menu
from premium_input import user_enter_premiums
from duration_input import duration_policy
from calculation_module import calculate_fee, calculate_policy_cost


def insurance_app():
    print()
    print("Welcome to our Insurance App")
    print()
    user_name = str(input("Please insert your username: "))
    print("Hello", user_name, ", please follow the instructions")

    duration_insurance = duration_policy()

    while True:
        # Display policy menu
        policy_type_menu()
        try:
            policy_operation = int(
                input("Please choose a type of Insurance from the above menu: "))
            print()
            valid_options = [1, 2, 3, 4]
        except ValueError:
            print("Invalid option, please try again!")
            continue

        if policy_operation not in valid_options:
            print("Invalid option, please try again!")
            continue

        if policy_operation == 4:
            print("Thank you for using our service, see you soon!")
            exit()

        cost = calculate_policy_cost(duration_insurance, policy_operation)
        break

    while True:
        # Display payment menu
        payment_type_menu()
        try:
            payment_operation = int(
                input("Please choose a payment type from the above menu: "))
            print()
            valid_options = [1, 2, 3, 4]
        except ValueError:
            print("Invalid option, please try again!")
            continue

        if payment_operation not in valid_options:
            print("Invalid option, please try again!")
            continue

        if payment_operation == 4:
            print("Thank you for using our service, see you soon!")
            exit()

        calculate_fee(cost, payment_operation)

        break

    # call the function end_continue to propose the user to continue the app
    end_continue()


def end_continue():
    while True:
        end_menu()
        try:
            continue_operation = int(
                input("Do you want to continue using our app? "))
            valid_options = [1, 2, 3]
        except ValueError:
            print("Invalid option, please try again")
            continue

        if continue_operation not in valid_options:
            print("Invalid option, please try again!")

        if continue_operation == 1:
            insurance_app()

        if continue_operation == 2:
            user_enter_premiums()

        if continue_operation == 3:
            print("Thank you for using our service, see you soon!")
            exit()


insurance_app()
