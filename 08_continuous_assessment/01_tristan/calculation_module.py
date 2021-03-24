def calculate_fee(cost, payment_operation):
    payment_operation_fee = {
        1: (1, "There is no additional fee, the total yearly fee for your insurance will be: "),
        2: (1.1, "There is an additional fee with this payment type of 10%, the total yearly fee for your insurance will be: "),
        3: (1.2, "There is an additional fee with this payment type of 20%, the total yearly fee for your insurance will be: "),
    }

    new_cost = cost * payment_operation_fee[payment_operation][0]
    print(payment_operation_fee[payment_operation][1], new_cost, "pounds")


def calculate_policy_cost(duration_insurance, policy_operation):
    policy_operation_cost = {
        1: (500, "The yearly premium before payment fee for your car insurance will be: "),
        2: (1000, "The yearly premium before payment fee for your home insurance will be: "),
        3: (120, "The yearly premium before payment fee for your mobile insurance will be: "),
    }
    cost = duration_insurance * policy_operation_cost[policy_operation][0]
    print(policy_operation_cost[policy_operation][1], cost, "pounds")
    return cost
