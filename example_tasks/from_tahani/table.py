# Take Input
num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
operation = input("Enter one of + - * /: ")

# Process Input
if operation == "+":
    res = num1 + num2
elif operation == "-":
    res = num1 - num2
elif operation == "*":
    res = num1 * num2
elif operation == "/":
    res = num1 / num2
else:
    print("Invlaid Operation")

# Output Result
print(res)