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


import tkinter as tk
from tkinter import messagebox

# Step 4 (your function kept)
def print_table(number, limit):
    output.delete("1.0", tk.END)  # clear old results
    for i in range(1, limit + 1):
        output.insert(tk.END, f"{number} x {i} = {number * i}\n")

# Button action (handles input + validation)
def handle_input():
    try:
        number = int(entry_number.get())
        limit = int(entry_limit.get())

        if limit <= 0:
            messagebox.showerror("Error", "Limit must be greater than 0")
        else:
            print_table(number, limit)

    except ValueError:
        messagebox.showerror("Error", "Please enter valid integers")

# ---------------- GUI Design ---------------- #

root = tk.Tk()
root.title("Multiplication Table")
root.geometry("300x350")

# Input fields
tk.Label(root, text="Enter a number:").pack(pady=5)
entry_number = tk.Entry(root)
entry_number.pack()

tk.Label(root, text="Enter the limit:").pack(pady=5)
entry_limit = tk.Entry(root)
entry_limit.pack()

# Button
tk.Button(root, text="Generate Table", command=handle_input).pack(pady=10)

# Output display
output = tk.Text(root, height=12, width=30)
output.pack(pady=5)

# Run window
root.mainloop()
