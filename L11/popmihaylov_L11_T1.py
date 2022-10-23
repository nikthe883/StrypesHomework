from tkinter import *
from math import prod, factorial

root = Tk()

class App:
    def __init__(self, master):

        self.master = master
        master.title("Calculator")

        self.value = ''
        self.memory_variable()
        self.input_field_display()
        self.load_buttons_numbers()

        self.memory = 0
        self.numbers = []
        self.result = 0

        self.change_sign_bool = False
        self.add = False
        self.subtract = False
        self.multiply = False
        self.divide = False
        self.root = False

    def load_buttons_numbers(self):
        button_frame = Frame(root)
        button_frame.grid(row=2, column=0)
        numbers = ["7", "4", "1", "8", "5", "2", "9", "6", "3"]

        for index in range(9):
            btn = Button(button_frame, text=numbers[index], command=lambda value=numbers[index]: self.insert_value(value), width=10, height=5, font='Helvetica 9 bold')
            btn.grid(padx=3, pady=3, row=index % 3, column=index // 3)

        zero = Button(button_frame, text="0", command=lambda: self.insert_value(0), width=10, height=5, font='Helvetica 9 bold')
        zero.grid(padx=5, pady=5, column=1, row=3)

        # clear entry
        Button(button_frame, text="C", command=lambda: self.clear_entry(), width=10, height=5, font='Helvetica 9 bold').grid(padx=5, pady=5, column=2, row=3)
        # clear all
        Button(button_frame, text="CE", command=lambda: self.clear_all(), width=10, height=5, font='Helvetica 9 bold').grid(padx=5, pady=5, column=2, row=4)
        # reverse sign
        Button(button_frame, text="+/-", command=lambda: self.change_sign(), width=10, height=5, font='Helvetica 9 bold').grid(padx=5, pady=5, column=0, row=3)
        # plus
        Button(button_frame, text="+", command=lambda: self.add_numbers(), width=10, height=5, font='Helvetica 9 bold').grid(padx=5, pady=5, column=4, row=0)
        # minus
        Button(button_frame, text="-", command=lambda: self.subtract_numbers(), width=10, height=5, font='Helvetica 9 bold').grid(padx=5, pady=5, column=4, row=1)
        # divide
        Button(button_frame, text="/", command=lambda: self.divide_numbers(), width=10, height=5, font='Helvetica 9 bold').grid(padx=5, pady=5, column=4, row=2)
        # multiply
        Button(button_frame, text="*", command=lambda: self.multiply_numbers(), width=10, height=5, font='Helvetica 9 bold').grid(padx=5, pady=5, column=4, row=3)
        # equals
        Button(button_frame, text="=", command=lambda: self.equals(), width=10, height=5, font='Helvetica 9 bold').grid(padx=5, pady=5, column=4, row=4)
        # root
        Button(button_frame, text="x2", command=lambda: self.root_numbers(), width=10, height=5, font='Helvetica 9 bold').grid(padx=5, pady=5, column=0, row=4)
        # factorial
        Button(button_frame, text="x!", command=lambda: self.factorial_numbers(), width=10, height=5, font='Helvetica 9 bold').grid(padx=5, pady=5, column=1, row=4)

        # memory frame
        memory_frame = Frame(root)
        memory_frame.grid(row=1, column=0)

        # memory clear
        Button(memory_frame, text="mc", command=lambda: self.memory_clear(), width=10, height=5, font='Helvetica 9 bold').grid(padx=5, pady=5, column=0, row=0)
        # memory plus
        Button(memory_frame, text="m+", command=lambda: self.memory_plus(), width=10, height=5, font='Helvetica 9 bold').grid(padx=5, pady=5, column=1, row=0)
        # memory minus
        Button(memory_frame, text="m-", command=lambda: self.memory_minus(), width=10, height=5, font='Helvetica 9 bold').grid(padx=5, pady=5, column=2, row=0)
        # memory recall
        Button(memory_frame, text="mr", command=lambda: self.memory_recall(), width=10, height=5, font='Helvetica 9 bold').grid(padx=5, pady=5, column=3, row=0)

        # memory label
        Label(self.master, text="Memory", padx=5, pady=5, width=10, height=5, font='Helvetica 9 bold').grid(column=2, row=0)
        Label(self.master, textvariable=self.memory_value, padx=5, pady=5, width=10, height=5, font='Helvetica 9 bold').grid(column=2, row=1)

    def insert_value(self, value):
        self.value += str(value)

        if self.change_sign_bool:
            self.text.set(f"-{self.value}")

        else:
            self.text.set(self.value)

    def input_field_display(self):
        self.input_frame = Frame(self.master, highlightbackground="black", highlightcolor="black", highlightthickness=1)
        self.input_frame.grid(row=0, column=0)

        self.text = StringVar()
        self.input_field = Entry(self.input_frame, textvariable=self.text, font=('arial', 18, 'bold'), bd=4, justify=RIGHT)
        self.input_field.grid(row=0, column=0)

    def memory_variable(self):
        self.memory_value = StringVar()
        self.memory_value.set("")

    def memory_clear(self):
        self.memory_value.set("")

    def memory_plus(self):
        self.memory += int(self.text.get())
        self.memory_value.set(str(self.memory))

    def memory_minus(self):
        self.memory -= int(self.text.get())
        self.memory_value.set(str(self.memory))

    def memory_recall(self):
        self.text.set(str(self.memory))

    def change_sign(self):
        check = self.text.get()
        if check[0] == "-":
            self.change_sign_bool = False
            self.text.set(f"{self.value}")
        else:
            self.change_sign_bool = True
            self.text.set(f"-{self.value}")

    def clear_entry(self):
        self.text.set("")
        self.value = ''

    def clear_all(self):
        self.text.set("")
        self.value = ''
        self.numbers = []

    def add_numbers(self):
        if self.value != "":
            self.numbers.append(self.text.get())
        self.text.set("")
        self.value = ""
        self.add = True
        print(self.numbers)

    def subtract_numbers(self):
        if self.value != "":
            if len(self.numbers) >= 1:
                self.numbers.append("-" + self.text.get())
            else:
                self.numbers.append(self.text.get())
        self.text.set("")
        self.value = ""
        self.subtract = True
        print(self.numbers)

    def multiply_numbers(self):
        if self.value != "":
            self.numbers.append(self.text.get())
        self.text.set("")
        self.value = ""
        self.multiply = True
        print(self.numbers)

    def divide_numbers(self):
        if self.value != "":
            self.numbers.append(self.text.get())
        self.text.set("")
        self.value = ""
        self.divide = True
        print(self.numbers)

    def root_numbers(self):
        result = pow(int(self.text.get()), 2)
        if result // 1 == result:
            result = int(result)

        self.text.set(str(result))
        self.numbers = (str(result))
        self.value = ""

    def factorial_numbers(self):
        try:
            result = factorial(int(self.text.get()))
            self.text.set(str(result))
            self.numbers = (str(result))
            self.value = ""
        except ValueError:
            self.text.set('0')
            self.value = ""

    def equals(self):
        result = 0
        if self.add:
            if len(self.numbers) == 1:
                result = int(self.numbers[0]) + int(self.text.get())
            elif len(self.numbers) > 1:
                if self.text.get() != "":
                    self.numbers.append(self.text.get())
                result = sum([int(x) for x in self.numbers])
            self.add = False

        if self.subtract:
            if len(self.numbers) == 1:
                result = int(self.numbers[0]) - int(self.text.get())
                print(self.text.get())
            elif len(self.numbers) > 1:
                if self.text.get() != "":
                    self.numbers.append("-" + self.text.get())
                result = sum([int(x) for x in self.numbers])

        if self.multiply:
            if len(self.numbers) == 1:
                result = int(self.numbers[0]) * int(self.text.get())
                print(self.text.get())
            elif len(self.numbers) > 1:
                if self.text.get() != "":
                    self.numbers.append(self.text.get())
                result = prod([int(x) for x in self.numbers])

        if self.divide:
            try:
                if len(self.numbers) == 1:
                    result = int(self.numbers[0]) / int(self.text.get())
                    if result // 1 == result:
                        result = int(result)
            except:
                self.text.set("Error")

        self.multiply = False
        self.subtract = False
        self.add = False
        self.divide = False
        self.text.set(str(result))
        self.numbers = [result]
        self.value = ''
        print(self.numbers, result)


bmi = App(root)
root.mainloop()
