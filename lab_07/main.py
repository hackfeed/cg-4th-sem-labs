import tkinter as tk
from tkinter import colorchooser


class RootWindow(tk.Tk):
    """
        Representation of root program window.
    """

    cut_color = "#FF0000"
    section_color = "#00FF00"
    res_color = "#0000FF"
    cut = [None, None, None, None]
    top_left_cut = [None, None]
    sections = []
    last_dot = [None, None]

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        img = tk.PhotoImage(file="assets/img/icon.png")

        self.geometry("1910x1000+0+0")
        self.minsize(1, 1)
        self.maxsize(1920, 1010)
        self.resizable(0, 0)
        self.title("Middle cut")
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
        self.canvas.bind("<Button-3>", lambda event: self.cutclick(event))

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
            activebackground="black",
            font="-family {Consolas} -size 14",
            command=lambda: self.get_color(self.cutcolorpicker, self.cut_color)
        )

        self.sectioncolorlb = tk.Label(self)
        self.sectioncolorlb.place(relx=0.031, rely=0.119, height=57, width=476)
        self.sectioncolorlb.configure(
            activebackground="#000080",
            activeforeground="white",
            background="#000080",
            font="-family {Consolas} -size 18",
            foreground="#ffffff",
            text="ЦВЕТ ОТРЕЗКОВ"
        )

        self.sectioncolorpicker = tk.Button(self)
        self.sectioncolorpicker.place(relx=0.031, rely=0.168, height=42, width=476)
        self.sectioncolorpicker.configure(
            background=self.section_color,
            activebackground="black",
            font="-family {Consolas} -size 14",
            command=lambda: self.get_color(self.sectioncolorpicker, self.section_color)
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
            activebackground="black",
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
            text="ГРАНИЦЫ ОТСЕКАТЕЛЯ"
        )

        self.xullb = tk.Label(self)
        self.xullb.place(relx=0.031, rely=0.357, height=36, width=232)
        self.xullb.configure(
            activebackground="#000080",
            activeforeground="white",
            background="#000080",
            font="-family {Consolas} -size 14",
            foreground="#ffffff",
            text="Xлв"
        )

        self.yullb = tk.Label(self)
        self.yullb.place(relx=0.152, rely=0.357, height=36, width=232)
        self.yullb.configure(
            activebackground="#000080",
            activeforeground="white",
            background="#000080",
            font="-family {Consolas} -size 14",
            foreground="#ffffff",
            text="Yлв"
        )

        self.xulsb = tk.Spinbox(self)
        self.xulsb.place(relx=0.031, rely=0.387, relheight=0.03, relwidth=0.126)
        self.xulsb.configure(
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

        self.yulsb = tk.Spinbox(self)
        self.yulsb.place(relx=0.157, rely=0.387, relheight=0.03, relwidth=0.126)
        self.yulsb.configure(
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

        self.xldlb = tk.Label(self)
        self.xldlb.place(relx=0.031, rely=0.416, height=36, width=232)
        self.xldlb.configure(
            activebackground="#000080",
            activeforeground="white",
            background="#000080",
            font="-family {Consolas} -size 14",
            foreground="#ffffff",
            text="Xпн"
        )

        self.yldlb = tk.Label(self)
        self.yldlb.place(relx=0.152, rely=0.416, height=36, width=232)
        self.yldlb.configure(
            activebackground="#000080",
            activeforeground="white",
            background="#000080",
            font="-family {Consolas} -size 14",
            foreground="#ffffff",
            text="Yпн"
        )

        self.xldsb = tk.Spinbox(self)
        self.xldsb.place(relx=0.031, rely=0.446, relheight=0.03, relwidth=0.126)
        self.xldsb.configure(
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

        self.yldsb = tk.Spinbox(self)
        self.yldsb.place(relx=0.157, rely=0.446, relheight=0.03, relwidth=0.126)
        self.yldsb.configure(
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

        self.applybtn = tk.Button(self)
        self.applybtn.place(relx=0.031, rely=0.486, height=43, width=476)
        self.applybtn.configure(
            background="#d9d9d9",
            foreground="black",
            activebackground="#000080",
            font="-family {Consolas} -size 14",
            text="Применить",
            command=self.add_cut
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
            text="Отсечь"
            # command=lambda: fill.fill(ROOT)
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
        self.cut = [None, None, None, None]
        self.sections = []
        self.top_left_cut = [None, None]

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
        self.canvas.create_line(dot_start[0], dot_start[1], dot_end[0], dot_end[1], fill=color)

    def draw_cut(self, top_left, bottom_right, color):
        self.canvas.create_rectangle(top_left[0], top_left[1],
                                     bottom_right[0], bottom_right[1], outline=color)

    def pixclick(self, event):
        if self.last_dot[0]:
            self.sections.append([self.last_dot.copy(), [event.x, event.y]])
            self.draw_line(self.sections[-1], self.sections[-1], self.section_color)
            self.last_dot[0] = None
        else:
            self.last_dot[0], self.last_dot[1] = event.x, event.y

    def cutclick(self, event):
        if self.top_left_cut[0]:
            self.cut = [self.top_left_cut[0], self.top_left_cut[1], event.x, event.y]
            self.draw_cut([self.cut[0], self.cut[1]], [self.cut[2], self.cut[3]], self.cut_color)
        else:
            self.reset()
            self.top_left_cut[0], self.top_left_cut[1] = event.x, event.y

    def add_dot(self):
        if self.last_dot[0]:
            self.sections.append([self.last_dot.copy(), [int(self.xsb.get()), int(self.ysb.get())]])
            self.draw_line(self.sections[-1], self.sections[-1], self.section_color)
            self.last_dot[0] = None
        else:
            self.last_dot[0], self.last_dot[1] = int(self.xsb.get()), int(self.ysb.get())

    def add_cut(self):
        self.reset()
        self.cut = [int(self.xulsb.get()), int(self.yulsb.get()),
                    int(self.xldsb.get()), int(self.yldsb.get())]
        self.draw_cut([self.cut[0], self.cut[1]], [self.cut[2], self.cut[3]], self.cut_color)


if __name__ == "__main__":
    ROOT = RootWindow()
    ROOT.mainloop()
