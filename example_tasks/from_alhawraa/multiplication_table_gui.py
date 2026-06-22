"""A simple desktop multiplication table utility using Tkinter."""

from __future__ import annotations

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from multiplication_table_cli import format_multiplication_table


class MultiplicationTableApp(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("Multiplication Table Utility")
        self.geometry("360x320")
        self.resizable(False, False)

        self._build_ui()

    def _build_ui(self) -> None:
        frame = ttk.Frame(self, padding=16)
        frame.pack(fill=tk.BOTH, expand=True)

        ttk.Label(frame, text="Number:").grid(row=0, column=0, sticky=tk.W)
        self.number_entry = ttk.Entry(frame)
        self.number_entry.grid(row=0, column=1, sticky=tk.EW, pady=4)

        ttk.Label(frame, text="Limit:").grid(row=1, column=0, sticky=tk.W)
        self.limit_entry = ttk.Entry(frame)
        self.limit_entry.grid(row=1, column=1, sticky=tk.EW, pady=4)

        generate_button = ttk.Button(frame, text="Generate", command=self.on_generate)
        generate_button.grid(row=2, column=0, columnspan=2, pady=(8, 12))

        self.result_text = tk.Text(frame, width=36, height=10, state=tk.DISABLED)
        self.result_text.grid(row=3, column=0, columnspan=2, pady=4)

        frame.columnconfigure(1, weight=1)

    def on_generate(self) -> None:
        number_text = self.number_entry.get().strip()
        limit_text = self.limit_entry.get().strip()

        try:
            number_value = int(number_text)
            limit_value = int(limit_text)
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter valid integers for number and limit.")
            return

        if limit_value < 0:
            messagebox.showerror("Invalid limit", "Limit must be zero or greater.")
            return

        lines = format_multiplication_table(number_value, limit_value)
        self._show_result(lines)

    def _show_result(self, lines: list[str]) -> None:
        self.result_text.config(state=tk.NORMAL)
        self.result_text.delete("1.0", tk.END)
        if lines:
            self.result_text.insert(tk.END, "\n".join(lines))
        else:
            self.result_text.insert(tk.END, "No results to display.")
        self.result_text.config(state=tk.DISABLED)


def main() -> None:
    app = MultiplicationTableApp()
    app.mainloop()


if __name__ == "__main__":
    main()
