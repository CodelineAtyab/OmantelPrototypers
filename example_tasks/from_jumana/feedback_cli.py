import tkinter as tk

CORRECT_PIN = "1234"
MAX_ATTEMPTS = 3   # set to None for unlimited retries


# ---------- CLI version ----------
def run_cli():
    attempts = 0
    while True:
        entered = input("Enter PIN: ")
        if entered == CORRECT_PIN:
            print("Access granted.")
            return True
        attempts += 1
        if MAX_ATTEMPTS and attempts >= MAX_ATTEMPTS:
            print("Too many incorrect attempts.")
            return False
        print("Incorrect PIN. Try again.")


# ---------- Desktop version ----------
def run_desktop():
    def check_pin():
        if pin_entry.get() == CORRECT_PIN:
            message.config(text="Access granted.", fg="green")
            # continue to your admin / shutdown panel here
        else:
            message.config(text="Incorrect PIN. Try again.", fg="red")
            pin_entry.delete(0, tk.END)   # clear the wrong entry
            pin_entry.focus_set()         # cursor back in the box immediately

    window = tk.Tk()
    window.title("Enter PIN")
    window.geometry("250x180")

    tk.Label(window, text="PIN:").pack(pady=(15, 0))
    pin_entry = tk.Entry(window, show="*")   # masks the PIN with *
    pin_entry.pack()
    pin_entry.focus_set()

    tk.Button(window, text="Submit", command=check_pin).pack(pady=10)

    message = tk.Label(window, text="")
    message.pack()

    window.bind("<Return>", lambda event: check_pin())   # Enter key also submits

    window.mainloop()


# ---------- Launcher ----------
if __name__ == "__main__":
    print("PIN Retry")
    print("1. CLI version")
    print("2. Desktop version")
    choice = input("Choose 1 or 2: ").strip()

    if choice == "1":
        run_cli()
    elif choice == "2":
        run_desktop()
    else:
        print("Invalid choice. Please run again and enter 1 or 2.")