import customtkinter as ctk
from tkinter import ttk

# Theme
ctk.set_appearance_mode("dark")      # dark / light
ctk.set_default_color_theme("blue")  # blue / green / dark-blue

# Window
app = ctk.CTk()
expenses = []
app.title("Expense Tracker")
app.geometry("700x500")

# Heading
title = ctk.CTkLabel(
    app,
    text="Expense Tracker",
    font=("Arial", 25, "bold")
)
title.pack(pady=20)

# Date
date_label = ctk.CTkLabel(app, text="Date")
date_label.pack()

date_entry = ctk.CTkEntry(app, width=300)
date_entry.pack(pady=5)

# Category
category_label = ctk.CTkLabel(app, text="Category")
category_label.pack()

category_entry = ctk.CTkEntry(app, width=300)
category_entry.pack(pady=5)

# Description
description_label = ctk.CTkLabel(app, text="Description")
description_label.pack()

description_entry = ctk.CTkEntry(app, width=300)
description_entry.pack(pady=5)

# Amount
amount_label = ctk.CTkLabel(app, text="Amount")
amount_label.pack()

amount_entry = ctk.CTkEntry(app, width=300)
amount_entry.pack(pady=10)





def add_expense():

    date = date_entry.get()
    category = category_entry.get()
    description = description_entry.get()
    amount = float(amount_entry.get())

    expense = {
        "date": date,
        "category": category,
        "description": description,
        "amount": amount
    }

    expenses.append(expense)

    tree.insert(
    "",
    "end",
    values=(date, category, description, amount)
)

    date_entry.delete(0, "end")
    category_entry.delete(0, "end")
    description_entry.delete(0, "end")
    amount_entry.delete(0, "end")

add_button = ctk.CTkButton(
    app,
    text="Add Expense",
    command=add_expense
)

add_button.pack(pady=15)



columns = ("Date", "Category", "Description", "Amount")

tree = ttk.Treeview(app, columns=columns, show="headings", height=8)

tree.heading("Date", text="Date")
tree.heading("Category", text="Category")
tree.heading("Description", text="Description")
tree.heading("Amount", text="Amount")

tree.column("Date", width=130)
tree.column("Category", width=150)
tree.column("Description", width=250)
tree.column("Amount", width=120)

tree.pack(pady=20, fill="x", padx=20)

app.mainloop()