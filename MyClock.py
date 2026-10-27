import tkinter as tk
from time import strftime


def update_clock():
    clock.config(text=strftime("%I:%M:%S %p"))
    root.after(1000, update_clock)


root = tk.Tk()
root.title("12-Hour Clock")
root.geometry("300x100")

clock = tk.Label(root, font=("Arial", 32), bg="black", fg="white")
clock.pack(expand=True, fill="both")

update_clock()
root.mainloop()