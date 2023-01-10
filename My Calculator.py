from tkinter import *


def button_press(num):
    global equation_text
    equation_text = equation_text + str(num)
    equation_label.set(equation_text)


def equals():
    global equation_text
    try:
        total = str(eval(equation_text))
        equation_label.set(total)
        # To reuse the total obtained:
        equation_text = total
    except ZeroDivisionError:
        equation_label.set("Math Error!")
        equation_text = ""
    except SyntaxError:
        equation_label.set("Syntax Error!")
        equation_text = ""


def clear():
    global equation_text
    equation_label.set("")  # To clear the label
    equation_text = ""


window = Tk()
window.title("My Calculator")
window.geometry("500x500")
icon = PhotoImage(file='calc.png')
window.iconphoto(True, icon)
window.config(background='#133175')

equation_text = ""
equation_label = StringVar()

label = Label(window, textvariable=equation_label, font=('Comic Sans', 20), fg='#00FF00', bg='black',
              relief=RAISED, bd=5, padx=10, pady=10,
              width=24, height=2)
label.pack()
frame = Frame(window)
frame.pack()

# Adding the buttons to the frame ;by use of grid to properly place them
button1 = Button(frame, text=1, height=4, width=9, fg='white', bg='#24499e', activeforeground='white',
                 activebackground='#24499e',
                 font=35, command=lambda: button_press(1))

button1.grid(row=0, column=0)

button2 = Button(frame, text=2, height=4, width=9, fg='white', bg='#24499e', activeforeground='white',
                 activebackground='#24499e',
                 font=35, command=lambda: button_press(2))

button2.grid(row=0, column=1)

button3 = Button(frame, text=3, height=4, width=9, fg='white', bg='#24499e', activeforeground='white',
                 activebackground='#24499e',
                 font=35, command=lambda: button_press(3))

button3.grid(row=0, column=2)

button4 = Button(frame, text=4, height=4, width=9, fg='white', bg='#24499e', activeforeground='white',
                 activebackground='#24499e',
                 font=35, command=lambda: button_press(4))

button4.grid(row=1, column=0)

button5 = Button(frame, text=5, height=4, width=9, fg='white', bg='#24499e', activeforeground='white',
                 activebackground='#24499e',
                 font=35, command=lambda: button_press(5))

button5.grid(row=1, column=1)

button6 = Button(frame, text=6, height=4, width=9, fg='white', bg='#24499e', activeforeground='white',
                 activebackground='#24499e',
                 font=35, command=lambda: button_press(6))

button6.grid(row=1, column=2)

button7 = Button(frame, text=7, height=4, width=9, fg='white', bg='#24499e', activeforeground='white',
                 activebackground='#24499e',
                 font=35, command=lambda: button_press(7))

button7.grid(row=2, column=0)

button8 = Button(frame, text=8, height=4, width=9, fg='white', bg='#24499e', activeforeground='white',
                 activebackground='#24499e',
                 font=35, command=lambda: button_press(8))

button8.grid(row=2, column=1)

button9 = Button(frame, text=9, height=4, width=9, fg='white', bg='#24499e', activeforeground='white',
                 activebackground='#24499e',
                 font=35, command=lambda: button_press(9))

button9.grid(row=2, column=2)

button1 = Button(frame, text=0, height=4, width=9, fg='white', bg='#24499e', activeforeground='white',
                 activebackground='#24499e',
                 font=35, command=lambda: button_press(0))

button1.grid(row=3, column=0)

plus = Button(frame, text='+', height=4, width=9, fg='black', bg='#24499e', activeforeground='black',
              activebackground='#24499e',
              font=35, command=lambda: button_press('+'))

plus.grid(row=0, column=3)

minus = Button(frame, text='-', height=4, width=9, fg='black', bg='#24499e', activeforeground='black',
               activebackground='#24499e',
               font=35, command=lambda: button_press('-'))

minus.grid(row=1, column=3)

multiply = Button(frame, text='x', height=4, width=9, fg='black', bg='#24499e', activeforeground='black',
                  activebackground='#24499e',
                  font=35, command=lambda: button_press('*'))

multiply.grid(row=2, column=3)

divide = Button(frame, text='/', height=4, width=9, fg='black', bg='#24499e', activeforeground='black',
                activebackground='#24499e',
                font=35, command=lambda: button_press('/'))

divide.grid(row=3, column=3)

equal = Button(frame, text='=', height=4, width=9, fg='#2ad413', bg='#24499e', activeforeground='#2ad413',
               activebackground='#24499e',
               font=35, command=equals)

equal.grid(row=3, column=2)

decimal = Button(frame, text='.', height=4, width=9, fg='black', bg='#24499e', activeforeground='black',
                 activebackground='#24499e',
                 font=35, command=lambda: button_press('.'))

decimal.grid(row=3, column=1)

clearButton = Button(window, text="Clear", width=12, height=4,
                     fg="red", activeforeground="red", command=clear)
clearButton.pack()

window.mainloop()
