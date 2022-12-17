from tkinter import *
app = Tk()

global op
global number1
number1 = 0

# insert the number which is clicked on the app
def enter(x):
    index = len(entry.get())
    entry.insert(index, str(x))

# hold the previous number, operation and clear screen
def hold_number_and_operation(x):
    global op
    global number1

    op = x
    number1 = float(entry.get())
    entry.delete(0, 'end')

# execute the given numbers and operation
def execute():
    if number1 and entry.get():
        number2 = float(entry.get())
        entry.delete(0, 'end')
        if op == 0: return entry.insert(0, str(number1+number2))
        elif op == 1: return entry.insert(0, str(number1-number2))
        elif op == 2: return entry.insert(0, str(number1*number2))
        elif op == 3: return entry.insert(0, str(number1/number2))

# clear screen
def clear():
    entry.delete(0, 'end')


# define app window with width and length
app.geometry("250x300")

# define the place where we see entered the numbers
entry = Entry(font="Verdana 14 bold", width=15, justify=RIGHT)
entry.place(x=20, y=20)

# define a button for every number 1-9
buttons = []
j = 0

for i in range(0,9):
    buttons.append(Button(text=str(i+1), font="Verdana 14 bold", 
            command=lambda x=i:enter(x)))

    buttons[i].place(x=20+(i%3)*50, y=50+(j%3)*50)
    if (i+1) % 3 == 0:
        j+=1

# define operation buttons
operations = ["+", "-", "x", "/"]
op_buttons = []

for i in range(0,4):
    op_buttons.append(Button(text=operations[i], font="Verdana 14 bold",
                    width=2, command=lambda x=i:hold_number_and_operation(x)))

    op_buttons[i].place(x=170, y=50+50*i)

# define other buttons
zero_button = Button(text="0", font="Verdana 14 bold", 
            command=lambda x=0:enter(x)).place(x=20, y=200)

decimal_button = Button(text=".", font="Verdana 14 bold", 
            command=lambda x=".":enter(x), width=2).place(x=70, y=200)

clear_button = Button(text="C", font="Verdana 14 bold", 
            command=clear, width=2).place(x=120, y=200)

equal_button = Button(text="=", fg="RED", font="Verdana 14 bold", 
            command=execute, width=10).place(x=20, y=250)

app.mainloop()