marks = int(input("Enter your marks: "))

# print(marks >= 70) # Just to check the output of the if condition

# Example of the number line I used in my head:
# -infinity, 0, 50, 70, 100, +infinity

# The below code uses ONE if-elif-else block
# if marks > 100 or marks < 0:
#     print("Invalid Marks!")
# elif marks >= 70:
#     print("Distinction!")
# elif marks >= 50:
#     print("Pass!")
# else:
#     print("Fail!")

# The below code uses 4 separate if blocks
if marks > 100 or marks < 0:
    print("Invalid Marks!")
if marks >= 70:
    print("Distinction!")
if marks >= 50:
    print("Pass!")
if marks >= 0:
    print("Fail!")
