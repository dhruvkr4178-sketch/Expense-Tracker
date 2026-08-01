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

app.mainloop()