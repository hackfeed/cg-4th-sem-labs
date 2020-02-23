import tkinter as tk


class RootWindow:
    def __init__(self, top=None):
        img = tk.PhotoImage(file="assets/img/icon.png")

        top.geometry("800x600+298+48")
        top.minsize(1, 1)
        top.maxsize(1351, 738)
        top.resizable(0, 0)
        top.title("Triangle Magic")
        top.iconphoto(True, img)
        top.configure(background="#000080")
        top.configure(cursor="watch")
        top.configure(highlightcolor="black")

        self.image = tk.Canvas(top)
        self.image.place(relx=0.263, rely=0.017, relheight=0.967, relwidth=0.725)

        self.image.configure(background="#ffffff")
        self.image.configure(borderwidth="2")
        self.image.configure(highlightbackground="#d8d8d8")
        self.image.configure(relief="ridge")
        self.image.configure(selectbackground="#c4c4c4")

        self.dotslist = tk.Listbox(top)
        self.dotslist.place(relx=0.013, rely=0.088, relheight=0.53, relwidth=0.24)
        self.dotslist.configure(background="white")
        self.dotslist.configure(font="-family {Consolas} -size 12")
        self.dotslist.configure(selectbackground="#c4c4c4")

        self.oplabel = tk.Label(top)
        self.oplabel.place(relx=0.013, rely=0.033, height=19, width=192)
        self.oplabel.configure(activebackground="#f9f9f9")
        self.oplabel.configure(background="#000080")
        self.oplabel.configure(font="-family {Consolas} -size 14")
        self.oplabel.configure(foreground="#ffffff")
        self.oplabel.configure(text="Список точек")

        self.addbtn = tk.Button(top)
        self.addbtn.place(relx=0.013, rely=0.633, height=29, width=192)
        self.addbtn.configure(background="#d9d9d9")
        self.addbtn.configure(foreground="black")
        self.addbtn.configure(activebackground="#000080")
        self.addbtn.configure(font="-family {Consolas} -size 12")
        self.addbtn.configure(text="Добавить точку")

        self.delbtn = tk.Button(top)
        self.delbtn.place(relx=0.013, rely=0.7, height=29, width=192)
        self.delbtn.configure(background="#d9d9d9")
        self.delbtn.configure(foreground="black")
        self.delbtn.configure(activebackground="#000080")
        self.delbtn.configure(font="-family {Consolas} -size 12")
        self.delbtn.configure(text="Удалить точку")

        self.editbtn = tk.Button(top)
        self.editbtn.place(relx=0.013, rely=0.767, height=29, width=192)
        self.editbtn.configure(background="#d9d9d9")
        self.editbtn.configure(foreground="black")
        self.editbtn.configure(activebackground="#000080")
        self.editbtn.configure(font="-family {Consolas} -size 12")
        self.editbtn.configure(text="Изменить точку")

        self.clrbtn = tk.Button(top)
        self.clrbtn.place(relx=0.013, rely=0.833, height=29, width=192)
        self.clrbtn.configure(background="#d9d9d9")
        self.clrbtn.configure(foreground="black")
        self.clrbtn.configure(activebackground="#000080")
        self.clrbtn.configure(font="-family {Consolas} -size 12")
        self.clrbtn.configure(text="Очистить всё")

        self.solvebtn = tk.Button(top)
        self.solvebtn.place(relx=0.013, rely=0.9, height=29, width=192)
        self.solvebtn.configure(background="#d9d9d9")
        self.solvebtn.configure(foreground="black")
        self.solvebtn.configure(activebackground="#000080")
        self.solvebtn.configure(font="-family {Consolas} -size 12")
        self.solvebtn.configure(text="Решить задачу")


if __name__ == "__main__":
    ROOT = tk.Tk()
    TOPLEVEL = RootWindow(ROOT)
    ROOT.mainloop()
