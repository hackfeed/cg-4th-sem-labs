import tkinter as tk
from view import view


class RootWindow(tk.Tk):
    """
        Representation of root program window.
    """

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        img = tk.PhotoImage(file="assets/img/icon.png")

        self.geometry("1910x1000+0+0")
        self.minsize(1, 1)
        self.maxsize(1920, 1010)
        self.resizable(0, 0)
        self.title("Filling with sorted edges")
        self.iconphoto(True, img)
        self.configure(
            background="#000080",
            highlightcolor="black"
        )

        self.image = tk.Canvas(self)
        self.image.place(relx=0.307, rely=0.028, relheight=0.945, relwidth=0.677)
        self.image.configure(
            background="#ffffff",
            borderwidth="2",
            relief="ridge",
            selectbackground="#c4c4c4"
        )

        # Mode selection section.
        self.modelb = tk.Label(self)
        self.modelb.place(relx=0.031, rely=0.028, height=58, width=476)
        self.modelb.configure(
            activebackground="#000080",
            activeforeground="white",
            background="#000080",
            font="-family {Consolas} -size 18",
            foreground="#ffffff",
            text="РЕЖИМ"
        )

        self.modelst = tk.Listbox(self, exportselection=0)
        self.modelst.place(relx=0.031, rely=0.083, relheight=0.065, relwidth=0.25)
        self.modelst.configure(
            background="white",
            foreground="black",
            selectbackground="#000080",
            selectforeground="white",
            font="-family {Consolas} -size 14"
        )
        self.modelst.insert(tk.END, "Без задержки")
        self.modelst.insert(tk.END, "С задержкой")
        # self.modelst.bind("<Button-1>", lambda event,
        #                    listbox=self.shapelst: view.check_lb(event, ROOT))

        # Color selection section.
        self.colorlb = tk.Label(self)
        self.colorlb.place(relx=0.031, rely=0.168, height=56, width=476)
        self.colorlb.configure(
            activebackground="#000080",
            activeforeground="white",
            background="#000080",
            font="-family {Consolas} -size 18",
            foreground="#ffffff",
            text="ЦВЕТ"
        )

        self.colorpicker = tk.Button(self)
        self.colorpicker.place(relx=0.031, rely=0.218, height=42, width=476)
        self.colorpicker.configure(
            background="black",
            activebackground="black",
            font="-family {Consolas} -size 14",
            command=lambda: view.get_color(ROOT)
        )

        # New dot section.
        self.dotlb = tk.Label(self)
        self.dotlb.place(relx=0.031, rely=0.278, height=56, width=476)
        self.dotlb.configure(
            activebackground="#000080",
            activeforeground="white",
            background="#000080",
            font="-family {Consolas} -size 18",
            foreground="#ffffff",
            text="КООРДИНАТЫ ТОЧКИ"
        )

        self.xlb = tk.Label(self)
        self.xlb.place(relx=0.031, rely=0.327, height=33, width=232)
        self.xlb.configure(
            activebackground="#000080",
            activeforeground="white",
            background="#000080",
            font="-family {Consolas} -size 14",
            foreground="#ffffff",
            text="X"
        )

        self.ylb = tk.Label(self)
        self.ylb.place(relx=0.157, rely=0.327, height=33, width=232)
        self.ylb.configure(
            activebackground="#000080",
            activeforeground="white",
            background="#000080",
            font="-family {Consolas} -size 14",
            foreground="#ffffff",
            text="X"
        )

        self.xsb = tk.Spinbox(self)
        self.xsb.place(relx=0.031, rely=0.357, relheight=0.039, relwidth=0.125)
        self.xsb.configure(
            activebackground="#f9f9f9",
            background="white",
            foreground="black",
            buttonbackground="#d9d9d9",
            justify="center",
            font="-family {Consolas} -size 14",
            highlightbackground="black",
            relief="flat",
            selectbackground="#c4c4c4",
            from_=0.0,
            to=1300.0,
            increment=1.0,
            textvariable=tk.IntVar()
        )

        self.ysb = tk.Spinbox(self)
        self.ysb.place(relx=0.1553, rely=0.357, relheight=0.039, relwidth=0.125)
        self.ysb.configure(
            activebackground="#f9f9f9",
            background="white",
            foreground="black",
            buttonbackground="#d9d9d9",
            justify="center",
            font="-family {Consolas} -size 14",
            highlightbackground="black",
            relief="flat",
            selectbackground="#c4c4c4",
            from_=0.0,
            to=1300.0,
            increment=1.0,
            textvariable=tk.IntVar()
        )

        self.addbtn = tk.Button(self)
        self.addbtn.place(relx=0.031, rely=0.396, height=42, width=477)
        self.addbtn.configure(
            background="#d9d9d9",
            foreground="black",
            activebackground="#000080",
            font="-family {Consolas} -size 14",
            text="Добавить точку"
        )

        self.fillbtn = tk.Button(self)
        self.fillbtn.place(relx=0.031, rely=0.803, height=41, width=476)
        self.fillbtn.configure(
            background="#d9d9d9",
            foreground="black",
            activebackground="#000080",
            font="-family {Consolas} -size 14",
            text="Выполнить закраску"
            # command=lambda: view.reset(ROOT)
        )

        self.timebtn = tk.Button(self)
        self.timebtn.place(relx=0.031, rely=0.861, height=40, width=476)
        self.timebtn.configure(
            background="#d9d9d9",
            foreground="black",
            activebackground="#000080",
            font="-family {Consolas} -size 14",
            text="Замерить время"
            # command=lambda: view.reset(ROOT)
        )

        self.clrbtn = tk.Button(self)
        self.clrbtn.place(relx=0.031, rely=0.917, height=41, width=476)
        self.clrbtn.configure(
            background="#d9d9d9",
            foreground="black",
            activebackground="#000080",
            font="-family {Consolas} -size 14",
            text="Очистить экран"
            # command=lambda: view.reset(ROOT)
        )


if __name__ == "__main__":
    ROOT = RootWindow()
    ROOT.mainloop()
