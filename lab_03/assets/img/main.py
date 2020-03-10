import tkinter as tk


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

        self.xstartlb = tk.Label(self)
        self.xstartlb.place(relx=0.039, rely=0.493, height=18, width=81)
        self.xstartlb.configure(activebackground="#f9f9f9")
        self.xstartlb.configure(background="#000080")
        self.xstartlb.configure(font="-family {Consolas} -size 14")
        self.xstartlb.configure(foreground="#ffffff")
        self.xstartlb.configure(text="""Xн""")

        self.cmpalgosbtn = tk.Button(self)
        self.cmpalgosbtn.place(relx=0.039, rely=0.861, height=29, width=320)
        self.cmpalgosbtn.configure(activebackground="#f9f9f9")
        self.cmpalgosbtn.configure(font="-family {Consolas} -size 14")
        self.cmpalgosbtn.configure(text="""Сравнение алгоритмов""")

        self.clrbtn = tk.Button(self)
        self.clrbtn.place(relx=0.039, rely=0.917, height=29, width=320)
        self.clrbtn.configure(activebackground="#f9f9f9")
        self.clrbtn.configure(font="-family {Consolas} -size 14")
        self.clrbtn.configure(text="""Очистить экран""")

        self.methodlst = tk.Listbox(self)
        self.methodlst.place(relx=0.039, rely=0.097, relheight=0.125, relwidth=0.25)
        self.methodlst.configure(background="white")
        self.methodlst.configure(font="-family {Consolas} -size 14")
        self.methodlst.configure(selectbackground="#c4c4c4")

        self.colorlb = tk.Label(self)
        self.colorlb.place(relx=0.039, rely=0.235, height=41, width=320)
        self.colorlb.configure(activebackground="#000080")
        self.colorlb.configure(activeforeground="white")
        self.colorlb.configure(background="#000080")
        self.colorlb.configure(font="-family {Consolas} -size 18")
        self.colorlb.configure(foreground="#ffffff")
        self.colorlb.configure(text="""ЦВЕТ ПОСТРОЕНИЯ""")

        self.colorlst = tk.Listbox(self)
        self.colorlst.place(relx=0.039, rely=0.292, relheight=0.125, relwidth=0.25)
        self.colorlst.configure(background="white")
        self.colorlst.configure(font="-family {Consolas} -size 14")
        self.colorlst.configure(selectbackground="#c4c4c4")

        self.linelb = tk.Label(self)
        self.linelb.place(relx=0.039, rely=0.432, height=41, width=320)
        self.linelb.configure(activebackground="#000080")
        self.linelb.configure(activeforeground="white")
        self.linelb.configure(background="#000080")
        self.linelb.configure(font="-family {Consolas} -size 18")
        self.linelb.configure(foreground="#ffffff")
        self.linelb.configure(text="""КООРДИНАТЫ ЛИНИИ""")

        self.ystartlb = tk.Label(self)
        self.ystartlb.place(relx=0.102, rely=0.493, height=18, width=80)
        self.ystartlb.configure(activebackground="#f9f9f9")
        self.ystartlb.configure(background="#000080")
        self.ystartlb.configure(font="-family {Consolas} -size 14")
        self.ystartlb.configure(foreground="#ffffff")
        self.ystartlb.configure(text="""Yн""")

        self.xendlb = tk.Label(self)
        self.xendlb.place(relx=0.164, rely=0.493, height=18, width=81)
        self.xendlb.configure(activebackground="#f9f9f9")
        self.xendlb.configure(background="#000080")
        self.xendlb.configure(font="-family {Consolas} -size 14")
        self.xendlb.configure(foreground="#ffffff")
        self.xendlb.configure(text="""Xк""")

        self.yendlb = tk.Label(self)
        self.yendlb.place(relx=0.227, rely=0.493, height=18, width=80)
        self.yendlb.configure(activebackground="#f9f9f9")
        self.yendlb.configure(background="#000080")
        self.yendlb.configure(font="-family {Consolas} -size 14")
        self.yendlb.configure(foreground="#ffffff")
        self.yendlb.configure(text="""Yк""")

        self.xstartsb = tk.Spinbox(self, from_=1.0, to=100.0)
        self.xstartsb.place(relx=0.039, rely=0.521, relheight=0.042, relwidth=0.063)
        self.xstartsb.configure(activebackground="#f9f9f9")
        self.xstartsb.configure(background="white")
        self.xstartsb.configure(font="-family {Consolas} -size 14")
        self.xstartsb.configure(highlightbackground="black")
        self.xstartsb.configure(relief="flat")
        self.xstartsb.configure(selectbackground="#c4c4c4")
        self.xstartsb.configure(textvariable=tk.StringVar())

        self.ystartsb = tk.Spinbox(self, from_=1.0, to=100.0)
        self.ystartsb.place(relx=0.102, rely=0.521, relheight=0.043, relwidth=0.063)
        self.ystartsb.configure(activebackground="#f9f9f9")
        self.ystartsb.configure(background="white")
        self.ystartsb.configure(font="-family {Consolas} -size 14")
        self.ystartsb.configure(highlightbackground="black")
        self.ystartsb.configure(relief="flat")
        self.ystartsb.configure(selectbackground="#c4c4c4")
        self.ystartsb.configure(textvariable=tk.StringVar())

        self.xendsb = tk.Spinbox(self, from_=1.0, to=100.0)
        self.xendsb.place(relx=0.165, rely=0.521, relheight=0.043, relwidth=0.063)
        self.xendsb.configure(activebackground="#f9f9f9")
        self.xendsb.configure(background="white")
        self.xendsb.configure(font="-family {Consolas} -size 14")
        self.xendsb.configure(highlightbackground="black")
        self.xendsb.configure(relief="flat")
        self.xendsb.configure(selectbackground="#c4c4c4")
        self.xendsb.configure(textvariable=tk.StringVar())

        self.yendsb = tk.Spinbox(self, from_=1.0, to=100.0)
        self.yendsb.place(relx=0.227, rely=0.521, relheight=0.043, relwidth=0.063)
        self.yendsb.configure(activebackground="#f9f9f9")
        self.yendsb.configure(background="white")
        self.yendsb.configure(font="-family {Consolas} -size 14")
        self.yendsb.configure(highlightbackground="black")
        self.yendsb.configure(relief="flat")
        self.yendsb.configure(selectbackground="#c4c4c4")
        self.yendsb.configure(textvariable=tk.StringVar())

        self.Button1_12 = tk.Button(self)
        self.Button1_12.place(relx=0.039, rely=0.574, height=28, width=320)
        self.Button1_12.configure(activebackground="#f9f9f9")
        self.Button1_12.configure(font="-family {Consolas} -size 14")
        self.Button1_12.configure(text="""Нарисовать линию""")

        self.Label1_6 = tk.Label(self)
        self.Label1_6.place(relx=0.039, rely=0.625, height=41, width=320)
        self.Label1_6.configure(activebackground="#000080")
        self.Label1_6.configure(activeforeground="white")
        self.Label1_6.configure(background="#000080")
        self.Label1_6.configure(font="-family {Consolas} -size 18")
        self.Label1_6.configure(foreground="#ffffff")
        self.Label1_6.configure(text="""ПАРАМЕТРЫ ПУЧКА""")

        self.Label3_1 = tk.Label(self)
        self.Label3_1.place(relx=0.039, rely=0.681, height=18, width=162)
        self.Label3_1.configure(activebackground="#f9f9f9")
        self.Label3_1.configure(background="#000080")
        self.Label3_1.configure(font="-family {Consolas} -size 14")
        self.Label3_1.configure(foreground="#ffffff")
        self.Label3_1.configure(text="""Радиус""")

        self.Label3_2 = tk.Label(self)
        self.Label3_2.place(relx=0.162, rely=0.681, height=18, width=163)
        self.Label3_2.configure(activebackground="#f9f9f9")
        self.Label3_2.configure(background="#000080")
        self.Label3_2.configure(font="-family {Consolas} -size 14")
        self.Label3_2.configure(foreground="#ffffff")
        self.Label3_2.configure(text="""Шаги""")

        self.Spinbox1_3 = tk.Spinbox(self, from_=1.0, to=100.0)
        self.Spinbox1_3.place(relx=0.039, rely=0.711, relheight=0.042, relwidth=0.125)
        self.Spinbox1_3.configure(activebackground="#f9f9f9")
        self.Spinbox1_3.configure(background="white")
        self.Spinbox1_3.configure(font="-family {Consolas} -size 14")
        self.Spinbox1_3.configure(highlightbackground="black")
        self.Spinbox1_3.configure(relief="flat")
        self.Spinbox1_3.configure(selectbackground="#c4c4c4")
        self.Spinbox1_3.configure(textvariable=tk.StringVar())

        self.Spinbox1_4 = tk.Spinbox(self, from_=1.0, to=100.0)
        self.Spinbox1_4.place(relx=0.165, rely=0.711, relheight=0.042, relwidth=0.125)
        self.Spinbox1_4.configure(activebackground="#f9f9f9")
        self.Spinbox1_4.configure(background="white")
        self.Spinbox1_4.configure(font="-family {Consolas} -size 14")
        self.Spinbox1_4.configure(highlightbackground="black")
        self.Spinbox1_4.configure(relief="flat")
        self.Spinbox1_4.configure(selectbackground="#c4c4c4")
        self.Spinbox1_4.configure(textvariable=tk.StringVar())

        self.Button1_11 = tk.Button(self)
        self.Button1_11.place(relx=0.039, rely=0.764, height=29, width=320)
        self.Button1_11.configure(activebackground="#f9f9f9")
        self.Button1_11.configure(font="-family {Consolas} -size 14")
        self.Button1_11.configure(text="""Построить пучок""")


if __name__ == "__main__":
    vp_start_gui()
