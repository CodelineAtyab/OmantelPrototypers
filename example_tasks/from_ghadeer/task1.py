# Input (Step 1)
number = int (input("Enter a number: "))
limit = int (input("Upto limit: "))




# Process & Output (step 2)
count = 1

while count <= limit:
    print (f"{number} x {count} = {number * count}")
    count = count + 1



#This is now outside the loop (step 3)
print ("Exiting Application!") 
