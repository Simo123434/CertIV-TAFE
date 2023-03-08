import tkinter as tk
from tkinter import ttk

# Create the root window
root = tk.Tk()
root.title("C0ffeE Sh0p Order System")
root.geometry("2000x1000")

# Create welcome message at top of window
welcomeMesasge = tk.Label(root, text="Welcome to C0ffeE Sh0p", font=("Arial", 30, "bold"))
welcomeMesasge.pack()



def radio_change():
    if selectedDrink.get() == 'coffee':
        print("User selected coffee")



# Prepare drink options with handler for inputs

drinks = ["coffee", "tea", "water"]
selectedDrink = tk.StringVar()
selectedDrink.trace_add('write', radio_change)
for drink in drinks:
    r = ttk.Radiobutton(
        root,
        text=drink,
        value=drink,
        variable=selectedDrink,
    )
    r.pack(fill='x', padx=5, pady=5)




root.mainloop()