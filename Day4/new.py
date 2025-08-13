import tkinter as tk
from tkinter import ttk, messagebox

root = tk.Tk()
root.geometry('440x300')
root.title("Largest Number")
root.resizable(0,0)

largest_among_two=tk.BooleanVar()
largest_among_two.set(False)
largest_among_three=tk.BooleanVar()
largest_among_three.set(False)

def largest_among_two_changed():
    configure_action_buttons()
    val=largest_among_two.get()
    if not val:
        l2_number1_entry.config(state=tk.DISABLED)
        l2_number2_entry.config(state=tk.DISABLED)
    else:
        l2_number1_entry.config(state=tk.NORMAL)
        l2_number2_entry.config(state=tk.NORMAL)
def largest_among_three_changed():
    configure_action_buttons()
    val=largest_among_three.get()
    if not val:
        l3_number1_entry.config(state=tk.DISABLED)
        l3_number2_entry.config(state=tk.DISABLED)
        l3_number3_entry.config(state=tk.DISABLED)
    else:
        l3_number1_entry.config(state=tk.NORMAL)
        l3_number2_entry.config(state=tk.NORMAL)
        l3_number3_entry.config(state=tk.NORMAL)
def configure_action_buttons():
    l3_val = largest_among_three.get()
    l2_val = largest_among_two.get()
    if(not l3_val) and not l2_val:
        result_btn.config(state=tk.DISABLED)
        reset_btn.config(state=tk.DISABLED)
    else:
        result_btn.config(state=tk.NORMAL)
        reset_btn.config(state=tk.NORMAL)
def reset_entries():
    l3_number1_entry.delete(0,'end')
    l3_number2_entry.delete(0,'end')
    l3_number3_entry.delete(0,'end')
    l2_number1_entry.delete(0,'end')
    l2_number2_entry.delete(0,'end')
def validate(entry):
    val=None
    try:
        val=int(entry.get())
    except ValueError as err:
        print(f'Error: {err}')
        print('ERROR')
        entry.delete(0,'end')
    return val


def show_result():
    l3=largest_among_three.get()
    l2=largest_among_two.get()
    if l3:
        l3_n1_val=validate(l3_number1_entry)
        l3_n2_val=validate(l3_number2_entry)
        l3_n3_val=validate(l3_number3_entry)
        if (l3_n1_val is not None and
            l3_n2_val is not None and
            l3_n3_val is not None):
            largest=max(l3_n1_val,l3_n2_val,l3_n3_val)
            messagebox.showinfo('Largest Among Three Numbers',
                            f"The largest number is: {largest}")
        else:
            messagebox.showerror('Largest Among Three Numbers',
                                 'All numbers should be integer values')
    if l2:
        l2_n1_val=validate(l2_number1_entry)
        l2_n2_val=validate(l2_number2_entry)
        if (l2_n1_val is not None and
            l2_n2_val is not None):
            largest=max(l2_n1_val,l2_n2_val)
            messagebox.showinfo('Largest Among Two Numbers',
                            f"The largest number is: {largest}")
        else:
            messagebox.showerror('Largest Among Two Numbers',
                                 'All numbers should be integer values')


l2_chk_bn = ttk.Checkbutton(root, text="Largest Among Two Numbers",
                             command=largest_among_two_changed,
                             variable=largest_among_two)
l2_chk_bn.grid(column=0, row=0,sticky=tk.W,padx=5,pady=5,columnspan=2)

l3_chk_bn=ttk.Checkbutton(root, text="Largest Among Three Numbers",
                          command=largest_among_three_changed,
                          variable=largest_among_three)
l3_chk_bn.grid(column=2, row=0,sticky=tk.W,padx=5,pady=5,columnspan=2)

# Generates a label and place that in grid location using <grid()> function
l2_number1_label = ttk.Label(root, text="Number1")
l2_number1_label.grid(column=0, row=1, sticky=tk.W, padx=20, pady=5)

# Generates a text box and place that in grid location using <grid()> function
# Text box will be disabled at the initial stage.
l2_number1_entry = ttk.Entry(root, state='disabled')
l2_number1_entry.grid(column=1, row=1, sticky=tk.W, padx=5, pady=5)

l2_number2_label = ttk.Label(root, text="Number2")
l2_number2_label.grid(column=0, row=2, sticky=tk.W, padx=20, pady=5)

l2_number2_entry = ttk.Entry(root, state='disabled')
l2_number2_entry.grid(column=1, row=2, sticky=tk.W, padx=5, pady=5)

# ====================================
# Widgets of Largest among three numbers.
# Three labels, three text box entries.
# ====================================
l3_number1_label = ttk.Label(root, text="Number1")
l3_number1_label.grid(column=2, row=1, sticky=tk.W, padx=5, pady=5)

l3_number1_entry = ttk.Entry(root, state='disabled')
l3_number1_entry.grid(column=3, row=1, padx=5, pady=5)

l3_number2_label = ttk.Label(root, text="Number2")
l3_number2_label.grid(column=2, row=2, sticky=tk.W, padx=5, pady=5)

l3_number2_entry = ttk.Entry(root, state='disabled')
l3_number2_entry.grid(column=3, row=2, padx=5, pady=5)

l3_number3_label = ttk.Label(root, text="Number3")
l3_number3_label.grid(column=2, row=3, sticky=tk.W, padx=5, pady=5)

l3_number3_entry = ttk.Entry(root, state='disabled')
l3_number3_entry.grid(column=3, row=3, padx=5, pady=5)

reset_btn = ttk.Button(root, text="Reset",command=reset_entries)
reset_btn.grid(column=1, row=4,sticky=tk.W,padx=5,pady=5)
reset_btn['state'] = tk.DISABLED

result_btn=ttk.Button(root, text="Result",command=show_result)
result_btn.grid(column=1, row=5,sticky=tk.W,padx=5,pady=5)
result_btn['state'] = tk.DISABLED
root.mainloop()