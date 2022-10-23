from tkinter import *
from tkinter import ttk

root = Tk()


class Bmi:
    def __init__(self, master):
        master.title("BMI Calculator")
        master.geometry('300x150')

        Label(master, text="Enter your height").pack()
        self.height_entry = ttk.Entry(master)
        self.height_entry.pack()

        Label(master, text="Enter you weight").pack()
        self.kg_entry = ttk.Entry(master)
        self.kg_entry.pack()

        Button(master, text="Calculate BMI", command=self.calculate).pack()
        master.bind('<Return>', self.calculate)
        self.label = Label(master, text=f"Your BMI is : \n")
        self.label.pack()

    def calculate(self, event=None):
        m = int(self.height_entry.get()) / 100
        kg = int(self.kg_entry.get())
        bmi_calc = kg / (m * m)
        self.label['text'] = f'Your BMI is : \n{bmi_calc:.2f}'


bmi = Bmi(root)
root.mainloop()
