# Step 1: Hardcoded multiplication table
 
#number = 2
#limit = 3
 
#for i in range(1, limit + 1):
    #print(f"{number} x {i} = {number * i}")

# Step 2: Accept user input
 
number = int(input("Enter a number: "))
limit = int(input("Enter the limit: "))
 
for i in range(1, limit + 1):
    print(f"{number} x {i} = {number * i}")

# Step 3: Input validation
 
try:
    number = int(input("Enter a number: "))
    limit = int(input("Enter the limit: "))
 
    if limit <= 0:
        print("Limit must be greater than 0")
    else:
        for i in range(1, limit + 1):
            print(f"{number} x {i} = {number * i}")
 
except ValueError:
    print("Please enter valid integers.") 

# Step 4: Refactor into function
 
def print_table(number, limit):
    for i in range(1, limit + 1):
        print(f"{number} x {i} = {number * i}")
 
try:
    number = int(input("Enter a number: "))
    limit = int(input("Enter the limit: "))
 
    if limit <= 0:
        print("Limit must be greater than 0")
    else:
        print_table(number, limit)
 
except ValueError:
    print("Please enter valid integers.")
    
    