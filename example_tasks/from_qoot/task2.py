# gui_table.py
import tkinter as tk
from tkinter import messagebox

def calculate_table():
    # Clear previous output
    text_output.delete("1.0", tk.END)

    try:
        # Read values from the interface input boxes
        num = int(entry_num.get())
        limit = int(entry_limit.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid whole numbers only.")
        return

    if limit < 1:
        messagebox.showerror("Invalid Limit", "Limit must be 1 or greater.")
        return

    # Generate table lines
    lines = []
    for i in range(1, limit + 1):
        lines.append(f"{num} x {i} = {num * i}")

    # Inject results into the GUI textbox
    result_text = "\n".join(lines)
    text_output.insert(tk.END, result_text)

# Setup Window
root = tk.Tk()
root.title("Multiplication Utility")
root.geometry("350x450")

# Widgets
tk.Label(root, text="Enter Number:", font=("Arial", 11)).pack(pady=(20, 2))
entry_num = tk.Entry(root, font=("Arial", 11), justify="center")
entry_num.pack(pady=5)

tk.Label(root, text="Enter Limit:", font=("Arial", 11)).pack(pady=(10, 2))
entry_limit = tk.Entry(root, font=("Arial", 11), justify="center")
entry_limit.pack(pady=5)

btn_generate = tk.Button(root, text="Generate Table", font=("Arial", 11, "bold"), bg="#4CAF50", fg="white", command=calculate_table)
btn_generate.pack(pady=15)

text_output = tk.Text(root, width=35, height=15, font=("Courier", 11))
text_output.pack(pady=10)

root.mainloop()