import tkinter as tk
from tkinter import ttk, messagebox

#main window
root = tk.Tk()
root.geometry("800x800")
root.title("Palindrome Check")
root.resizable(True, True)

def show_result():
    given_str=given_string_entry.get()
    if len(given_str.strip())>0:
        result_str = given_str[::-1]
        reverse_label.config(text=result_str)
    else:
        messagebox.showwarning("Empty", "Input THAAAA")

    if given_str==result_str:
        messagebox.showinfo(result_str, "is Palindrome")
    else:
        messagebox.showinfo(f"{result_str} is Palindrome")

#UI component
pal_label = tk.Label(root, text="PALINDROME CHECK")
pal_label.grid(column=0, row=0, sticky=tk.W,padx=20, pady=20,columnspan=2)

given_string_label = tk.Label(root, text="GIVEN STRING")
given_string_label.grid(column=0, row=2, sticky=tk.W,padx=5, pady=5)

given_string_entry = ttk.Entry(root)
given_string_entry.grid(column=1, row=2, sticky=tk.W,padx=5, pady=5)

reverse_btn = tk.Button(root, text="REVERSE",command=show_result)
reverse_btn.grid(column=2, row=2, sticky=tk.W,padx=5, pady=5)

result_label = tk.Label(root, text="REVERESED STRING:")
result_label.grid(column=0, row=3, sticky=tk.W,padx=5, pady=5)

reverse_label = tk.Label(root, text="",font='helvetica 100 bold')
reverse_label.grid(column=1, row=3, sticky=tk.W,padx=5, pady=5,columnspan=2)

root.mainloop()
