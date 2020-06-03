import tkinter as tk
from tkinter import colorchooser
from cut import cut


class RootWindow(tk.Tk):
    """
        Representation of root program window.
    """

    cut_color = "#FF0000"
    figure_color = "#00FF00"
    res_color = "#0000FF"
    cut = []
    figure = []

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        img = tk.PhotoImage(file="assets/img/icon.png")

        self.geometry("1910x1000+0+0")
        self.minsize(1, 1)
        self.maxsize(1920, 1010)
        self.resizable(0, 0)
        self.title("Sutherland-Hodgman cut")
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
        self.canvas.bind("<Button-1>", lambda event: self.pixclick(event))
        self.canvas.bind("<Button-3>", lambda event: self.pixclose())
        self.canvas.bind("<Button-4>", lambda event: self.cutclick(event))
        self.canvas.bind("<Button-5>", lambda event: self.cutclose())

        # Color selection section.
        self.cutcolorlb = tk.Label(self)
        self.cutcolorlb.place(relx=0.031, rely=0.03, height=57, width=476)
        self.cutcolorlb.configure(
            activebackground="#000080",
            activeforeground="white",
            background="#000080",
            font="-family {Consolas} -size 18",
            foreground="#ffffff",
            text="ЦВЕТ ОТСЕКАТЕЛЯ"
        )

        self.cutcolorpicker = tk.Button(self)
        self.cutcolorpicker.place(relx=0.031, rely=0.079, height=42, width=476)
        self.cutcolorpicker.configure(
            background=self.cut_color,
            activebackground=self.cut_color,
            font="-family {Consolas} -size 14",
            command=lambda: self.get_color(self.cutcolorpicker, self.cut_color)
        )

        self.figurecolorlb = tk.Label(self)
        self.figurecolorlb.place(relx=0.031, rely=0.119, height=57, width=476)
        self.figurecolorlb.configure(
            activebackground="#000080",
            activeforeground="white",
            background="#000080",
            font="-family {Consolas} -size 18",
            foreground="#ffffff",
            text="ЦВЕТ ОТРЕЗКОВ"
        )

        self.figurecolorpicker = tk.Button(self)
        self.figurecolorpicker.place(relx=0.031, rely=0.168, height=42, width=476)
        self.figurecolorpicker.configure(
            background=self.figure_color,
            activebackground=self.figure_color,
            font="-family {Consolas} -size 14",
            command=lambda: self.get_color(self.figurecolorpicker, self.figure_color)
        )

        self.rescolorlb = tk.Label(self)
        self.rescolorlb.place(relx=0.031, rely=0.208, height=56, width=476)
        self.rescolorlb.configure(
            activebackground="#000080",
            activeforeground="white",
            background="#000080",
            font="-family {Consolas} -size 18",
            foreground="#ffffff",
            text="ЦВЕТ РЕЗУЛЬТАТА"
        )

        self.rescolorpicker = tk.Button(self)
        self.rescolorpicker.place(relx=0.031, rely=0.258, height=43, width=476)
        self.rescolorpicker.configure(
            background=self.res_color,
            activebackground=self.res_color,
            font="-family {Consolas} -size 14",
            command=lambda: self.get_color(self.rescolorpicker, self.res_color)
        )

        # Borders section.
        self.cutlb = tk.Label(self)
        self.cutlb.place(relx=0.031, rely=0.317, height=56, width=476)
        self.cutlb.configure(
            activebackground="#000080",
            activeforeground="white",
            background="#000080",
            font="-family {Consolas} -size 18",
            foreground="#ffffff",
            text="КООРДИНАТЫ ВЕРШИНЫ ОТСЕКАТЕЛЯ"
        )

        self.xclb = tk.Label(self)
        self.xclb.place(relx=0.031, rely=0.357, height=36, width=232)
        self.xclb.configure(
            activebackground="#000080",
            activeforeground="white",
            background="#000080",
            font="-family {Consolas} -size 14",
            foreground="#ffffff",
            text="X"
        )

        self.yclb = tk.Label(self)
        self.yclb.place(relx=0.152, rely=0.357, height=36, width=232)
        self.yclb.configure(
            activebackground="#000080",
            activeforeground="white",
            background="#000080",
            font="-family {Consolas} -size 14",
            foreground="#ffffff",
            text="Y"
        )

        self.xcsb = tk.Spinbox(self)
        self.xcsb.place(relx=0.031, rely=0.387, relheight=0.03, relwidth=0.126)
        self.xcsb.configure(
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

        self.ycsb = tk.Spinbox(self)
        self.ycsb.place(relx=0.157, rely=0.387, relheight=0.03, relwidth=0.126)
        self.ycsb.configure(
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

        self.addcbtn = tk.Button(self)
        self.addcbtn.place(relx=0.031, rely=0.426, height=43, width=476)
        self.addcbtn.configure(
            background="#d9d9d9",
            foreground="black",
            activebackground="#000080",
            font="-family {Consolas} -size 14",
            text="Добавить точку отсекателя",
            command=self.add_cut
        )

        self.lockbtn = tk.Button(self)
        self.lockbtn.place(relx=0.031, rely=0.486, height=43, width=476)
        self.lockbtn.configure(
            background="#d9d9d9",
            foreground="black",
            activebackground="#000080",
            font="-family {Consolas} -size 14",
            text="Замкнуть",
            command=self.cutclose
        )

        # New dot section.
        self.dotlb = tk.Label(self)
        self.dotlb.place(relx=0.031, rely=0.555, height=56, width=476)
        self.dotlb.configure(
            activebackground="#000080",
            activeforeground="white",
            background="#000080",
            font="-family {Consolas} -size 18",
            foreground="#ffffff",
            text="КООРДИНАТЫ ТОЧКИ"
        )

        self.xlb = tk.Label(self)
        self.xlb.place(relx=0.031, rely=0.599, height=36, width=240)
        self.xlb.configure(
            activebackground="#000080",
            activeforeground="white",
            background="#000080",
            font="-family {Consolas} -size 14",
            foreground="#ffffff",
            text="X"
        )

        self.ylb = tk.Label(self)
        self.ylb.place(relx=0.157, rely=0.599, height=36, width=240)
        self.ylb.configure(
            activebackground="#000080",
            activeforeground="white",
            background="#000080",
            font="-family {Consolas} -size 14",
            foreground="#ffffff",
            text="Y"
        )

        self.xsb = tk.Spinbox(self)
        self.xsb.place(relx=0.031, rely=0.64, relheight=0.03, relwidth=0.126)
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
        self.ysb.place(relx=0.157, rely=0.64, relheight=0.03, relwidth=0.126)
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
        self.addbtn.place(relx=0.031, rely=0.684, height=42, width=477)
        self.addbtn.configure(
            background="#d9d9d9",
            foreground="black",
            activebackground="#000080",
            font="-family {Consolas} -size 14",
            text="Добавить точку",
            command=self.add_dot
        )

        self.cutbtn = tk.Button(self)
        self.cutbtn.place(relx=0.031, rely=0.862, height=40, width=476)
        self.cutbtn.configure(
            background="#d9d9d9",
            foreground="black",
            activebackground="#000080",
            font="-family {Consolas} -size 14",
            text="Отсечь",
            command=lambda: cut.cut(ROOT)
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
        self.cut = []
        self.figure = []

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

    def draw_figure(self, figure, color):
        for section in figure:
            self.draw_line(*section, color)

    def pixclick(self, event):
        self.figure.append([event.x, event.y])
        if len(self.figure) > 1:
            self.draw_line(self.figure[-1], self.figure[-2], self.figure_color)

    def pixclose(self):
        if len(self.figure) < 3:
            return
        self.draw_line(self.figure[-1], self.figure[0], self.figure_color)

    def cutclick(self, event):
        self.cut.append([event.x, event.y])
        if len(self.cut) > 1:
            self.draw_line(self.cut[-1], self.cut[-2], self.cut_color)

    def cutclose(self):
        if len(self.cut) < 3:
            return
        self.draw_line(self.cut[-1], self.cut[0], self.cut_color)

    def add_dot(self):
        self.figure.append([int(self.xsb.get()), int(self.ysb.get())])
        if len(self.figure) > 1:
            self.draw_line(self.figure[-1], self.figure[-2], self.figure_color)

    def add_cut(self):
        self.cut.append([int(self.xcsb.get()), int(self.ycsb.get())])
        if len(self.cut) > 1:
            self.draw_line(self.cut[-1], self.cut[-2], self.cut_color)


if __name__ == "__main__":
    ROOT = RootWindow()
    ROOT.mainloop()
