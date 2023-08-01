import tkinter as tk

# Function to handle button click
def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(number))

# Function to clear the entry field
def clear_entry():
    entry.delete(0, tk.END)

# Function to evaluate the expression and display the result
def button_equal():
    expression = entry.get()
    try:
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Create the main window
window = tk.Tk()
window.title("Julius Kazibwe Calculator")

# Create an entry field
entry = tk.Entry(window, width=30)
entry.grid(row=0, column=0, columnspan=4)

# Button configurations
button_config = {
    "padx": 20,
    "pady": 10,
    "bg": "#F0F0F0",
    "fg": "#000000",
    "font": ("Arial", 12)
}

# Create buttons for numbers and operators
buttons = [
    [tk.Button(window, text="1", command=lambda: button_click(1)), tk.Button(window, text="2", command=lambda: button_click(2)), tk.Button(window, text="3", command=lambda: button_click(3)), tk.Button(window, text="+", command=lambda: button_click("+"))],
    [tk.Button(window, text="4", command=lambda: button_click(4)), tk.Button(window, text="5", command=lambda: button_click(5)), tk.Button(window, text="6", command=lambda: button_click(6)), tk.Button(window, text="-", command=lambda: button_click("-"))],
    [tk.Button(window, text="7", command=lambda: button_click(7)), tk.Button(window, text="8", command=lambda: button_click(8)), tk.Button(window, text="9", command=lambda: button_click(9)), tk.Button(window, text="*", command=lambda: button_click("*"))],
    [tk.Button(window, text="0", command=lambda: button_click(0)), tk.Button(window, text="C", command=clear_entry), tk.Button(window, text="=", command=button_equal), tk.Button(window, text="/", command=lambda: button_click("/"))]
]

# Position the buttons on the grid and configure their appearance
for row_index, row in enumerate(buttons):
    for col_index, button in enumerate(row):
        button.grid(row=row_index+1, column=col_index)
        button.config(**button_config)

# Start the main event loop
window.mainloop()
