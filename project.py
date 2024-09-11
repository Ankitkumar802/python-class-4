import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("Calculator")

# Entry widget to display the numbers and result
entry = tk.Entry(window, width=20, borderwidth=5, font=("Arial", 20))
entry.grid(row=0, column=0, columnspan=4)

# Function to insert number or operator into the entry
def button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(value))

# Function to clear the entry
def button_clear():
    entry.delete(0, tk.END)

# Function to evaluate the expression
def button_equal():
    try:
        result = eval(entry.get())  # Use eval to calculate the expression
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Create number buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row = 1
col = 0

for button in buttons:
    if button == "=":
        tk.Button(window, text=button, width=10, height=3, command=button_equal).grid(row=row, column=col, columnspan=2)
        col += 1
    else:
        tk.Button(window, text=button, width=5, height=3, command=lambda b=button: button_click(b)).grid(row=row, column=col)
    
    col += 1
    if col > 3:
        col = 0
        row += 1

# Clear button
tk.Button(window, text="Clear", width=20, height=3, command=button_clear).grid(row=row, column=0, columnspan=4)

# Start the Tkinter event loop
window.mainloop()
