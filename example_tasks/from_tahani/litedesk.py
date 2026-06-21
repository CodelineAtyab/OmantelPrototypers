number = int(input("Enter a number: "))
limit = int(input("Enter a limit: "))
 
current = 1
while current <= limit:
    result = number * current
    print(f"{number} x {current} = {result}")
    current = current + 1
 