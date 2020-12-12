from tkinter import *


def buttonClick(number):
    global operator
    operator = operator + str(number)
    Text_Input.set(operator)


def clearWindow():
    global operator
    operator = ""
    Text_Input.set("")


def equalSign():
    global operator
    final = str(eval(operator))
    Text_Input.set(final)
    operator=""


calculator = Tk();
calculator.title("Python Calculator")
operator = ""
Text_Input =StringVar()


txtDisplay = Entry(calculator, font=('Times New Roman', 15), textvariable=Text_Input,
                   bd=4, insertwidth=6, justify='right').grid(columnspan=4)
b7 = Button(calculator, font=('Times New Roman', 10, 'bold'), text="7", bd=4,
            padx=15, command=lambda: buttonClick(7)).grid(row=1, column=0)
b8 = Button(calculator, font=('Times New Roman', 10, 'bold'), text="8", bd=4,
            padx=15, command=lambda: buttonClick(8)).grid(row=1, column=1)
b9 = Button(calculator, font=('Times New Roman', 10, 'bold'), text="9", bd=4,
            padx=15, command=lambda: buttonClick(9)).grid(row=1, column=2)
bdiv = Button(calculator, font=('Times New Roman', 10, 'bold'), text="/", bd=4,
              padx=15, command=lambda: buttonClick("/")).grid(row=1, column=3)

b4 = Button(calculator, font=('Times New Roman', 10, 'bold'), text="4", bd=4,
            padx=15, command=lambda: buttonClick(4)).grid(row=2, column=0)
b5 = Button(calculator, font=('Times New Roman', 10, 'bold'), text="5", bd=4,
            padx=15, command=lambda: buttonClick(5)).grid(row=2, column=1)
b6 = Button(calculator, font=('Times New Roman', 10, 'bold'), text="6", bd=4,
            padx=15, command=lambda: buttonClick(6)).grid(row=2, column=2)
bmul = Button(calculator, font=('Times New Roman', 10, 'bold'), text="*", bd=4,
              padx=15, command=lambda: buttonClick("*")).grid(row=2, column=3)

b1 = Button(calculator, font=('Times New Roman', 10, 'bold'), text="1", bd=4,
            padx=15, command=lambda: buttonClick(1)).grid(row=3, column=0)
b2 = Button(calculator, font=('Times New Roman', 10, 'bold'), text="2", bd=4,
            padx=15, command=lambda: buttonClick(2)).grid(row=3, column=1)
b3 = Button(calculator, font=('Times New Roman', 10, 'bold'), text="3", bd=4,
            padx=15, command=lambda: buttonClick(3)).grid(row=3, column=2)
bsub = Button(calculator, font=('Times New Roman', 10, 'bold'), text="-", bd=4,
              padx=15, command=lambda: buttonClick("-")).grid(row=3, column=3)

b0 = Button(calculator, font=('Times New Roman', 10, 'bold'), text="0", bd=4,
            padx=15, command=lambda: buttonClick(0)).grid(row=4, column=0)
bclr = Button(calculator, font=('Times New Roman', 10, 'bold'), text="C", bd=4,
              padx=15, command=clearWindow).grid(row=4, column=1)
beql = Button(calculator, font=('Times New Roman', 10, 'bold'), text="=", bd=4,
              padx=15, command=equalSign).grid(row=4, column=2)
badd = Button(calculator, font=('Times New Roman', 10, 'bold'), text="+", bd=4,
              padx=15, command=lambda: buttonClick("+")).grid(row=4, column=3)

calculator.mainloop()
