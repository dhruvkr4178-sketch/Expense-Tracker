import customtkinter as ctk
from tkinter import ttk

# Theme
ctk.set_appearance_mode("dark")      # dark / light
ctk.set_default_color_theme("blue")  # blue / green / dark-blue

# Window
app = ctk.CTk()
expenses = []
app.title("Expense Tracker")
app.geometry("800x800")

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

# Total Expense Label
total_label = ctk.CTkLabel(
    app,
    text="Total Expense: ₹0",
    font=("Arial", 18, "bold")
)

total_label.pack(pady=5)


# Calculate Total Expense
def calculate_total():

    total = 0

    for item in expenses:
        total = total + item["amount"]

    total_label.configure(
        text=f"Total Expense: ₹{total}"
    )


# Total Expense Button
total_button = ctk.CTkButton(
    app,
    text="Total Expense",
    command=calculate_total
)

total_button.pack(pady=10)


# Delete Selected Expense
def delete_expense():

    selected_item = tree.selection()

    if selected_item:
        item = selected_item[0]

        # Get selected row data
        values = tree.item(item)["values"]

        # Remove from expenses list
        for expense in expenses:
            if (
                expense["date"] == values[0]
                and expense["category"] == values[1]
                and expense["description"] == values[2]
                and expense["amount"] == values[3]
            ):
                expenses.remove(expense)
                break

        # Remove from table
        tree.delete(item)

        # Update total after delete
        calculate_total()

# Delete Button
delete_button = ctk.CTkButton(
    app,
    text="Delete Selected Expense",
    command=delete_expense
)

delete_button.pack(pady=10)

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