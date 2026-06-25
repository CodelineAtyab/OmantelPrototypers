import tkinter as tk


# ---------- Shared logic ----------
def build_table(number, limit):
    return [f"{number} x {i} = {number * i}" for i in range(1, limit + 1)]


# ---------- CLI version ----------
def get_number(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a whole number.")

def run_cli():
    number = get_number("Enter a number: ")
    limit = get_number("Enter the limit: ")
    for line in build_table(number, limit):
        print(line)


# ---------- Desktop version ----------
def run_desktop():
    def generate_table():
        output.delete("1.0", tk.END)
        try:
            number = int(number_entry.get())
            limit = int(limit_entry.get())
        except ValueError:
            output.insert(tk.END, "Please enter whole numbers in both fields.")
            return
        for line in build_table(number, limit):
            output.insert(tk.END, line + "\n")

    window = tk.Tk()
    window.title("Multiplication Table")
    window.geometry("300x400")

    tk.Label(window, text="Number:").pack(pady=(10, 0))
    number_entry = tk.Entry(window)
    number_entry.pack()

    tk.Label(window, text="Limit:").pack(pady=(10, 0))
    limit_entry = tk.Entry(window)
    limit_entry.pack()

    tk.Button(window, text="Generate", command=generate_table).pack(pady=10)

    output = tk.Text(window, height=15, width=30)
    output.pack(pady=10)

    window.mainloop()


# ---------- Launcher ----------
if __name__ == "__main__":
    print("Multiplication Table")
    print("1. CLI version")
    print("2. Desktop version")
    choice = input("Choose 1 or 2: ").strip()

    if choice == "1":
        run_cli()
    elif choice == "2":
        run_desktop()
    else:
        print("Invalid choice. Please run again and enter 1 or 2.")