#A Python desktop application that calculates the year a user will reach 100 years old using a graphical user interface.
import tkinter as tk
from datetime import datetime

def calculate_year():
    name = name_entry.get()
    age = int(age_entry.get())
    current_year = datetime.now().year
    year_100 = current_year + (100 - age)

    result_label.config(
        text=f"Hello {name}, you will turn 100 in the year {year_100}"
    )

# Window
window = tk.Tk()
window.title("Age Prediction Calculator")
window.geometry("400x300")

# Widgets
tk.Label(window, text="Enter your name").pack()
name_entry = tk.Entry(window)
name_entry.pack()

tk.Label(window, text="Enter your age").pack()
age_entry = tk.Entry(window)
age_entry.pack()

tk.Button(window, text="Calculate", command=calculate_year).pack()

result_label = tk.Label(window, text="")
result_label.pack()

window.mainloop()




