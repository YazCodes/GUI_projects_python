
# def update_balance(balance, withdraw, deposit):
#     """Update the bank balance after a withdrawal and deposit."""
#     balance -= withdraw
#     balance += deposit
#     return balance


# # Get user input
# balance = int(input("What is your balance? "))
# withdraw = int(input("How much do you want to withdraw? "))
# deposit = int(input("How much do you want to deposit? "))

# # Update and show result
# new_balance = update_balance(balance, withdraw, deposit)
# print(f"Your new balance is: {new_balance}")

import tkinter as tk

def update_balance():
    try:
        balance = int(balance_entry.get())
        withdraw = int(withdraw_entry.get())
        deposit = int(deposit_entry.get())

        new_balance = balance - withdraw + deposit
        result_label.config(text=f"Your new balance is: {new_balance}")
    except ValueError:
        result_label.config(text="Please enter valid numbers!")


# Create window
root = tk.Tk()
root.title("Banking App")
root.geometry("300x250")

# Balance input
tk.Label(root, text="Current Balance:").pack(pady=5)
balance_entry = tk.Entry(root)
balance_entry.pack()

# Withdraw input
tk.Label(root, text="Withdraw Amount:").pack(pady=5)
withdraw_entry = tk.Entry(root)
withdraw_entry.pack()

# Deposit input
tk.Label(root, text="Deposit Amount:").pack(pady=5)
deposit_entry = tk.Entry(root)
deposit_entry.pack()

# Button
tk.Button(root, text="Update Balance", command=update_balance).pack(pady=10)

# Result label
result_label = tk.Label(root, text="")
result_label.pack()

# Run the app
root.mainloop()
