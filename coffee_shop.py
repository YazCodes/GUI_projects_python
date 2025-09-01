import tkinter as tk

ice_coffee_price = 300
hot_chocolate_price = 500
tea_price = 200

def calculate_total():
    try:
        ice_qty = int(ice_entry.get() or 0)
        hot_qty = int(hot_entry.get() or 0)
        tea_qty = int(tea_entry.get() or 0)

        global ice_coffee_price, hot_chocolate_price, tea_price
        ice_coffee_price = 300
        hot_chocolate_price = 500
        tea_price = 200

        total = (ice_qty * ice_coffee_price) + (hot_qty * hot_chocolate_price) + (tea_qty * tea_price)

        result_label.config(text=f"Your total cost is: ¥{total}")
    except ValueError:
        result_label.config(text="Please enter numbers only!")


root = tk.Tk()
root.title("☕ Coffee Shop")
root.geometry("350x300")
root.config(bg="#f5f5dc") 


tk.Label(root, text="Welcome to the Coffee Shop!", font=("Arial", 14, "bold"), bg="#f5f5dc").pack(pady=10)

tk.Label(root, text=f"Ice Coffee (¥{ice_coffee_price}):", bg="#f5f5dc").pack()
ice_entry = tk.Entry(root, width=5)
ice_entry.pack()

tk.Label(root, text=f"Hot Chocolate (¥{hot_chocolate_price}):", bg="#f5f5dc").pack()
hot_entry = tk.Entry(root, width=5)
hot_entry.pack()

tk.Label(root, text=f"Green tea (¥{tea_price}):", bg="#f5f5dc").pack()
tea_entry = tk.Entry(root, width=5)
tea_entry.pack()

tk.Button(root, text="Calculate Total", command=calculate_total, bg="#8B4513", fg="white", font=("Arial", 12, "bold")).pack(pady=15)

result_label = tk.Label(root, text="", font=("Arial", 12, "bold"), bg="#f5f5dc")
result_label.pack()

root.mainloop()
