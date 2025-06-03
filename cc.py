import tkinter as tk
from tkinter import ttk, messagebox

# --- Hardcoded exchange rates (base: USD) ---
exchange_rates = {
    "USD": 1.0,
    "INR": 83.2,
    "EUR": 0.92,
    "GBP": 0.78,
    "JPY": 157.6,
    "AUD": 1.52,
    "CAD": 1.37,
    "CHF": 0.90,
    "CNY": 7.24
}

# --- Conversion Function ---
def convert_currency():
    from_currency = from_currency_var.get()
    to_currency = to_currency_var.get()
    amount = amount_var.get()

    if not amount:
        messagebox.showerror("Error", "Please enter an amount.")
        return

    try:
        amount = float(amount)
    except ValueError:
        messagebox.showerror("Error", "Amount must be a number.")
        return

    try:
        usd_amount = amount / exchange_rates[from_currency]
        converted = usd_amount * exchange_rates[to_currency]
        result_var.set(f"{converted:.2f} {to_currency}")
    except KeyError:
        messagebox.showerror("Error", "Invalid currency selected.")

# --- GUI Setup ---
root = tk.Tk()
root.title("Offline Currency Converter")
root.geometry("350x250")
root.resizable(False, False)

# Dropdown options
CURRENCIES = list(exchange_rates.keys())

# Widgets
tk.Label(root, text="From Currency").pack(pady=5)
from_currency_var = tk.StringVar(value="USD")
from_dropdown = ttk.Combobox(root, textvariable=from_currency_var, values=CURRENCIES, state="readonly")
from_dropdown.pack()

tk.Label(root, text="To Currency").pack(pady=5)
to_currency_var = tk.StringVar(value="INR")
to_dropdown = ttk.Combobox(root, textvariable=to_currency_var, values=CURRENCIES, state="readonly")
to_dropdown.pack()

tk.Label(root, text="Amount").pack(pady=5)
amount_var = tk.StringVar()
amount_entry = ttk.Entry(root, textvariable=amount_var)
amount_entry.pack()

tk.Button(root, text="Convert", command=convert_currency).pack(pady=10)

result_var = tk.StringVar()
tk.Label(root, textvariable=result_var, font=("Arial", 16, "bold")).pack(pady=10)

root.mainloop()
