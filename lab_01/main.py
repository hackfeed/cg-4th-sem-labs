import tkinter as tk
from trview import view


class RootWindow(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        img = tk.PhotoImage(file="assets/img/icon.png")

        self.geometry("800x600+298+48")
        self.minsize(1, 1)
        self.maxsize(1351, 738)
        self.resizable(0, 0)
        self.title("Triangle Magic")
        self.iconphoto(True, img)
        self.configure(background="#000080")
        self.configure(cursor="watch")
        self.configure(highlightcolor="black")

        self.image = tk.Canvas(self)
        self.image.place(relx=0.263, rely=0.017, relheight=0.967, relwidth=0.725)

        self.image.configure(background="#ffffff")
        self.image.configure(borderwidth="2")
        self.image.configure(highlightbackground="#d8d8d8")
        self.image.configure(relief="ridge")
        self.image.configure(selectbackground="#c4c4c4")

        self.dotslist = tk.Listbox(self)
        self.dotslist.place(relx=0.013, rely=0.088, relheight=0.53, relwidth=0.24)
        self.dotslist.configure(background="white")
        self.dotslist.configure(foreground="black")
        self.dotslist.configure(font="-family {Consolas} -size 12")
        self.dotslist.configure(selectbackground="#000080")
        self.dotslist.configure(selectforeground="white")
        self.dotslist.bind("<Double-Button-1>", lambda event,
                           listbox=self.dotslist: view.check_lb(event, ROOT, listbox))

        self.oplabel = tk.Label(self)
        self.oplabel.place(relx=0.013, rely=0.033, height=19, width=192)
        self.oplabel.configure(activebackground="#f9f9f9")
        self.oplabel.configure(background="#000080")
        self.oplabel.configure(font="-family {Consolas} -size 14")
        self.oplabel.configure(foreground="#ffffff")
        self.oplabel.configure(text="Список точек")

        self.addbtn = tk.Button(self)
        self.addbtn.place(relx=0.013, rely=0.633, height=29, width=192)
        self.addbtn.configure(background="#d9d9d9")
        self.addbtn.configure(foreground="black")
        self.addbtn.configure(activebackground="#000080")
        self.addbtn.configure(font="-family {Consolas} -size 12")
        self.addbtn.configure(text="Добавить точку")
        self.addbtn.configure(command=lambda: add_action(ROOT))

        self.delbtn = tk.Button(self)
        self.delbtn.place(relx=0.013, rely=0.7, height=29, width=192)
        self.delbtn.configure(background="#d9d9d9")
        self.delbtn.configure(foreground="black")
        self.delbtn.configure(activebackground="#000080")
        self.delbtn.configure(font="-family {Consolas} -size 12")
        self.delbtn.configure(text="Удалить точку")
        self.delbtn.configure(command=lambda: view.del_dot(self))
        self.delbtn.configure(state="disabled")

        self.editbtn = tk.Button(self)
        self.editbtn.place(relx=0.013, rely=0.767, height=29, width=192)
        self.editbtn.configure(background="#d9d9d9")
        self.editbtn.configure(foreground="black")
        self.editbtn.configure(activebackground="#000080")
        self.editbtn.configure(font="-family {Consolas} -size 12")
        self.editbtn.configure(text="Изменить точку")
        self.editbtn.configure(state="disabled")
        self.editbtn.configure(command=lambda: edit_action(ROOT))

        self.clrbtn = tk.Button(self)
        self.clrbtn.place(relx=0.013, rely=0.833, height=29, width=192)
        self.clrbtn.configure(background="#d9d9d9")
        self.clrbtn.configure(foreground="black")
        self.clrbtn.configure(activebackground="#000080")
        self.clrbtn.configure(font="-family {Consolas} -size 12")
        self.clrbtn.configure(text="Очистить всё")
        self.clrbtn.configure(command=lambda: view.clean_scr(self))

        self.solvebtn = tk.Button(self)
        self.solvebtn.place(relx=0.013, rely=0.9, height=29, width=192)
        self.solvebtn.configure(background="#d9d9d9")
        self.solvebtn.configure(foreground="black")
        self.solvebtn.configure(activebackground="#000080")
        self.solvebtn.configure(font="-family {Consolas} -size 12")
        self.solvebtn.configure(text="Решить задачу")


class DotWindow(tk.Toplevel):
    def __init__(self, *args, **kwargs):
        tk.Toplevel.__init__(self, *args, **kwargs)

        img = tk.PhotoImage(file="assets/img/icon.png")

        self.geometry("240x130+2408+934")
        self.minsize(1, 1)
        self.maxsize(3271, 1439)
        self.resizable(0, 0)
        self.title("Dots Action")
        self.iconphoto(True, img)
        self.configure(background="#000080")
        self.configure(cursor="watch")
        self.grab_set()
        self.focus_set()

        self.xentry = tk.Entry(self)
        self.xentry.place(relx=0.042, rely=0.285, height=41, relwidth=0.417)
        self.xentry.configure(background="white")
        self.xentry.configure(foreground="black")
        self.xentry.configure(cursor="watch")
        self.xentry.configure(font="-family {Consolas} -size 12")
        self.xentry.configure(justify="center")
        self.xentry.insert(tk.END, "0")

        self.yentry = tk.Entry(self)
        self.yentry.place(relx=0.542, rely=0.285, height=41, relwidth=0.417)
        self.yentry.configure(background="white")
        self.yentry.configure(foreground="black")
        self.xentry.configure(relief="flat")
        self.yentry.configure(cursor="watch")
        self.yentry.configure(font="-family {Consolas} -size 12")
        self.yentry.configure(justify="center")
        self.yentry.insert(tk.END, "0")

        self.okbtn = tk.Button(self)
        self.okbtn.place(relx=0.104, rely=0.692, height=29, width=192)
        self.okbtn.configure(background="#d9d9d9")
        self.okbtn.configure(foreground="black")
        self.okbtn.configure(activebackground="#000080")
        self.okbtn.configure(font="-family {Consolas} -size 12")
        self.okbtn.configure(text="OK")
        self.okbtn.configure(command=lambda: view.dot(DOTACTION, ROOT, MODE))

        self.xlabel = tk.Label(self)
        self.xlabel.place(relx=0.042, rely=0.077, height=19, width=96)
        self.xlabel.configure(activebackground="#000080")
        self.xlabel.configure(activeforeground="white")
        self.xlabel.configure(background="#000080")
        self.xlabel.configure(font="-family {Consolas} -size 12")
        self.xlabel.configure(foreground="#ffffff")
        self.xlabel.configure(text="X coord")

        self.ylabel = tk.Label(self)
        self.ylabel.place(relx=0.542, rely=0.077, height=19, width=96)
        self.ylabel.configure(activebackground="#000080")
        self.ylabel.configure(activeforeground="white")
        self.ylabel.configure(background="#000080")
        self.ylabel.configure(font="-family {Consolas} -size 14")
        self.ylabel.configure(foreground="#ffffff")
        self.ylabel.configure(text="Y coord")


def add_action(root):
    global DOTACTION, MODE
    MODE = 0
    DOTACTION = DotWindow(root)


def edit_action(root):
    global DOTACTION, MODE
    MODE = 1
    DOTACTION = DotWindow(root)
    ind = root.dotslist.curselection()
    item = root.dotslist.get(ind[0]).split(";")
    DOTACTION.xentry.delete(0, tk.END)
    DOTACTION.xentry.insert(0, item[0])
    DOTACTION.yentry.delete(0, tk.END)
    DOTACTION.yentry.insert(0, item[1])


if __name__ == "__main__":
    DOTACTION = None
    MODE = 0
    ROOT = RootWindow()
    ROOT.mainloop()
