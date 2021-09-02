from tkinter import *

root = Tk()
root.title('Python Calculator')  # Window title for GUI
e = Entry(root, width=35, borderwidth=5)  # Entry window within GUI
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)  # Grid placement for calculator window


# Displaying the numerical value in the print window of the GUI


def button_click(number):
    current = e.get()  # Getting the initial click number
    e.delete(0, number)  # This statement deletes the entry to avoid a 'get' of multiple entries
    e.insert(0, str(current) + str(number))  # Adding the string values of the numbers for multiple digits


def button_clear():
    e.delete(0, END)


def button_add():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    e.delete(0, END)


def button_equal():
    second_number = e.get()  # This is same operation for each expression and needs to be outside each if statement
    e.delete(0, END)
    if math == "addition":   # Equal button evaluates expressions relative to the value of math
        e.insert(0, f_num + int(second_number))
    if math == "subtraction":
        e.insert(0, f_num - int(second_number))
    if math == "multiplication":
        e.insert(0, f_num * int(second_number))
    if math == "division":
        e.insert(0, f_num / int(second_number))


def button_multiply():
    first_number = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    e.delete(0, END)


def button_divide():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    e.delete(0, END)


def button_subtract():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    e.delete(0, END)


# Numerical buttons for the calculator


button_1 = Button(root, text='1', padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text='2', padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text='3', padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text='4', padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text='5', padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text='6', padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text='7', padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text='8', padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text='9', padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text='0', padx=40, pady=20, command=lambda: button_click(0))

# Operational buttons
button_add = Button(root, bg='blue', fg='white', text='+', padx=40, pady=20, command=button_add)
button_equal = Button(root, bg='blue', fg='white', text='=', padx=40, pady=20, command=button_equal)
button_clear = Button(root, bg='blue', fg='white', text='Clear', padx=40, pady=20, command=button_clear)
button_multiply = Button(root, bg='blue', fg='white', text='x', padx=40, pady=20, command=button_multiply)
button_divide = Button(root, bg='blue', fg='white', text='/', padx=40, pady=20, command=button_divide)
button_subtract = Button(root, bg='blue', fg='white', text='-', padx=40, pady=20, command=button_subtract)
# Placing the buttons on the screen
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=1)

# Operational buttons for the calculator
button_add.grid(row=3, column=3)
button_clear.grid(row=1, column=3, columnspan=1)  # These buttons are larger and span two columns
button_equal.grid(row=2, column=3, columnspan=1)
button_multiply.grid(row=4, column=3)
button_subtract.grid(row=4, column=2)
button_divide.grid(row=4, column=0)
root.mainloop()
