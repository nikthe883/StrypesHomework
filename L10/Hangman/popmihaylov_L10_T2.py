import os
from tkinter import *
import tkinter as tk
from string import ascii_uppercase
import random

root = Tk()

# class for new window when the game is won io lost
class Window:
    def __init__(self, master, state, word):
        self.master = master
        self.frame = tk.Frame(master)
        master.title(f"You {state}")
        master.geometry('215x200')
        if state == "WON":
            Label(master, text=f"CONGRATS, YOU {state} !", font="Helvetica 12 bold").grid(row=0, column=0, sticky="NSWE", pady=10, padx=10)
            Label(master, text=f"You guessed the word \n {word} !", font="Helvetica 12 bold").grid(row=1, column=0, sticky="NSWE", pady=10, padx=10)
        else:
            Label(master, text=f"SORRY, YOU {state} !", font="Helvetica 12 bold").grid(row=0, column=0, sticky="NSWE", pady=10, padx=10)
            Label(master, text=f"The word was \n {word} !", font="Helvetica 12 bold").grid(row=1, column=0, sticky="NSWE", pady=10, padx=10)

        Button(master, text="Play Again", command=lambda: self.play_again(), font="Helvetica 12 bold").grid(row=2, column=0, sticky="NSWE", pady=10)
        Button(master, text="   Quit   ", command=lambda: exit(), font="Helvetica 12 bold").grid(row=3, column=0, sticky="NSWE", pady=10)

    def play_again(self):
        self.master.destroy()
        Hangman(root)


class Hangman:
    def __init__(self, master):
        master.title("Hangman")
        # initialize the variables
        self.master = master
        self.buttons = []
        self.the_word_with_space = ""
        self.number_guesses = 0
        self.guessed = []
        self.win = None
        self.photos = []
        self.image_label = Label(master)
        self.load_photos()
        self.word_list = ["BIRD", "HOUSE", "PANDA", "COMPUTER", "JAVASCRIPT", "JAVA", "DESK", "MOUSE", "PYTHON", "SOMETHING"]
        self.count = 1
        self.label_word = StringVar(root, value="")
        Label(self.master, textvariable=self.label_word, font="Consolas 24 bold").grid(row=0, column=3, columnspan=6, pady=20)
        self.label_count_tip = StringVar(root, value=f"Tips left\n {self.count}")
        Label(self.master, textvariable=self.label_count_tip, font="Consolas 12 bold").grid(row=0, column=8, padx=10)

        # start the game
        self.new_game()
        # load images
        self.image_label.grid(row=0, column=0, columnspan=3, padx=10, pady=40)
        self.image_label.config(image=self.photos[0])
        # load buttons
        self.load_buttons()
        # show additional buttons
        Button(master, text="").grid(row=3, column=8, sticky="NSWE")
        Button(master, text="Play Again", command=lambda: self.new_game(), font="Helvetica 12 bold").grid(row=4, column=5, columnspan=4, sticky="NSWE", pady=10)
        Button(master, text=f"Tips", command=lambda: self.tips(), font="Helvetica 12 bold").grid(row=4, column=0, columnspan=4, sticky="NSWE", pady=10)

    def tips(self):

        if self.count > 0:
            for i in range(len(list(self.the_word_with_space))):
                if self.guessed[i] == "_":
                    self.guessed[i] = self.the_word_with_space[i]
                    self.label_word.set("".join(self.guessed))
                    if self.label_word.get() == self.the_word_with_space:
                        self.win = True
                    break

            self.count -= 1
            self.label_count_tip.set(f"Tips left\n {self.count}")
        self.check_win()


    def new_game(self):
        self.count = 1
        self.label_count_tip.set(f"Tips left\n {self.count}")

        self.enable_buttons(self.buttons)
        self.image_label.config(image=self.photos[0])

        the_word = random.choice(self.word_list)
        self.the_word_with_space = " ".join(the_word)
        self.label_word.set(" ".join("_" * len(the_word)))
        self.guessed = list(self.label_word.get())
        self.guessed[0], self.guessed[-1] = self.the_word_with_space[0], self.the_word_with_space[-1]
        self.label_word.set("".join(self.guessed))

    def load_photos(self):
        for i in range(len(os.listdir('images'))):
            self.photos.append(PhotoImage(file=f'images/hang{i}.png', master=root))

    def guess(self, letter):

        if self.number_guesses < 11:
            word_to_guess = list(self.the_word_with_space)

            if letter in word_to_guess:
                for i in range(len(word_to_guess)):

                    if word_to_guess[i] == letter:
                        self.guessed[i] = letter
                    self.label_word.set("".join(self.guessed))

                    if self.label_word.get() == self.the_word_with_space:
                        self.win = True

            else:
                self.number_guesses += 1
                self.image_label.config(image=self.photos[self.number_guesses])
                if self.number_guesses == 11:
                    self.win = False

        self.check_win()

    def check_win(self):

        if self.win:
            new_window = tk.Toplevel(self.master)
            Window(new_window, state="WON", word=self.the_word_with_space)
            self.label_word.set("")
            self.win = None

        if self.win is False:
            new_window = tk.Toplevel(self.master)
            Window(new_window, state="LOST", word=self.the_word_with_space)
            self.label_word.set("")
            self.win = None

    def disable_buttons(self, index):
        self.buttons[index].config(state="disabled")

    def enable_buttons(self, btn_list):
        for i in btn_list:
            i.config(state="normal")

    def load_buttons(self):
        letters = ascii_uppercase
        for index in range(len(ascii_uppercase)):
            n = letters[index]
            btn = Button(self.master, text=n, state='active', command=lambda letter=n, i=index: [self.guess(letter), self.disable_buttons(i)],
                         font="Helvetica 18", width=4, pady=10, padx=10)
            btn.grid(row=1 + index // 9, column=index % 9)
            self.buttons.append(btn)


hangman = Hangman(root)
root.mainloop()
