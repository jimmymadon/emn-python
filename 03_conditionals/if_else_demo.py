marks = int(input("Enter your marks: "))

# print(marks >= 70) # Just to check the output of the if condition

# Example of the number line I used in my head:
# -infinity, 0, 50, 70, 100, +infinity

if marks > 100 or marks < 0:
    print("Invalid Marks!")
elif marks >= 70:
    print("Distinction!")
elif marks >= 50:
    print("Pass!")
else:
    print("Fail!")
