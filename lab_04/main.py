import tkinter as tk
from view import view


class RootWindow(tk.Tk):
    """
        Representation of root program window.
    """

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        img = tk.PhotoImage(file="assets/img/icon.png")

        self.geometry("1920x1010+0+0")
        self.minsize(1, 1)
        self.maxsize(1920, 1010)
        self.resizable(0, 0)
        self.title("Circle drawing")
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

        # Shape selection section.
        self.shapelb = tk.Label(self)
        self.shapelb.place(relx=0.039, rely=0.028, height=60, width=477)
        self.shapelb.configure(
            activebackground="#000080",
            activeforeground="white",
            background="#000080",
            font="-family {Consolas} -size 18",
            foreground="#ffffff",
            text="ФИГУРА"
        )

        self.shapelst = tk.Listbox(self, exportselection=0)
        self.shapelst.place(relx=0.039, rely=0.083, relheight=0.04, relwidth=0.25)
        self.shapelst.configure(
            background="white",
            foreground="black",
            selectbackground="#000080",
            selectforeground="white",
            font="-family {Consolas} -size 14"
        )
        self.shapelst.insert(tk.END, "Окружность")
        self.shapelst.insert(tk.END, "Эллипс")
        self.shapelst.bind("<Button-1>", lambda event,
                           listbox=self.shapelst: view.check_lb(event, ROOT))

        # Drawing method section.
        self.methodlb = tk.Label(self)
        self.methodlb.place(relx=0.037, rely=0.133, height=60, width=477)
        self.methodlb.configure(
            activebackground="#000080",
            activeforeground="white",
            background="#000080",
            font="-family {Consolas} -size 18",
            foreground="#ffffff",
            text="МЕТОД ПОСТРОЕНИЯ"
        )

        self.methodlst = tk.Listbox(self, exportselection=0)
        self.methodlst.place(relx=0.037, rely=0.19, relheight=0.1, relwidth=0.25)
        self.methodlst.configure(
            background="white",
            foreground="black",
            selectbackground="#000080",
            selectforeground="white",
            font="-family {Consolas} -size 14"
        )
        self.methodlst.insert(tk.END, "Каноническое уравнение")
        self.methodlst.insert(tk.END, "Параметрическое уравнение")
        self.methodlst.insert(tk.END, "Алгоритм Брезенхема")
        self.methodlst.insert(tk.END, "Алгоритм средней точки")
        self.methodlst.insert(tk.END, "Библиотечная функция")
        self.methodlst.bind("<Button-1>", lambda event,
                            listbox=self.methodlst: view.check_lb(event, ROOT))

        # Drawing color section.
        self.colorlb = tk.Label(self)
        self.colorlb.place(relx=0.037, rely=0.305, height=59, width=477)
        self.colorlb.configure(
            activebackground="#000080",
            activeforeground="white",
            background="#000080",
            font="-family {Consolas} -size 18",
            foreground="#ffffff",
            text="ЦВЕТ ПОСТРОЕНИЯ"
        )

        self.colorlst = tk.Listbox(self, exportselection=0)
        self.colorlst.place(relx=0.037, rely=0.362, relheight=0.039, relwidth=0.25)
        self.colorlst.configure(
            background="white",
            foreground="black",
            selectbackground="#000080",
            selectforeground="white",
            font="-family {Consolas} -size 14"
        )
        self.colorlst.insert(tk.END, "Синий")
        self.colorlst.insert(tk.END, "Фоновый")
        self.colorlst.bind("<Button-1>", lambda event,
                           listbox=self.colorlst: view.check_lb(event, ROOT))

        # Shape parameters section.
        self.shapeparlb = tk.Label(self)
        self.shapeparlb.place(relx=0.037, rely=0.419, height=39, width=477)
        self.shapeparlb.configure(
            activebackground="#000080",
            activeforeground="white",
            background="#000080",
            font="-family {Consolas} -size 18",
            foreground="#ffffff",
            text="ПАРАМЕТРЫ ФИГУРЫ"
        )

        self.xcenterlb = tk.Label(self)
        self.xcenterlb.place(relx=0.037, rely=0.457, height=28, width=122)
        self.xcenterlb.configure(
            activebackground="#f9f9f9",
            background="#000080",
            font="-family {Consolas} -size 14",
            foreground="#ffffff",
            text="Xc"
        )

        self.ycenterlb = tk.Label(self)
        self.ycenterlb.place(relx=0.1, rely=0.457, height=28, width=120)
        self.ycenterlb.configure(
            activebackground="#f9f9f9",
            background="#000080",
            font="-family {Consolas} -size 14",
            foreground="#ffffff",
            text="Yc"
        )

        self.r1lb = tk.Label(self)
        self.r1lb.place(relx=0.163, rely=0.457, height=28, width=120)
        self.r1lb.configure(
            activebackground="#f9f9f9",
            background="#000080",
            font="-family {Consolas} -size 14",
            foreground="#ffffff",
            text="R1"
        )

        self.r2lb = tk.Label(self)
        self.r2lb.place(relx=0.226, rely=0.457, height=28, width=120)
        self.r2lb.configure(
            activebackground="#f9f9f9",
            background="#000080",
            font="-family {Consolas} -size 14",
            foreground="#ffffff",
            text="R2"
        )

        self.xcentersb = tk.Spinbox(self)
        self.xcentersb.place(relx=0.037, rely=0.486, relheight=0.03, relwidth=0.064)
        self.xcentersb.configure(
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

        self.ycentersb = tk.Spinbox(self)
        self.ycentersb.place(relx=0.1, rely=0.486, relheight=0.03, relwidth=0.063)
        self.ycentersb.configure(
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
            to=955.0,
            increment=1.0,
            textvariable=tk.IntVar()
        )

        self.r1sb = tk.Spinbox(self)
        self.r1sb.place(relx=0.162, rely=0.486, relheight=0.03, relwidth=0.063)
        self.r1sb.configure(
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
            to=487.0,
            increment=1.0,
            textvariable=tk.IntVar()
        )

        self.r2sb = tk.Spinbox(self)
        self.r2sb.place(relx=0.224, rely=0.486, relheight=0.03, relwidth=0.063)
        self.r2sb.configure(
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
            to=487.0,
            increment=1.0,
            textvariable=tk.IntVar()
        )

        self.drawbtn = tk.Button(self)
        self.drawbtn.place(relx=0.037, rely=0.524, height=40, width=477)
        self.drawbtn.configure(
            background="#d9d9d9",
            foreground="black",
            activebackground="#000080",
            font="-family {Consolas} -size 14",
            text="Построить фигуру",
            state="disabled",
            command=lambda: view.draw(ROOT)
        )

        # Spectre drawing section.
        self.spectrelb = tk.Label(self)
        self.spectrelb.place(relx=0.037, rely=0.58, height=57, width=477)
        self.spectrelb.configure(
            activebackground="#000080",
            activeforeground="white",
            background="#000080",
            font="-family {Consolas} -size 18",
            foreground="#ffffff",
            text="ПАРАМЕТРЫ СПЕКТРА"
        )

        self.xscenterlb = tk.Label(self)
        self.xscenterlb.place(relx=0.037, rely=0.622, height=33, width=233)
        self.xscenterlb.configure(
            activebackground="#000080",
            activeforeground="white",
            background="#000080",
            font="-family {Consolas} -size 14",
            foreground="#ffffff",
            text="Xc"
        )

        self.yscenterlb = tk.Label(self)
        self.yscenterlb.place(relx=0.163, rely=0.622, height=33, width=232)
        self.yscenterlb.configure(
            activebackground="#000080",
            activeforeground="white",
            background="#000080",
            font="-family {Consolas} -size 14",
            foreground="#ffffff",
            text="Yc"
        )

        self.xscentersb = tk.Spinbox(self)
        self.xscentersb.place(relx=0.037, rely=0.66, relheight=0.033, relwidth=0.127)
        self.xscentersb.configure(
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

        self.yscentersb = tk.Spinbox(self)
        self.yscentersb.place(relx=0.163, rely=0.66, relheight=0.033, relwidth=0.127)
        self.yscentersb.configure(
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
            to=955.0,
            increment=1.0,
            textvariable=tk.IntVar()
        )

        self.rs1lb = tk.Label(self)
        self.rs1lb.place(relx=0.037, rely=0.708, height=34, width=122)
        self.rs1lb.configure(
            activebackground="#f9f9f9",
            background="#000080",
            font="-family {Consolas} -size 14",
            foreground="#ffffff",
            text="R1"
        )

        self.rs2lb = tk.Label(self)
        self.rs2lb.place(relx=0.1, rely=0.708, height=34, width=121)
        self.rs2lb.configure(
            activebackground="#f9f9f9",
            background="#000080",
            font="-family {Consolas} -size 14",
            foreground="#ffffff",
            text="R2"
        )

        self.steplb = tk.Label(self)
        self.steplb.place(relx=0.163, rely=0.708, height=34, width=121)
        self.steplb.configure(
            activebackground="#f9f9f9",
            background="#000080",
            font="-family {Consolas} -size 14",
            foreground="#ffffff",
            text="Шаг"
        )

        self.nlb = tk.Label(self)
        self.nlb.place(relx=0.226, rely=0.708, height=34, width=121)
        self.nlb.configure(
            activebackground="#f9f9f9",
            background="#000080",
            font="-family {Consolas} -size 14",
            foreground="#ffffff",
            text="N"
        )

        self.rs1sb = tk.Spinbox(self)
        self.rs1sb.place(relx=0.037, rely=0.746, relheight=0.033, relwidth=0.064)
        self.rs1sb.configure(
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
            to=487.0,
            increment=1.0,
            textvariable=tk.IntVar()
        )

        self.rs2sb = tk.Spinbox(self)
        self.rs2sb.place(relx=0.1, rely=0.746, relheight=0.033, relwidth=0.064)
        self.rs2sb.configure(
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
            to=487.0,
            increment=1.0,
            textvariable=tk.IntVar()
        )

        self.stepsb = tk.Spinbox(self)
        self.stepsb.place(relx=0.163, rely=0.746, relheight=0.033, relwidth=0.064)
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
            textvariable=tk.IntVar()
        )

        self.nsb = tk.Spinbox(self)
        self.nsb.place(relx=0.226, rely=0.746, relheight=0.033, relwidth=0.063)
        self.nsb.configure(
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
            textvariable=tk.IntVar()
        )

        self.drawspectrebtn = tk.Button(self)
        self.drawspectrebtn.place(relx=0.037, rely=0.785, height=42, width=477)
        self.drawspectrebtn.configure(
            background="#d9d9d9",
            foreground="black",
            activebackground="#000080",
            font="-family {Consolas} -size 14",
            text="Построить спектр",
            state="disabled",
            command=lambda: view.draw_spectre(ROOT)
        )

        # Additional stuff section.
        self.cmpalgosbtn = tk.Button(self)
        self.cmpalgosbtn.place(relx=0.037, rely=0.861, height=40, width=477)
        self.cmpalgosbtn.configure(
            background="#d9d9d9",
            foreground="black",
            activebackground="#000080",
            font="-family {Consolas} -size 14",
            text="Сравнение алгоритмов",
            command=lambda: view.compare_algos(ROOT.image)
        )

        self.clrbtn = tk.Button(self)
        self.clrbtn.place(relx=0.037, rely=0.917, height=41, width=477)
        self.clrbtn.configure(
            background="#d9d9d9",
            foreground="black",
            activebackground="#000080",
            font="-family {Consolas} -size 14",
            text="Очистить экран",
            command=lambda: view.reset(ROOT)
        )


if __name__ == "__main__":
    ROOT = RootWindow()
    ROOT.mainloop()
