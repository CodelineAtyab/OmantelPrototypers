import tkinter as tk
from tkinter import messagebox


def get_multiplication_table(number: int, limit: int) -> list[str]:
    return [f"{number} x {i} = {number * i}" for i in range(1, limit + 1)]


def build_app() -> None:
    root = tk.Tk()
    root.title("Multiplication Table")
    root.geometry("360x380")
    root.resizable(False, False)

    tk.Label(root, text="Multiplication Table Desktop", font=("Segoe UI", 14, "bold")).pack(pady=10)

    frame = tk.Frame(root)
    frame.pack(padx=20, pady=10, fill="x")

    tk.Label(frame, text="Number:").grid(row=0, column=0, sticky="w")
    number_var = tk.StringVar()
    tk.Entry(frame, textvariable=number_var).grid(row=0, column=1, sticky="ew")

    tk.Label(frame, text="Limit:").grid(row=1, column=0, sticky="w", pady=(10, 0))
    limit_var = tk.StringVar()
    tk.Entry(frame, textvariable=limit_var).grid(row=1, column=1, sticky="ew", pady=(10, 0))

    frame.columnconfigure(1, weight=1)

    output_text = tk.Text(root, width=40, height=12, state="disabled", wrap="none")
    output_text.pack(padx=20, pady=10, fill="both", expand=True)

    def show_table() -> None:
        try:
            number = int(number_var.get().strip())
            limit = int(limit_var.get().strip())
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter valid integer values.")
            return

        output_lines = get_multiplication_table(number, limit)
        output_text.config(state="normal")
        output_text.delete("1.0", tk.END)
        if output_lines:
            output_text.insert(tk.END, "\n".join(output_lines))
        else:
            output_text.insert(tk.END, "No results for the given limit.")
        output_text.config(state="disabled")

    button_frame = tk.Frame(root)
    button_frame.pack(padx=20, pady=(0, 20), fill="x")

    tk.Button(button_frame, text="Generate Table", command=show_table).pack(side="left", expand=True, fill="x")
    tk.Button(button_frame, text="Close", command=root.destroy).pack(side="left", expand=True, fill="x", padx=(10, 0))

    root.mainloop()


if __name__ == "__main__":
    build_app()
