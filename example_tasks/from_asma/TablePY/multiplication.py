print("Welcome to the Multiplication Table Utility!")

def multiplication_table(number, limit):
    print(f"\n--- Multiplication Table for {number} (up to {limit}) ---")
    for i in range(1, limit + 1):
        print(f"| {number} x {i} = {number * i} |")
    print("---------------------------------------------------")

try:
    number = int(input("Enter a number: "))
    limit = int(input("Enter a limit: "))
    print()
    multiplication_table(number, limit)
except ValueError:
    print("❌ Error! You entered an invalid value. Please enter numbers only, not letters or symbols.")
