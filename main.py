from tkinter import *
from tkinter import messagebox

opps = ['+', '-', '*', '/']
root = Tk()
root.geometry("240x340")
root.title("Calculator")
root.resizable(width=False, height=False)


def add_number(num):
    val = calc.get()
    if val[0] == '0':
        val = val[1:]
    calc.delete(0, END)
    calc.insert(0, val + num)


def add_op(op):
    val = calc.get()
    if val[-1] in opps:
        val = val[:-1]
    calc.delete(0, END)
    calc.insert(0, val + op)


def make_num_button(num):
    return Button(text=num, bg='lime', fg='black', bd=5, font=('Arial', 12), command=lambda: add_number(num))


def make_dop_button(num):
    return Button(text=num, bg='cyan', fg='black', bd=5, font=('Arial', 12), command=lambda: add_number(num))


def make_op_button(op):
    return Button(text=op, bg='blue', fg='white', bd=5, font=('Arial', 12), command=lambda: add_op(op))


def calculate():
    val = calc.get()
    if val[-1] in opps:
        val = val + val[:-1]
    calc.delete(0, END)
    try:
        calc.insert(0, eval(val))
    except:
        messagebox.showerror('Error!', 'Incorrect Input')
        calc.insert(0, '0')


def delete():
    calc.delete(0, END)
    calc.insert(0, '0')


def delete_one():
    val = calc.get()
    val = val[:-1]
    calc.delete(0, END)
    calc.insert(END, val)
    if len(val) <= 0:
        calc.insert(0, '0')


def make_cls_button(C):
    return Button(text=C, bg='yellow', fg='black', bd=5, font=('Arial', 12), command=lambda: delete())


def make_del_button(delete):
    return Button(text=delete, bg='yellow', fg='black', bd=5, font=('Arial', 12), command=lambda: delete_one())


def make_calc(op):
    return Button(text=op, bg='red', fg='white', bd=5, font=('Arial', 12), command=calculate)


root["bg"] = 'black'
calc = Entry(root, justify=RIGHT, font=('Arial', 15), width=15, bg='cyan', fg='black')
calc.insert(0, '0')
calc.grid(row=0, column=0, columnspan=4, stick='we', padx=5, pady=5)
make_num_button('1').grid(row=1, column=0, stick='wens', padx=5, pady=5)
make_num_button('2').grid(row=1, column=1, stick='wens', padx=5, pady=5)
make_num_button('3').grid(row=1, column=2, stick='wens', padx=5, pady=5)
make_num_button('4').grid(row=2, column=0, stick='wens', padx=5, pady=5)
make_num_button('5').grid(row=2, column=1, stick='wens', padx=5, pady=5)
make_num_button('6').grid(row=2, column=2, stick='wens', padx=5, pady=5)
make_num_button('7').grid(row=3, column=0, stick='wens', padx=5, pady=5)
make_num_button('8').grid(row=3, column=1, stick='wens', padx=5, pady=5)
make_num_button('9').grid(row=3, column=2, stick='wens', padx=5, pady=5)
make_num_button('0').grid(row=4, column=0, stick='wens', padx=5, pady=5)
make_dop_button('.').grid(row=5, column=1, stick='wens', padx=5, pady=5)
make_dop_button('(').grid(row=5, column=2, stick='wens', padx=5, pady=5)
make_dop_button(')').grid(row=5, column=3, stick='wens', padx=5, pady=5)
make_op_button('+').grid(row=4, column=1, stick='wens', padx=5, pady=5)
make_op_button('-').grid(row=4, column=2, stick='wens', padx=5, pady=5)
make_op_button('*').grid(row=4, column=3, stick='wens', padx=5, pady=5)
make_op_button('/').grid(row=3, column=3, stick='wens', padx=5, pady=5)
make_calc('=').grid(row=5, column=0, stick='wens', padx=5, pady=5)
make_cls_button('C').grid(row=1, column=3, stick='wens', padx=5, pady=5)
make_del_button('del').grid(row=2, column=3, stick='wens', padx=5, pady=5)

root.grid_columnconfigure(0, minsize=60)
root.grid_columnconfigure(1, minsize=60)
root.grid_columnconfigure(2, minsize=60)
root.grid_columnconfigure(3, minsize=60)

root.rowconfigure(1, minsize=60)
root.rowconfigure(2, minsize=60)
root.rowconfigure(3, minsize=60)
root.rowconfigure(4, minsize=60)
root.rowconfigure(5, minsize=60)
root.rowconfigure(6, minsize=60)

root.mainloop()
