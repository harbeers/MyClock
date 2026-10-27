import tkinter as tk
from datetime import datetime

root = tk.Tk()
root.title("24-Hour Clock")

clock = tk.Label(root, font=("Arial", 48), padx=20, pady=10)
clock.pack()


def update_clock():
    clock.config(text=datetime.now().strftime("%H:%M:%S"))
    root.after(1000, update_clock)


update_clock()
root.mainloop()