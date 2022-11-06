import tkinter
from database import *
from tkinter import *
from tkinter import scrolledtext
from PIL import ImageTk, Image
from tkinter import filedialog
root = Tk()



class App:
    def __init__(self, master):
        self.master = master
        master.title("Collection Manager")
        self.db = Database("books")
        self.db1 = Database("movies")
        self.db2 = Database("games")
        self.db3 = Database("books")
        self.list_box_frame = Frame(self.master)
        self.list_box_frame.grid(row=1, column=0)
        self.load_list_box()
        self.filename = ""
        self.search_trigger = False
        self.drop_down()


    def drop_down(self):
        list_option = Frame(self.master)
        list_option.grid(row=0, column=1)
        options = [
            "Movies",
            "Books",
            "Games",
        ]
        menu = StringVar()
        menu.set("Select type of collection")

        drop = OptionMenu(list_option, menu, *options)
        drop.grid(row=0, column=1)
        def get_type_of_selection():
            if menu.get() == "Movies":
                self.db = self.db1
                self.load_list_box()
            if menu.get() == "Books":
                self.db = self.db3
                self.load_list_box()
            if menu.get() == "Games":
                self.db = self.db2
                self.load_list_box()
        tkinter.Button(list_option, text="Get", command=get_type_of_selection).grid(column=1, row=2)




    def load_list_box(self):
        self.list_box = tkinter.Listbox(self.master, font=("Times New Roman", 15))
        self.list_box.grid(row=0, column=0)
        for i in self.db.show().items():
            self.list_box.insert(END, i[0], )



        button = tkinter.Button(self.list_box_frame, text="Get", command=self.ret, font=("Times New Roman", 15))
        button.grid(row=0, column=0)
        button = tkinter.Button(self.list_box_frame, text="Create", command=self.create, font=("Times New Roman", 15))
        button.grid(row=0, column=1)
        button = tkinter.Button(self.list_box_frame, text="Search", command=self.search, font=("Times New Roman", 15))
        button.grid(row=0, column=2)



    def ret(self, get = None):
        retrieve = Toplevel(self.master)
        ret_frame = Frame(retrieve)
        ret_frame.grid(row=0, column=1)
        functions_frame = Frame(retrieve)
        functions_frame.grid(row=1, column=1)
        if not self.search_trigger:
            self.searched = self.db.search(self.list_box.get(self.list_box.curselection()))
            self.picked = self.list_box.get(self.list_box.curselection())
            print(self.searched)
            retrieve.title(self.picked)
        if self.search_trigger:
            self.searched = self.db.search(get)


        self.values = list(self.searched.values())
        keys = list(self.searched.keys())
        len_of_values = len(self.values)

        for i in range(len(self.values)):
            text = Label(ret_frame, text=f"{keys[i].upper()}", font=("Times New Roman", 15),  wraplengt=400,  borderwidth=2)
            text.grid(row=i, column=0)
            if keys[i] == "picture":
                try:
                    image = Image.open(f"{str(self.values[i])}")
                    image = image.resize((50, 50))
                    image1 = ImageTk.PhotoImage(image)
                    text1 = Label(ret_frame, image=image1, pady=10)
                    text1.image = image1

                except (FileNotFoundError, AttributeError):
                    image = Image.open(r'images/images.jpg')
                    image = image.resize((50, 50))
                    image1 = ImageTk.PhotoImage(image)

                    text1 = Label(ret_frame, image=image1, pady=10)
                    text1.image = image1
            else:

                text1 = Label(ret_frame, text=f"{self.values[i]}", font=("Times New Roman", 15), wraplengt=400, pady=10)
            text1.grid(row=i, column=1)


        button = tkinter.Button(functions_frame, text="Update", command=self.update_function, font=("Times New Roman", 15))
        button.grid(row=len_of_values + 1, column=0)

        button = tkinter.Button(functions_frame, text="Delete", command=self.delete_function, font=("Times New Roman", 15))
        button.grid(row=len_of_values + 1, column=1)


    def update_function(self):
        update_window = Toplevel(self.master)
        update_window.title("Update")



        tkinter.Label(update_window, text="Update Database", font=("Times New Roman", 15)).grid(column=0, row=0)
        tkinter.Label(update_window, text="Update title", font=("Bold", 12)).grid(column=0, row=1)
        text_area_title = scrolledtext.ScrolledText(update_window, wrap=tkinter.WORD,
                                                    width=20, height=3,
                                                    font=("Times New Roman", 15))
        text_area_title.insert(INSERT, self.picked)
        text_area_title.grid(column=0, row=2, pady=10, padx=10)

        tkinter.Label(update_window, text="Update producer name ", font=("Bold", 12)).grid(column=0, row=3)
        text_area_producer = scrolledtext.ScrolledText(update_window, wrap=tkinter.WORD,
                                              width=20, height=3,
                                              font=("Times New Roman", 15))
        text_area_producer.insert(INSERT, self.values[0])
        text_area_producer.grid(column=0, row=4, pady=10, padx=10)

        tkinter.Label(update_window, text="Update description", font=("Bold", 12)).grid(column=0, row=5)
        text_area_description = scrolledtext.ScrolledText(update_window, wrap=tkinter.WORD,
                                                       width=20, height=3,
                                                       font=("Times New Roman", 15))
        text_area_description.insert(INSERT, self.values[1])
        text_area_description.grid(column=0, row=6, pady=10, padx=10)

        tkinter.Label(update_window, text="Update genre", font=("Bold", 12)).grid(column=0, row=7)
        text_area_genre = scrolledtext.ScrolledText(update_window, wrap=tkinter.WORD,
                                                       width=20, height=3,
                                                       font=("Times New Roman", 15))

        text_area_genre.insert(INSERT, self.values[2])
        text_area_genre.grid(column=0, row=8, pady=10, padx=10)

        tkinter.Label(update_window, text="Update year of creation", font=("Bold", 12)).grid(column=0, row=9)
        text_area_year = scrolledtext.ScrolledText(update_window, wrap=tkinter.WORD,
                                                       width=20, height=3,
                                                       font=("Times New Roman", 15))
        text_area_year.insert(INSERT, self.values[3])
        text_area_year.grid(column=0, row=10, pady=10, padx=10)

        def browseFiles():
            self.filename = filedialog.askopenfilename(initialdir="/",
                                                  title="Select a File",
                                                  filetypes=(("jpeg files",
                                                              "*.jpg"),
                                                             ("all files",
                                                              "*.*")))


        button_explore = Button(update_window,
                                text="Select image",
                                command=browseFiles)


        button_explore.grid(column=0, row=11)

        def get_input_producer():
            return text_area_producer.get(1.0, 'end-1c')

        def get_input_description():
            return text_area_description.get(1.0, 'end-1c')

        def get_genre_input():
            return text_area_genre.get(1.0, 'end-1c')

        def year_input():
            return text_area_year.get(1.0, 'end-1c')

        def get_path_image():
            return self.filename

        def close():
            update_window.destroy()

        def get_input_title():
            return text_area_title.get(1.0, 'end-1c')


        def update_the_result():
            new_title = get_input_title()
            new_producer = get_input_producer()
            new_description = get_input_description()
            new_genre = get_genre_input()
            new_year = year_input()
            picture_path = get_path_image()

            updated_dict = {new_title: {"producer": new_producer,
                                          "description": new_description,
                                          "genre": new_genre,
                                          "year": new_year,
                                          "picture": picture_path
                                          }}
            print(updated_dict)

            self.db.update_existing_to_file(updated_dict,self.picked)
            self.db.write_to_file()
            self.load_list_box()

        tkinter.Button(update_window, text="Save", command=lambda: [update_the_result(), close()]).grid(column=0, row=12)

    def create(self):
        update_window = Toplevel(self.master)
        update_window.title("Create")

        tkinter.Label(update_window, text="Create new instance", font=("Times New Roman", 15)).grid(column=0, row=0)
        tkinter.Label(update_window, text="Write title ", font=("Bold", 12)).grid(column=0, row=1)
        text_area_title = scrolledtext.ScrolledText(update_window, wrap=tkinter.WORD,
                                                       width=20, height=3,
                                                       font=("Times New Roman", 15))
        text_area_title.grid(column=0, row=2, pady=10, padx=10)

        tkinter.Label(update_window, text="Write producer name ", font=("Bold", 12)).grid(column=0, row=3)
        text_area_producer = scrolledtext.ScrolledText(update_window, wrap=tkinter.WORD,
                                                       width=20, height=3,
                                                       font=("Times New Roman", 15))
        text_area_producer.grid(column=0, row=4, pady=10, padx=10)

        tkinter.Label(update_window, text="Write description", font=("Bold", 12)).grid(column=0, row=5)
        text_area_description = scrolledtext.ScrolledText(update_window, wrap=tkinter.WORD,
                                                          width=20, height=3,
                                                          font=("Times New Roman", 15))
        text_area_description.grid(column=0, row=6, pady=10, padx=10)

        tkinter.Label(update_window, text="Write genre", font=("Bold", 12)).grid(column=0, row=7)
        text_area_genre = scrolledtext.ScrolledText(update_window, wrap=tkinter.WORD,
                                                    width=20, height=3,
                                                    font=("Times New Roman", 15))

        text_area_genre.grid(column=0, row=8, pady=10, padx=10)

        tkinter.Label(update_window, text="Write production year", font=("Bold", 12)).grid(column=0, row=9)
        text_area_year = scrolledtext.ScrolledText(update_window, wrap=tkinter.WORD,
                                                   width=20, height=3,
                                                   font=("Times New Roman", 15))
        text_area_year.grid(column=0, row=10, pady=10, padx=10)

        def browseFiles():
            self.filename = filedialog.askopenfilename(initialdir="/",
                                                       title="Select a File",
                                                       filetypes=(("jpeg files",
                                                                   "*.jpg"),
                                                                  ("all files",
                                                                   "*.*")))

        button_explore = Button(update_window,
                                text="Select image",
                                command=browseFiles)

        button_explore.grid(column=0, row=11)
        def get_input_title():
            return text_area_title.get(1.0, 'end-1c')
        def get_input_producer():
            return text_area_producer.get(1.0, 'end-1c')

        def get_input_description():
            return text_area_description.get(1.0, 'end-1c')

        def get_genre_input():
            return text_area_genre.get(1.0, 'end-1c')

        def year_input():
            return text_area_year.get(1.0, 'end-1c')

        def get_path_image():
            return self.filename

        def close():
            update_window.destroy()

        def create_the_result():
            new_title = get_input_title()
            new_producer = get_input_producer()
            new_description = get_input_description()
            new_genre = get_genre_input()
            new_year = year_input()
            picture_path = get_path_image()

            created_dict = {new_title: {"producer": new_producer,
                                          "description": new_description,
                                          "genre": new_genre,
                                          "year": new_year,
                                          "picture": picture_path
                                          }}

            self.db.add_new(created_dict)
            self.db.write_to_file()
            self.load_list_box()

        tkinter.Button(update_window, text="Save", command=lambda: [create_the_result(), close()]).grid(column=0, row=12)


    def delete_function(self):
        self.db.delete_from_file(self.picked)
        self.db.write_to_file()
        self.load_list_box()

    def search(self):
        update_window = Toplevel(self.master)
        update_window.title("Search")
        tkinter.Label(update_window, text="Search by name", font=("Times New Roman", 15)).grid(column=0, row=1)
        text_area_title = scrolledtext.ScrolledText(update_window, wrap=tkinter.WORD,
                                                    width=20, height=3,
                                                    font=("Times New Roman", 15))
        text_area_title.grid(column=0, row=2, pady=10, padx=10)

        def get_input_title():
            self.search_trigger = True

            return text_area_title.get(1.0, 'end-1c')

        tkinter.Button(update_window, text="Get", command=lambda :[self.ret(get=get_input_title())]).grid(column=0, row=12)

        self.search_trigger = False


bmi = App(root)
root.mainloop()
