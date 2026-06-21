import customtkinter as ctk
from tkinter import messagebox


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class MultiplicationTableApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Multiplication Table Studio")
        self.geometry("980x640")
        self.minsize(900, 560)
        self.configure(fg_color="#0f172a")

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=2)
        self.grid_rowconfigure(1, weight=1)

        self._build_ui()

    def _build_ui(self):
        header = ctk.CTkFrame(self, corner_radius=24, fg_color="#111827", border_width=1, border_color="#1f2937")
        header.grid(row=0, column=0, columnspan=2, sticky="ew", padx=18, pady=(18, 12))
        header.grid_columnconfigure(0, weight=1)

        title = ctk.CTkLabel(
            header,
            text="Multiplication Table Studio",
            font=("Segoe UI", 28, "bold"),
            text_color="#eff6ff",
            anchor="w",
        )
        title.grid(row=0, column=0, sticky="w", padx=20, pady=(18, 4))

        subtitle = ctk.CTkLabel(
            header,
            text="Generate clean, readable multiplication tables with a modern desktop interface.",
            font=("Segoe UI", 13),
            text_color="#cbd5e1",
            anchor="w",
        )
        subtitle.grid(row=1, column=0, sticky="w", padx=20, pady=(0, 18))

        left_panel = ctk.CTkFrame(self, corner_radius=24, fg_color="#111827", border_width=1, border_color="#1f2937")
        left_panel.grid(row=1, column=0, sticky="nsew", padx=(18, 9), pady=(0, 18))
        left_panel.grid_columnconfigure(0, weight=1)

        right_panel = ctk.CTkFrame(self, corner_radius=24, fg_color="#111827", border_width=1, border_color="#1f2937")
        right_panel.grid(row=1, column=1, sticky="nsew", padx=(9, 18), pady=(0, 18))
        right_panel.grid_columnconfigure(0, weight=1)
        right_panel.grid_rowconfigure(1, weight=1)

        ctk.CTkLabel(left_panel, text="Table settings", font=("Segoe UI", 18, "bold"), text_color="#eff6ff").grid(
            row=0, column=0, sticky="w", padx=18, pady=(18, 4)
        )
        ctk.CTkLabel(
            left_panel,
            text="Enter a number and how far you want the table to go.",
            font=("Segoe UI", 12),
            text_color="#cbd5e1",
        ).grid(row=1, column=0, sticky="w", padx=18, pady=(0, 18))

        card = ctk.CTkFrame(left_panel, corner_radius=18, fg_color="#172554", border_width=1, border_color="#1e3a8a")
        card.grid(row=2, column=0, sticky="ew", padx=18, pady=(0, 18))
        card.grid_columnconfigure(0, weight=1)

        ctk.CTkLabel(card, text="Number to multiply", font=("Segoe UI", 13, "bold"), text_color="#dbeafe").grid(
            row=0, column=0, sticky="w", padx=16, pady=(16, 6)
        )
        self.number_var = ctk.StringVar(value="7")
        self.number_entry = ctk.CTkEntry(card, textvariable=self.number_var, placeholder_text="Example: 7", font=("Segoe UI", 14))
        self.number_entry.grid(row=1, column=0, sticky="ew", padx=16, pady=(0, 12))

        ctk.CTkLabel(card, text="Up to what number?", font=("Segoe UI", 13, "bold"), text_color="#dbeafe").grid(
            row=2, column=0, sticky="w", padx=16, pady=(4, 6)
        )
        self.limit_var = ctk.StringVar(value="10")
        self.limit_entry = ctk.CTkEntry(card, textvariable=self.limit_var, placeholder_text="Example: 10", font=("Segoe UI", 14))
        self.limit_entry.grid(row=3, column=0, sticky="ew", padx=16, pady=(0, 16))

        button_row = ctk.CTkFrame(left_panel, fg_color="transparent")
        button_row.grid(row=3, column=0, sticky="ew", padx=18, pady=(0, 14))
        button_row.grid_columnconfigure(0, weight=1)
        button_row.grid_columnconfigure(1, weight=1)

        generate_button = ctk.CTkButton(
            button_row,
            text="Generate table",
            font=("Segoe UI", 13, "bold"),
            height=42,
            corner_radius=14,
            command=self.generate_table,
        )
        generate_button.grid(row=0, column=0, sticky="ew", padx=(0, 8))

        clear_button = ctk.CTkButton(
            button_row,
            text="Clear",
            font=("Segoe UI", 13, "bold"),
            height=42,
            corner_radius=14,
            fg_color="#374151",
            hover_color="#4b5563",
            command=self.clear_output,
        )
        clear_button.grid(row=0, column=1, sticky="ew", padx=(8, 0))

        insight_frame = ctk.CTkFrame(left_panel, corner_radius=18, fg_color="#111827", border_width=1, border_color="#1f2937")
        insight_frame.grid(row=4, column=0, sticky="ew", padx=18, pady=(0, 18))
        insight_frame.grid_columnconfigure(0, weight=1)

        ctk.CTkLabel(insight_frame, text="Quick tips", font=("Segoe UI", 14, "bold"), text_color="#eff6ff").grid(
            row=0, column=0, sticky="w", padx=16, pady=(14, 4)
        )
        ctk.CTkLabel(
            insight_frame,
            text="• Try different numbers to compare patterns\n• Use the clear button to reset the view\n• The result panel updates instantly after each run",
            font=("Segoe UI", 12),
            text_color="#cbd5e1",
            justify="left",
            anchor="w",
        ).grid(row=1, column=0, sticky="w", padx=16, pady=(0, 16))

        ctk.CTkLabel(right_panel, text="Result preview", font=("Segoe UI", 18, "bold"), text_color="#eff6ff").grid(
            row=0, column=0, sticky="w", padx=18, pady=(18, 6)
        )
        self.status_var = ctk.StringVar(value="Ready to generate your first table.")
        ctk.CTkLabel(right_panel, textvariable=self.status_var, font=("Segoe UI", 12), text_color="#bfdbfe").grid(
            row=1, column=0, sticky="w", padx=18, pady=(0, 10)
        )

        self.output_box = ctk.CTkTextbox(
            right_panel,
            font=("Cascadia Code", 13),
            fg_color="#020617",
            text_color="#e5eefb",
            corner_radius=18,
            border_width=1,
            border_color="#1e293b",
            activate_scrollbars=True,
        )
        self.output_box.grid(row=2, column=0, sticky="nsew", padx=18, pady=(0, 18))
        self.output_box.insert("0.0", "Pick a number and limit, then click Generate table to see your result here.")
        self.output_box.configure(state="disabled")

        self.bind("<Return>", lambda event: self.generate_table())

    def generate_table(self):
        try:
            number = int(self.number_var.get())
            limit = int(self.limit_var.get())
        except ValueError:
            messagebox.showerror("Input error", "Please enter valid whole numbers for the table and limit.")
            return

        if limit < 1:
            messagebox.showerror("Input error", "The limit must be at least 1.")
            return

        rows = [f"{number} × {i} = {number * i}" for i in range(1, limit + 1)]
        table_text = "\n".join(rows)

        self.output_box.configure(state="normal")
        self.output_box.delete("0.0", "end")
        self.output_box.insert(
            "0.0",
            f"Multiplication table for {number}\n"
            f"{'=' * 36}\n"
            f"{table_text}\n\n"
            f"Generated with {limit} terms.",
        )
        self.output_box.configure(state="disabled")
        self.status_var.set(f"Showing {limit} results for the number {number}.")

    def clear_output(self):
        self.output_box.configure(state="normal")
        self.output_box.delete("0.0", "end")
        self.output_box.insert("0.0", "Pick a number and limit, then click Generate table to see your result here.")
        self.output_box.configure(state="disabled")
        self.status_var.set("Ready to generate your first table.")


if __name__ == "__main__":
    app = MultiplicationTableApp()
    app.mainloop()
