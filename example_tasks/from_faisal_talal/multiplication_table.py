#!/usr/bin/env python3
"""
Multiplication Table Generator

A simple Tkinter app: type a number, choose how many rows,
and press Generate to see its multiplication table.
"""

import tkinter as tk
from tkinter import ttk, messagebox


def generate(entry, depth_var, output):
    raw = entry.get().strip()
    try:
        n = int(raw)
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a whole number.")
        return

    depth = depth_var.get()
    lines = [f"{i:2d}  x  {n}  =  {i * n}" for i in range(1, depth + 1)]

    output.config(state="normal")
    output.delete("1.0", tk.END)
    output.insert(tk.END, "\n".join(lines))
    output.config(state="disabled")


def main():
    root = tk.Tk()
    root.title("Multiplication Table")
    root.geometry("320x420")
    root.resizable(False, False)

    frame = ttk.Frame(root, padding=16)
    frame.pack(fill="both", expand=True)

    ttk.Label(frame, text="Number:").pack(anchor="w")
    entry = ttk.Entry(frame, font=("Segoe UI", 14))
    entry.pack(fill="x", pady=(0, 12))
    entry.focus()

    ttk.Label(frame, text="Rows:").pack(anchor="w")
    depth_var = tk.IntVar(value=10)
    ttk.Spinbox(frame, from_=1, to=100, textvariable=depth_var, width=8).pack(
        anchor="w", pady=(0, 12)
    )

    output = tk.Text(
        frame, height=12, font=("Consolas", 12), state="disabled",
        relief="solid", borderwidth=1,
    )
    output.pack(fill="both", expand=True, pady=(0, 12))

    btn = ttk.Button(
        frame, text="Generate",
        command=lambda: generate(entry, depth_var, output),
    )
    btn.pack(fill="x")

    # Enter key also generates the table
    root.bind("<Return>", lambda _e: generate(entry, depth_var, output))

    root.mainloop()


if __name__ == "__main__":
    main()