import tkinter as tk
from tkinter import colorchooser
from fhorizon import fhorizon


class RootWindow(tk.Tk):
    """
        Representation of root program window.
    """

    color = "#FF0000"

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        img = tk.PhotoImage(file="assets/img/icon.png")

        self.geometry("1910x1000+0+0")
        self.minsize(1, 1)
        self.maxsize(1920, 1010)
        self.resizable(0, 0)
        self.title("Floating Horizon")
        self.iconphoto(True, img)
        self.configure(
            background="#000080",
            highlightcolor="black"
        )

        self.canvas = tk.Canvas(self)
        self.canvas.place(relx=0.307, rely=0.028, relheight=0.945, relwidth=0.677)
        self.canvas.configure(
            background="#ffffff",
            borderwidth="2",
            relief="ridge",
            selectbackground="#c4c4c4"
        )

        # Color selection section.
        self.colorlb = tk.Label(self)
        self.colorlb.place(relx=0.031, rely=0.03, height=57, width=476)
        self.colorlb.configure(
            activebackground="#000080",
            activeforeground="white",
            background="#000080",
            font="-family {Consolas} -size 18",
            foreground="#ffffff",
            text="ЦВЕТ"
        )

        self.colorpicker = tk.Button(self)
        self.colorpicker.place(relx=0.031, rely=0.079, height=42, width=476)
        self.colorpicker.configure(
            background=self.color,
            activebackground=self.color,
            font="-family {Consolas} -size 14",
            command=lambda: self.get_color(self.colorpicker, self.color)
        )

        # Function section.
        self.funclb = tk.Label(self)
        self.funclb.place(relx=0.031, rely=0.129, height=57, width=476)
        self.funclb.configure(
            activebackground="#000080",
            activeforeground="white",
            background="#000080",
            font="-family {Consolas} -size 18",
            foreground="#ffffff",
            text="ФУНКЦИЯ"
        )

        self.funclst = tk.Listbox(self, exportselection=0)
        self.funclst.place(relx=0.031, rely=0.178, relheight=0.106, relwidth=0.249)
        self.funclst.configure(
            background="white",
            foreground="black",
            selectbackground="#000080",
            selectforeground="white",
            font="-family {Consolas} -size 14"
        )

        # Limits section.
        self.limitslb = tk.Label(self)
        self.limitslb.place(relx=0.031, rely=0.297, height=56, width=476)
        self.limitslb.configure(
            activebackground="#000080",
            activeforeground="white",
            background="#000080",
            font="-family {Consolas} -size 18",
            foreground="#ffffff",
            text="ПРЕДЕЛЫ"
        )

        self.xlimitslb = tk.Label(self)
        self.xlimitslb.place(relx=0.026, rely=0.387, height=32, width=120)
        self.xlimitslb.configure(
            activebackground="#000080",
            activeforeground="white",
            background="#000080",
            font="-family {Consolas} -size 14",
            foreground="#ffffff",
            text="X"
        )

        self.zlimitslb = tk.Label(self)
        self.zlimitslb.place(relx=0.026, rely=0.426, height=31, width=120)
        self.zlimitslb.configure(
            activebackground="#000080",
            activeforeground="white",
            background="#000080",
            font="-family {Consolas} -size 14",
            foreground="#ffffff",
            text="Z"
        )

        self.fromlb = tk.Label(self)
        self.fromlb.place(relx=0.089, rely=0.357, height=31, width=120)
        self.fromlb.configure(
            activebackground="#000080",
            activeforeground="white",
            background="#000080",
            font="-family {Consolas} -size 14",
            foreground="#ffffff",
            text="От"
        )

        self.tolb = tk.Label(self)
        self.tolb.place(relx=0.152, rely=0.357, height=31, width=120)
        self.tolb.configure(
            activebackground="#000080",
            activeforeground="white",
            background="#000080",
            font="-family {Consolas} -size 14",
            foreground="#ffffff",
            text="До"
        )

        self.steplb = tk.Label(self)
        self.steplb.place(relx=0.215, rely=0.357, height=31, width=120)
        self.steplb.configure(
            activebackground="#000080",
            activeforeground="white",
            background="#000080",
            font="-family {Consolas} -size 14",
            foreground="#ffffff",
            text="Шаг"
        )

        self.xfromsb = tk.Spinbox(self)
        self.xfromsb.place(relx=0.089, rely=0.387, relheight=0.033, relwidth=0.063)
        self.xfromsb.configure(
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

        self.xtosb = tk.Spinbox(self)
        self.xtosb.place(relx=0.152, rely=0.387, relheight=0.033, relwidth=0.064)
        self.xtosb.configure(
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

        self.xstepsb = tk.Spinbox(self)
        self.xstepsb.place(relx=0.215, rely=0.387, relheight=0.033, relwidth=0.064)
        self.xstepsb.configure(
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

        self.zfromsb = tk.Spinbox(self)
        self.zfromsb.place(relx=0.089, rely=0.426, relheight=0.033, relwidth=0.063)
        self.zfromsb.configure(
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

        self.ztosb = tk.Spinbox(self)
        self.ztosb.place(relx=0.152, rely=0.426, relheight=0.033, relwidth=0.063)
        self.ztosb.configure(
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

        self.zstepsb = tk.Spinbox(self)
        self.zstepsb.place(relx=0.215, rely=0.426, relheight=0.033, relwidth=0.063)
        self.zstepsb.configure(
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

        self.lapplybtn = tk.Button(self)
        self.lapplybtn.place(relx=0.031, rely=0.469, height=43, width=476)
        self.lapplybtn.configure(
            background="#d9d9d9",
            foreground="black",
            activebackground="#000080",
            font="-family {Consolas} -size 14",
            text="Применить"
            # command=self.add_cut
        )

        # Rotate section.
        self.rotatelb = tk.Label(self)
        self.rotatelb.place(relx=0.031, rely=0.535, height=56, width=476)
        self.rotatelb.configure(
            activebackground="#000080",
            activeforeground="white",
            background="#000080",
            font="-family {Consolas} -size 18",
            foreground="#ffffff",
            text="ВРАЩЕНИЕ"
        )

        self.xrotatelb = tk.Label(self)
        self.xrotatelb.place(relx=0.031, rely=0.595, height=33, width=122)
        self.xrotatelb.configure(
            activebackground="#000080",
            activeforeground="white",
            background="#000080",
            font="-family {Consolas} -size 14",
            foreground="#ffffff",
            text="X"
        )

        self.yrotatelb = tk.Label(self)
        self.yrotatelb.place(relx=0.031, rely=0.634, height=32, width=120)
        self.yrotatelb.configure(
            activebackground="#000080",
            activeforeground="white",
            background="#000080",
            font="-family {Consolas} -size 14",
            foreground="#ffffff",
            text="Y"
        )

        self.zrotatelb = tk.Label(self)
        self.zrotatelb.place(relx=0.031, rely=0.674, height=32, width=120)
        self.zrotatelb.configure(
            activebackground="#000080",
            activeforeground="white",
            background="#000080",
            font="-family {Consolas} -size 14",
            foreground="#ffffff",
            text="Z"
        )

        self.xrotatesb = tk.Spinbox(self)
        self.xrotatesb.place(relx=0.089, rely=0.595, relheight=0.033, relwidth=0.063)
        self.xrotatesb.configure(
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

        self.yrotatesb = tk.Spinbox(self)
        self.yrotatesb.place(relx=0.089, rely=0.634, relheight=0.033, relwidth=0.063)
        self.yrotatesb.configure(
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

        self.zrotatesb = tk.Spinbox(self)
        self.zrotatesb.place(relx=0.089, rely=0.674, relheight=0.033, relwidth=0.063)
        self.zrotatesb.configure(
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

        self.xrotatebtn = tk.Button(self)
        self.xrotatebtn.place(relx=0.157, rely=0.595, height=33, width=236)
        self.xrotatebtn.configure(
            background="#d9d9d9",
            foreground="black",
            activebackground="#000080",
            font="-family {Consolas} -size 14",
            text="Вращать"
            # command=self.add_dot
        )

        self.yrotatebtn = tk.Button(self)
        self.yrotatebtn.place(relx=0.157, rely=0.634, height=33, width=236)
        self.yrotatebtn.configure(
            background="#d9d9d9",
            foreground="black",
            activebackground="#000080",
            font="-family {Consolas} -size 14",
            text="Вращать"
            # command=self.add_dot
        )

        self.zrotatebtn = tk.Button(self)
        self.zrotatebtn.place(relx=0.157, rely=0.674, height=33, width=236)
        self.zrotatebtn.configure(
            background="#d9d9d9",
            foreground="black",
            activebackground="#000080",
            font="-family {Consolas} -size 14",
            text="Вращать"
            # command=self.add_dot
        )

        # Scale section.
        self.scalelb = tk.Label(self)
        self.scalelb.place(relx=0.031, rely=0.723, height=56, width=476)
        self.scalelb.configure(
            activebackground="#000080",
            activeforeground="white",
            background="#000080",
            font="-family {Consolas} -size 18",
            foreground="#ffffff",
            text="МАСШТАБИРОВАНИЕ"
        )

        self.kscalelb = tk.Label(self)
        self.kscalelb.place(relx=0.031, rely=0.773, height=33, width=122)
        self.kscalelb.configure(
            activebackground="#000080",
            activeforeground="white",
            background="#000080",
            font="-family {Consolas} -size 14",
            foreground="#ffffff",
            text="K"
        )

        self.kscalesb = tk.Spinbox(self)
        self.kscalesb.place(relx=0.089, rely=0.773, relheight=0.033, relwidth=0.063)
        self.kscalesb.configure(
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

        self.kscalebtn = tk.Button(self)
        self.kscalebtn.place(relx=0.157, rely=0.773, height=33, width=236)
        self.kscalebtn.configure(
            background="#d9d9d9",
            foreground="black",
            activebackground="#000080",
            font="-family {Consolas} -size 14",
            text="Применить"
            # command=lambda: cut.cut(ROOT)
        )

        # General section.
        self.drawbtn = tk.Button(self)
        self.drawbtn.place(relx=0.031, rely=0.862, height=40, width=476)
        self.drawbtn.configure(
            background="#d9d9d9",
            foreground="black",
            activebackground="#000080",
            font="-family {Consolas} -size 14",
            text="Нарисовать"
            # command=lambda: cut.cut(ROOT)
        )

        self.clrbtn = tk.Button(self)
        self.clrbtn.place(relx=0.031, rely=0.917, height=41, width=476)
        self.clrbtn.configure(
            background="#d9d9d9",
            foreground="black",
            activebackground="#000080",
            font="-family {Consolas} -size 14",
            text="Очистить экран",
            command=self.reset
        )

    def reset(self):
        self.canvas.delete("all")

    def get_color(self, cp, color):
        _, hex_code = colorchooser.askcolor(
            parent=self,
            title="Выберите цвет для закрашивания",
            initialcolor=color
        )
        cp.configure(
            background=hex_code,
            activebackground=hex_code
        )
        color = hex_code

    def draw_line(self, dot_start, dot_end, color):
        self.canvas.create_line(round(dot_start[0]), round(
            dot_start[1]), round(dot_end[0]), round(dot_end[1]), fill=color)


if __name__ == "__main__":
    ROOT = RootWindow()
    ROOT.mainloop()
