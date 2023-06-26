from tkinter import *


class functions:
    def __init__(self, entry_widget):
        self.entry_widget = entry_widget

    def click(self):
        pass



class calculator:
    def __init__(self):
        self.window = Tk()
        self.window.title('title')
        self.window.geometry('277x370+320+120')
        self.window.resizable(False, False)
        self.operator = ""
        self.text_Input = StringVar()
        self.txtDisplay = None
        self.txtDisplay_image = None  # Initialize txtDisplay_image as None

        self.fun = functions(entry_widget=None)

    def label(self):
        self.txtDisplay_image = PhotoImage(file="images/search.png")
        self.myimage = Label(image=self.txtDisplay_image)
        self.myimage.place(x=3, y=20)

        self.txtDisplay = Entry(
            self.window,
            justify='right',
            font=('arial black', 15, 'bold'),
            width=15,
            border=0,
            highlightthickness=0,
            bg="#404040",
            fg="#000000"
        )
        self.txtDisplay.place(x=30, y=34)
        self.txtDisplay.config(bg="#404040", readonlybackground="#404040")
        self.txtDisplay.focus()

    def general_buttons(self):
        self.backspace_image = PhotoImage(file="images/backspace.png")
        self.b1 = Button(self.window, text='bsce', image=self.backspace_image, bg='gold', fg='black', font='Norasi',
                         command=self.fun.click)
        self.b1.place(x=216, y=80)

        self.division_image = PhotoImage(file="images/division.png")
        self.b2 = Button(self.window, text='div', image=self.division_image, bg='gold', fg='black', font='Norasi',
                         command=self.fun.click)
        self.b2.place(x=216, y=130)

        self.multiplication_image = PhotoImage(file="images/multiplication.png")
        self.b3 = Button(self.window, text='x', image=self.multiplication_image, bg='gold', fg='black', font='Norasi',
                         command=self.fun.click)
        self.b3.place(x=216, y=180)

        self.subtraction_image = PhotoImage(file="images/subtraction.png")
        self.b4 = Button(self.window, text='-', image=self.subtraction_image, bg='gold', fg='black', font='Norasi',
                         command=self.fun.click)
        self.b4.place(x=216, y=230)

        self.addition_image = PhotoImage(file="images/addition.png")
        self.b5 = Button(self.window, text='+', image=self.addition_image, bg='gold', fg='black', font='Norasi',
                         command=self.fun.click)
        self.b5.place(x=216, y=280)

        self.equal_image = PhotoImage(file="images/equals.png")
        self.b6 = Button(self.window, text='=', image=self.equal_image, bg='gold', fg='black', font='Norasi',
                         command=self.fun.click)
        self.b6.place(x=216, y=330)

        self.clear_image = PhotoImage(file="images/clear.png")
        self.b7 = Button(self.window, text='c', image=self.clear_image, bg='gold', fg='black', font='Norasi',
                         command=self.fun.click)
        self.b7.place(x=145, y=80)

        self.root_image = PhotoImage(file="images/root.png")
        self.b8 = Button(self.window, text='2ryza', image=self.root_image, bg='gold', fg='black', font='Norasi',
                         command=self.fun.click)
        self.b8.place(x=145, y=130)

        self.dot_image = PhotoImage(file="images/dot.png")
        self.b9 = Button(self.window, text='.', image=self.dot_image, bg='gold', fg='black', font='Norasi',
                         command=self.fun.click)
        self.b9.place(x=74, y=330)

        self.square_image = PhotoImage(file="images/square2.png")
        self.b10 = Button(self.window, text='^', image=self.square_image, bg='gold', fg='black', font='Norasi',
                          command=self.fun.click)
        self.b10.place(x=74, y=130)

        self.percent_image = PhotoImage(file="images/percent.png")
        self.b11 = Button(self.window, text='%', image=self.percent_image, bg='gold', fg='black', font='Norasi',
                          command=self.fun.click)
        self.b11.place(x=74, y=80)

        self.sin_image = PhotoImage(file="images/sin.png")
        self.b12 = Button(self.window, text='%', image=self.sin_image, bg='gold', fg='black', font='Norasi',
                          command=self.fun.click)
        self.b12.place(x=3, y=80)

        self.cos_image = PhotoImage(file="images/cos.png")
        self.b13 = Button(self.window, text='%', image=self.cos_image, bg='gold', fg='black', font='Norasi',
                          command=self.fun.click)
        self.b13.place(x=3, y=130)

        self.pi_image = PhotoImage(file="images/pi.png")
        self.b14 = Button(self.window, text='1', image=self.pi_image, bg='gold', fg='black', font='Norasi',
                          command=self.fun.click)
        self.b14.place(x=145, y=330)

        # Rest of the button configurations...

    def numbers(self):
        self.fun = functions(entry_widget=self.txtDisplay)

        self.number9_image = PhotoImage(file="images/numbers/number9.png")
        self.b15 = Button(self.window, text='9', image=self.number9_image, bg='gold', fg='black', font='Norasi',
                          command=lambda: self.fun.entry_widget.insert(END, '9'))
        self.b15.place(x=145, y=180)

        self.number6_image = PhotoImage(file="images/numbers/number6.png")
        self.b16 = Button(self.window, text='6', image=self.number6_image, bg='gold', fg='black', font='Norasi',
                          command=lambda: self.fun.entry_widget.insert(END, '6'))
        self.b16.place(x=145, y=230)

        self.number3_image = PhotoImage(file="images/numbers/number3.png")
        self.b17 = Button(self.window, text='3', image=self.number3_image, bg='gold', fg='black', font='Norasi',
                          command=lambda: self.fun.entry_widget.insert(END, '3'))
        self.b17.place(x=145, y=280)

        self.number8_image = PhotoImage(file="images/numbers/number8.png")
        self.b18 = Button(self.window, text='8', image=self.number8_image, bg='gold', fg='black', font='Norasi',
                          command=lambda: self.fun.entry_widget.insert(END, '8'))
        self.b18.place(x=74, y=180)

        self.number5_image = PhotoImage(file="images/numbers/number5.png")
        self.b19 = Button(self.window, text='5', image=self.number5_image, bg='gold', fg='black', font='Norasi',
                          command=lambda: self.fun.entry_widget.insert(END, '5'))
        self.b19.place(x=74, y=230)

        self.number2_image = PhotoImage(file="images/numbers/number2.png")
        self.b20 = Button(self.window, text='2', image=self.number2_image, bg='gold', fg='black', font='Norasi',
                          command=lambda: self.fun.entry_widget.insert(END, '2'))
        self.b20.place(x=74, y=280)

        self.number7_image = PhotoImage(file="images/numbers/number7.png")
        self.b21 = Button(self.window, text='7', image=self.number7_image, bg='gold', fg='black', font='Norasi',
                          command=lambda: self.fun.entry_widget.insert(END, '7'))
        self.b21.place(x=3, y=180)

        self.number4_image = PhotoImage(file="images/numbers/number4.png")
        self.b22 = Button(self.window, text='4', image=self.number4_image, bg='gold', fg='black', font='Norasi',
                          command=lambda: self.fun.entry_widget.insert(END, '4'))
        self.b22.place(x=3, y=230)

        self.number1_image = PhotoImage(file="images/numbers/number1.png")
        self.b23 = Button(self.window, text='1', image=self.number1_image, bg='gold', fg='black', font='Norasi',
                         command=lambda: self.fun.entry_widget.insert(END, '1'))
        self.b23.place(x=3, y=280)

        self.number0_image = PhotoImage(file="images/numbers/number0.png")
        self.b24 = Button(self.window, text='0', image=self.number0_image, bg='gold', fg='black', font='Norasi',
                          command=lambda: self.fun.entry_widget.insert(END, '0'))
        self.b24.place(x=74, y=180)

    def run(self):
        self.label()
        self.general_buttons()
        self.numbers()
        self.window.mainloop()


calc = calculator()
calc.run()
