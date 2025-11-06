

import tkinter as tk
from tkinter import messagebox


# Create main application window
root = tk.Tk()
root.title("NextHikes Calculator")
root.geometry("320x470")
root.resizable(False, False)
root.configure(bg="#202020")


# Equation display variable
expression = ""


# Function to update expression in the text entry field
def press(num):
global expression
expression += str(num)
equation.set(expression)


# Function to evaluate final expression
def equal_press():
global expression
try:
total = str(eval(expression))
equation.set(total)
expression = total
except ZeroDivisionError:
messagebox.showerror("Error", "Cannot divide by zero")
equation.set("")
expression = ""
except Exception:
messagebox.showerror("Error", "Invalid Input")
equation.set("")
expression = ""


# Function to clear the entry field
def clear():
global expression
expression = ""
equation.set("")


# Equation StringVar
equation = tk.StringVar()


# Entry field for showing expressions
entry_field = tk.Entry(root, textvariable=equation, font=('Arial', 24), bg="#333", fg="white", bd=10, insertwidth=2, width=15, borderwidth=4, relief="ridge", justify='right')
entry_field.grid(row=0, column=0, columnspan=4, padx=10, pady=20)


# Button style settings
button_config = {
'font': ('Arial', 18),
'bg': '#4B4B4B',
root.mainloop()
