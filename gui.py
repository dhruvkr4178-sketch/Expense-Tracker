import customtkinter as ctk
from tkinter import ttk
import csv

# Theme
ctk.set_appearance_mode("dark")      # dark / light
ctk.set_default_color_theme("blue")  # blue / green / dark-blue

# Window
app = ctk.CTk()
expenses = []
tree = None
view_window = None
selected_expense = None
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
    refresh_table()

#     tree.insert(
#     "",
#     "end",
#     values=(date, category, description, amount)
# )

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
                str(expense["date"]) == str(values[0])
                and str(expense["category"]) == str(values[1])
                and str(expense["description"]) == str(values[2])
                and float(expense["amount"]) == float(values[3])
            ):
                expenses.remove(expense)
                break
    # Remove from table
    refresh_table()

    # Update total after delete
    calculate_total()

# Delete Button
# delete_button = ctk.CTkButton(
#     app,
#     text="Delete Selected Expense",
#     command=delete_expense
# )

# delete_button.pack(pady=10)

def edit_expense():

    print("Edit button clicked")

    global selected_expense

    selected_item = tree.selection()

    print(selected_item)

    if not selected_item:
        return

    item = selected_item[0]

    values = tree.item(item)["values"]

    print(values)

    for expense in expenses:

        if (
            str(expense["date"]) == str(values[0])
            and str(expense["category"]) == str(values[1])
            and str(expense["description"]) == str(values[2])
            and float(expense["amount"]) == float(values[3])
        ):

            selected_expense = expense

            print("Matched:", selected_expense)
            break

    date_entry.delete(0, "end")
    date_entry.insert(0, selected_expense["date"])

    category_entry.delete(0, "end")
    category_entry.insert(0, selected_expense["category"])

    description_entry.delete(0, "end")
    description_entry.insert(0, selected_expense["description"])

    amount_entry.delete(0, "end")
    amount_entry.insert(0, selected_expense["amount"])

    print(date_entry.get())
    print(category_entry.get())
    print(description_entry.get())
    print(amount_entry.get())   


def update_expense():

    global selected_expense

    if selected_expense is None:
        return

    selected_expense["date"] = date_entry.get()
    selected_expense["category"] = category_entry.get()
    selected_expense["description"] = description_entry.get()
    selected_expense["amount"] = float(amount_entry.get())

    refresh_table()
    calculate_total()

    date_entry.delete(0, "end")
    category_entry.delete(0, "end")
    description_entry.delete(0, "end")
    amount_entry.delete(0, "end")

    selected_expense = None

def refresh_table():

    if tree is None:
        return

    # Purani rows delete karo
    for item in tree.get_children():
        tree.delete(item)

    # Nayi rows add karo
    for expense in expenses:
        tree.insert(
            "",
            "end",
            values=(
                expense["date"],
                expense["category"],
                expense["description"],
                expense["amount"]
            )
        )


def save_expenses():

    with open("expenses.csv", "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerow(
            ["Date", "Category", "Description", "Amount"]
        )

        for expense in expenses:

            writer.writerow([
                expense["date"],
                expense["category"],
                expense["description"],
                expense["amount"]
            ])

def load_expenses():

    global expenses

    try:

        with open("expenses.csv", "r") as file:

            reader = csv.DictReader(file)

            expenses = []

            for row in reader:

                expenses.append({
                    "date": row["Date"],
                    "category": row["Category"],
                    "description": row["Description"],
                    "amount": float(row["Amount"])
                })

    except FileNotFoundError:

        expenses = []



def view_expenses():

    global tree, view_window

    if view_window is not None and view_window.winfo_exists():
        view_window.lift()
        view_window.focus_force()
        refresh_table()
        return

    view_window = ctk.CTkToplevel(app)
    view_window.title("All Expenses")
    view_window.geometry("750x450")
    view_window.after(100, view_window.lift)
    view_window.after(100, view_window.focus_force)
    view_window.after(100, lambda: view_window.attributes("-topmost", False))

    columns = ("Date", "Category", "Description", "Amount")

    tree = ttk.Treeview(view_window, columns=columns, show="headings", height=15)

    tree.heading("Date", text="Date")
    tree.heading("Category", text="Category")
    tree.heading("Description", text="Description")
    tree.heading("Amount", text="Amount")

    tree.column("Date", width=130)
    tree.column("Category", width=150)
    tree.column("Description", width=250)
    tree.column("Amount", width=120)

    tree.pack(fill="both", expand=True, padx=20, pady=20)


    delete_button = ctk.CTkButton(
       view_window,
       text="Delete Selected",
       command=delete_expense
)
    
    delete_button.pack(pady=10)


    edit_button = ctk.CTkButton(
    view_window,
    text="Edit Selected",
    command=edit_expense
)

    edit_button.pack(pady=10)

    # Show all expenses
    refresh_table()

view_button = ctk.CTkButton(
    app,
    text="View Expenses",
    command=view_expenses
)

view_button.pack(pady=10)

update_button = ctk.CTkButton(
    app,
    text="Update Expense",
    command=update_expense
)

update_button.pack(pady=5)

save_button = ctk.CTkButton(
    app,
    text="Save Expenses",
    command=save_expenses
)

save_button.pack(pady=5)

load_expenses()

app.mainloop()