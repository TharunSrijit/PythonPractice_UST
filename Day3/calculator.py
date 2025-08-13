import tkinter as tk
from tkinter import ttk, messagebox
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

root = tk.Tk()
root.title("Modular Calculator")
root.geometry("300x280")
root.resizable(True, True)

def clear_fields():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    result_var.set("")

def calculate(op):
        num1 = float(entry1.get())
        num2 = float(entry2.get())

        if op == "add":
            result = add(num1, num2)
        elif op == "subtract":
            result = subtract(num1, num2)
        elif op == "multiply":
            result = multiply(num1, num2)
        elif op == "divide":
            result = divide(num1, num2)

        result_var.set(f"Result: {result}")
        else:
        messagebox.showerror("Error", "Please enter valid numbers.")

ttk.Label(root, text="Enter First Number:").pack(pady=5)
entry1 = ttk.Entry(root)
entry1.pack()

ttk.Label(root, text="Enter Second Number:").pack(pady=5)
entry2 = ttk.Entry(root)
entry2.pack()

# Operation Buttons
btn_frame = ttk.Frame(root)
btn_frame.pack(pady=10)

ttk.Button(btn_frame, text="+", command=lambda: calculate("add")).grid(row=0, column=0, padx=5)
ttk.Button(btn_frame, text="-", command=lambda: calculate("subtract")).grid(row=0, column=1, padx=5)
ttk.Button(btn_frame, text="×", command=lambda: calculate("multiply")).grid(row=0, column=2, padx=5)
ttk.Button(btn_frame, text="÷", command=lambda: calculate("divide")).grid(row=0, column=3, padx=5)

result_var = tk.StringVar()
result_label = ttk.Label(root, textvariable=result_var, font=("Arial", 12))
result_label.pack(pady=10)

ttk.Button(root, text="Clear", command=clear_fields).pack(pady=5)
ttk.Button(root, text="Exit", command=root.destroy).pack(pady=5)

root.mainloop()
