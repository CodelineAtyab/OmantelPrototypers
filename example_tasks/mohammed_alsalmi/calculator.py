#calculator
Num1 = int(input(("Enter num1: ")))
Num2 = int(input(("Enter num2: ")))
operator = input("Enter operator (+, -, *, /): ")
if operator == "+":
    Res = Num1 + Num2   
elif operator == "-":
    Res = Num1 - Num2
elif operator == "*":
    Res = Num1 * Num2
elif operator == "/": 
    Res = Num1 / Num2   
else :
    Res = "Invalid operator" 
print(Res)