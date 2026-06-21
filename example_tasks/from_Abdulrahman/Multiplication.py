#multipication table
number = int(input("Enter a number: "))
limit = int(input("Enter a limit: "))
 
for i in range(1, limit + 1):
   print(f"{number} x {i} = {number * i}")
 
   # multiplication table — CLI
 
def multiplication_table(number: int, limit: int) -> list[str]:
    """Return a list of formatted multiplication rows."""
    return [f"{number} x {i} = {number * i}" for i in range(1, limit + 1)]
 
 
def get_valid_int(prompt: str, min_val: int = 1) -> int:
    """Keep asking until the user enters a whole number >= min_val."""
    while True:
        try:
            value = int(input(prompt))
            if value < min_val:
                print(f"  Please enter a number that is {min_val} or greater.")
            else:
                return value
        except ValueError:
            print("  Invalid input — please enter a whole number.")
 
 
def main():
    print("\n=== Multiplication Table ===\n")
    number = get_valid_int("Enter a number : ")
    limit  = get_valid_int("Enter a limit  : ")
    print()
    for row in multiplication_table(number, limit):
        print(" ", row)
    print()
 
 
if __name__ == "__main__":
    main()
 
    # multiplication table — Desktop App (tkinter)
# Kept separate from cli.py; shares only the pure core function.
 
import tkinter as tk
from tkinter import messagebox
from cli import multiplication_table   # reuse the tested core function
 
# ── Palette ────────────────────────────────────────────────────────────
BG          = "#1e1e2e"
SURFACE     = "#2a2a3e"
SURFACE2    = "#252538"
ACCENT      = "#a78bfa"
ACCENT2     = "#f472b6"
TEXT        = "#e2e8f0"
MUTED       = "#64748b"
BTN_BG      = "#a78bfa"
BTN_FG      = "#ffffff"
BTN_HOVER   = "#7c3aed"
 
FONT_TITLE  = ("Segoe UI",  18, "bold")
FONT_LABEL  = ("Segoe UI",  11)
FONT_INPUT  = ("Courier New", 13)
FONT_ROW    = ("Courier New", 12)
FONT_RESULT = ("Courier New", 12, "bold")
FONT_HINT   = ("Segoe UI",    9)
 
 
# multiplication table — Desktop App (tkinter)
# Kept separate from cli.py; shares only the pure core function.
 
import tkinter as tk
from tkinter import messagebox
from cli import multiplication_table   # reuse the tested core function
 
# ── Palette ────────────────────────────────────────────────────────────
BG          = "#1e1e2e"
SURFACE     = "#2a2a3e"
SURFACE2    = "#252538"
ACCENT      = "#a78bfa"
ACCENT2     = "#f472b6"
TEXT        = "#e2e8f0"
MUTED       = "#64748b"
BTN_BG      = "#a78bfa"
BTN_FG      = "#ffffff"
BTN_HOVER   = "#7c3aed"
 
FONT_TITLE  = ("Segoe UI",  18, "bold")
FONT_LABEL  = ("Segoe UI",  11)
FONT_INPUT  = ("Courier New", 13)
FONT_ROW    = ("Courier New", 12)
FONT_RESULT = ("Courier New", 12, "bold")
FONT_HINT   = ("Segoe UI",    9)
 
 
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Multiplication Table")
        self.geometry("460x580")
        self.resizable(False, False)
        self.configure(bg=BG)
        self._build_ui()
        self.bind("<Return>", lambda _: self._generate())
 
    def _build_ui(self):
        tk.Frame(self, bg=ACCENT, height=4).pack(fill="x")
 
        tk.Label(self, text="Multiplication Table",
                 font=FONT_TITLE, bg=BG, fg=TEXT).pack(pady=(20, 2))
        tk.Label(self, text="Enter a number and a limit to generate your table.",
                 font=FONT_HINT, bg=BG, fg=MUTED).pack()
 
        card = tk.Frame(self, bg=SURFACE, padx=24, pady=20)
        card.pack(fill="x", padx=30, pady=(18, 0))
 
        tk.Label(card, text="Number", font=FONT_LABEL,
                 bg=SURFACE, fg=MUTED, anchor="w").grid(row=0, column=0, sticky="w")
        self.num_var = tk.StringVar()
        num_entry = tk.Entry(card, textvariable=self.num_var, width=10,
                             font=FONT_INPUT, bg=BG, fg=TEXT,
                             insertbackground=ACCENT, relief="flat", bd=4)
        num_entry.grid(row=1, column=0, sticky="w", pady=(4, 0))
        num_entry.focus_set()
 
        tk.Label(card, text="Limit", font=FONT_LABEL,
                 bg=SURFACE, fg=MUTED, anchor="w").grid(
                 row=0, column=1, sticky="w", padx=(28, 0))
        self.lim_var = tk.StringVar()
        lim_entry = tk.Entry(card, textvariable=self.lim_var, width=10,
                             font=FONT_INPUT, bg=BG, fg=TEXT,
                             insertbackground=ACCENT, relief="flat", bd=4)
        lim_entry.grid(row=1, column=1, sticky="w", padx=(28, 0), pady=(4, 0))
 
        btn = tk.Button(card, text="Generate  →",
                        font=("Segoe UI", 11, "bold"),
                        bg=BTN_BG, fg=BTN_FG, activebackground=BTN_HOVER,
                        activeforeground=BTN_FG, relief="flat",
                        cursor="hand2", padx=16, pady=8,
                        command=self._generate)
        btn.grid(row=2, column=0, columnspan=2, sticky="w", pady=(16, 0))
        btn.bind("<Enter>", lambda e: btn.config(bg=BTN_HOVER))
        btn.bind("<Leave>", lambda e: btn.config(bg=BTN_BG))
 
        result_outer = tk.Frame(self, bg=BG)
        result_outer.pack(fill="both", expand=True, padx=30, pady=(16, 20))
 
        self.canvas = tk.Canvas(result_outer, bg=BG, highlightthickness=0)
        scrollbar = tk.Scrollbar(result_outer, orient="vertical",
                                 command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)
 
        self.rows_frame = tk.Frame(self.canvas, bg=BG)
        self._win_id = self.canvas.create_window(
            (0, 0), window=self.rows_frame, anchor="nw")
 
        self.rows_frame.bind("<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")))
        self.canvas.bind("<Configure>",
            lambda e: self.canvas.itemconfig(self._win_id, width=e.width))
 
        tk.Label(self, text="CLI version available: python cli.py",
                 font=FONT_HINT, bg=BG, fg=MUTED).pack(pady=(0, 10))
 
    def _generate(self):
        try:
            number = int(self.num_var.get())
            limit  = int(self.lim_var.get())
        except ValueError:
            messagebox.showerror("Invalid input",
                "Both Number and Limit must be whole numbers.")
            return
        if number < 1 or limit < 1:
            messagebox.showerror("Invalid input",
                "Both values must be 1 or greater.")
            return
 
        for w in self.rows_frame.winfo_children():
            w.destroy()
 
        rows = multiplication_table(number, limit)
        for idx, row in enumerate(rows):
            bg = SURFACE if idx % 2 == 0 else SURFACE2
            lhs, rhs = row.split("=")
 
            row_frame = tk.Frame(self.rows_frame, bg=bg, pady=7, padx=16)
            row_frame.pack(fill="x")
 
            tk.Label(row_frame, text=lhs.strip() + "  =",
                     font=FONT_ROW, bg=bg, fg=TEXT,
                     width=14, anchor="e").pack(side="left")
            tk.Label(row_frame, text="  " + rhs.strip(),
                     font=FONT_RESULT, bg=bg, fg=ACCENT2).pack(side="left")
 
 
if __name__ == "__main__":
    App().mainloop()