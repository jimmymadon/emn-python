def duration_policy():
    while True:
        try:
            duration_policy = int(
                input("Please insert the duration of your insurance policy (in years): "))
            return duration_policy
        except ValueError:
            print("Please only insert a number of year")
            continue
        break
