import tkinter as tk
from linedraw import dda, util


class RootWindow(tk.Tk):
    """
        Representation of root program window.
    """

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        img = tk.PhotoImage(file="assets/img/icon.png")

        self.geometry("1280x720+298+185")
        self.minsize(1, 1)
        self.maxsize(1905, 1050)
        self.resizable(1, 1)
        self.title("Line segments drawing")
        self.iconphoto(True, img)
        self.configure(
            background="#000080",
            highlightcolor="black"
        )

        self.image = tk.Canvas(self)
        self.image.place(relx=0.328, rely=0.028, relheight=0.944, relwidth=0.656)
        self.image.configure(
            background="#ffffff",
            borderwidth="2",
            relief="ridge",
            selectbackground="#c4c4c4"
        )

        # Drawing method section.
        self.methodlb = tk.Label(self)
        self.methodlb.place(relx=0.038, rely=0.042, height=41, width=320)
        self.methodlb.configure(
            activebackground="#000080",
            activeforeground="white",
            background="#000080",
            font="-family {Consolas} -size 18",
            foreground="#ffffff",
            text="""МЕТОД ПОСТРОЕНИЯ"""
        )

        self.methodlst = tk.Listbox(self, exportselection=0)
        self.methodlst.place(relx=0.039, rely=0.097, relheight=0.181, relwidth=0.25)
        self.methodlst.configure(
            background="white",
            foreground="black",
            selectbackground="#000080",
            selectforeground="white",
            font="-family {Consolas} -size 14"
        )
        self.methodlst.insert(tk.END, "ЦДА")
        self.methodlst.insert(tk.END, "Брезенхем (int)")
        self.methodlst.insert(tk.END, "Брезенхем (float)")
        self.methodlst.insert(tk.END, "Брезенхем (сглаживание)")
        self.methodlst.insert(tk.END, "Ву")
        self.methodlst.insert(tk.END, "Библиотечная функция")

        # Drawing color section.
        self.colorlb = tk.Label(self)
        self.colorlb.place(relx=0.039, rely=0.289, height=41, width=320)
        self.colorlb.configure(
            activebackground="#000080",
            activeforeground="white",
            background="#000080",
            font="-family {Consolas} -size 18",
            foreground="#ffffff",
            text="""ЦВЕТ ПОСТРОЕНИЯ"""
        )

        self.colorlst = tk.Listbox(self, exportselection=0)
        self.colorlst.place(relx=0.039, rely=0.347, relheight=0.069, relwidth=0.25)
        self.colorlst.configure(
            background="white",
            foreground="black",
            selectbackground="#000080",
            selectforeground="white",
            font="-family {Consolas} -size 14"
        )
        self.colorlst.insert(tk.END, "Синий")
        self.colorlst.insert(tk.END, "Фоновый")

        # Line coordinates section.
        self.linelb = tk.Label(self)
        self.linelb.place(relx=0.039, rely=0.432, height=41, width=320)
        self.linelb.configure(
            activebackground="#000080",
            activeforeground="white",
            background="#000080",
            font="-family {Consolas} -size 18",
            foreground="#ffffff",
            text="""КООРДИНАТЫ ЛИНИИ"""
        )

        self.xstartlb = tk.Label(self)
        self.xstartlb.place(relx=0.039, rely=0.493, height=18, width=81)
        self.xstartlb.configure(
            activebackground="#f9f9f9",
            background="#000080",
            font="-family {Consolas} -size 14",
            foreground="#ffffff",
            text="""Xн"""
        )

        self.ystartlb = tk.Label(self)
        self.ystartlb.place(relx=0.102, rely=0.493, height=18, width=80)
        self.ystartlb.configure(
            activebackground="#f9f9f9",
            background="#000080",
            font="-family {Consolas} -size 14",
            foreground="#ffffff",
            text="""Yн"""
        )

        self.xendlb = tk.Label(self)
        self.xendlb.place(relx=0.164, rely=0.493, height=18, width=81)
        self.xendlb.configure(
            activebackground="#f9f9f9",
            background="#000080",
            font="-family {Consolas} -size 14",
            foreground="#ffffff",
            text="""Xк"""
        )

        self.yendlb = tk.Label(self)
        self.yendlb.place(relx=0.227, rely=0.493, height=18, width=80)
        self.yendlb.configure(
            activebackground="#f9f9f9",
            background="#000080",
            font="-family {Consolas} -size 14",
            foreground="#ffffff",
            text="""Yк"""
        )

        self.xstartsb = tk.Spinbox(self)
        self.xstartsb.place(relx=0.039, rely=0.521, relheight=0.042, relwidth=0.063)
        self.xstartsb.configure(
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
            to=840.0,
            increment=1.0,
            textvariable=tk.DoubleVar()
        )

        self.ystartsb = tk.Spinbox(self)
        self.ystartsb.place(relx=0.102, rely=0.521, relheight=0.043, relwidth=0.063)
        self.ystartsb.configure(
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
            to=680.0,
            increment=1.0,
            textvariable=tk.DoubleVar()
        )

        self.xendsb = tk.Spinbox(self)
        self.xendsb.place(relx=0.165, rely=0.521, relheight=0.043, relwidth=0.063)
        self.xendsb.configure(
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
            to=840.0,
            increment=1.0,
            textvariable=tk.DoubleVar()
        )

        self.yendsb = tk.Spinbox(self)
        self.yendsb.place(relx=0.227, rely=0.521, relheight=0.043, relwidth=0.063)
        self.yendsb.configure(
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
            to=680.0,
            increment=1.0,
            textvariable=tk.DoubleVar()
        )

        self.drawbtn = tk.Button(self)
        self.drawbtn.place(relx=0.039, rely=0.574, height=28, width=320)
        self.drawbtn.configure(
            background="#d9d9d9",
            foreground="black",
            activebackground="#000080",
            font="-family {Consolas} -size 14",
            text="""Нарисовать линию"""
        )

        # Bunch drawing section.
        self.bunchlb = tk.Label(self)
        self.bunchlb.place(relx=0.039, rely=0.625, height=41, width=320)
        self.bunchlb.configure(
            activebackground="#000080",
            activeforeground="white",
            background="#000080",
            font="-family {Consolas} -size 18",
            foreground="#ffffff",
            text="""ПАРАМЕТРЫ ПУЧКА"""
        )

        self.radlb = tk.Label(self)
        self.radlb.place(relx=0.039, rely=0.681, height=18, width=162)
        self.radlb.configure(
            activebackground="#f9f9f9",
            background="#000080",
            font="-family {Consolas} -size 14",
            foreground="#ffffff",
            text="""Радиус"""
        )

        self.steplb = tk.Label(self)
        self.steplb.place(relx=0.162, rely=0.681, height=18, width=163)
        self.steplb.configure(
            activebackground="#f9f9f9",
            background="#000080",
            font="-family {Consolas} -size 14",
            foreground="#ffffff",
            text="""Шаги"""
        )

        self.radbsb = tk.Spinbox(self)
        self.radbsb.place(relx=0.039, rely=0.711, relheight=0.042, relwidth=0.125)
        self.radbsb.configure(
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
            to=340.0,
            increment=1.0,
            textvariable=tk.DoubleVar()
        )

        self.stepsb = tk.Spinbox(self)
        self.stepsb.place(relx=0.165, rely=0.711, relheight=0.042, relwidth=0.125)
        self.stepsb.configure(
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
            to=100.0,
            increment=1.0,
            textvariable=tk.DoubleVar()
        )

        self.drawbunchbtn = tk.Button(self)
        self.drawbunchbtn.place(relx=0.039, rely=0.764, height=29, width=320)
        self.drawbunchbtn.configure(
            background="#d9d9d9",
            foreground="black",
            activebackground="#000080",
            font="-family {Consolas} -size 14",
            text="""Построить пучок"""
        )

        # Additional stuff section.
        self.cmpalgosbtn = tk.Button(self)
        self.cmpalgosbtn.place(relx=0.039, rely=0.861, height=29, width=320)
        self.cmpalgosbtn.configure(
            background="#d9d9d9",
            foreground="black",
            activebackground="#000080",
            font="-family {Consolas} -size 14",
            text="""Сравнение алгоритмов"""
        )

        self.clrbtn = tk.Button(self)
        self.clrbtn.place(relx=0.039, rely=0.917, height=29, width=320)
        self.clrbtn.configure(
            background="#d9d9d9",
            foreground="black",
            activebackground="#000080",
            font="-family {Consolas} -size 14",
            text="""Очистить экран"""
        )


if __name__ == "__main__":
    ROOT = RootWindow()
    dots = dda.dda(10, 10, 840, 60)
    util.draw_line(ROOT.image, dots)
    ROOT.mainloop()
