import tkinter as tk
from tkinter import messagebox


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
        self.resizable(0, 0)
        self.title("Image Actions")
        self.iconphoto(True, img)
        self.configure(background="#000080")
        self.configure(highlightcolor="black")

        self.image = tk.Canvas(self)
        self.image.place(relx=0.328, rely=0.028, relheight=0.944, relwidth=0.656)
        self.image.configure(background="#ffffff")
        self.image.configure(borderwidth="2")
        self.image.configure(relief="ridge")
        self.image.configure(selectbackground="#c4c4c4")

        self.dxmove = tk.Entry(self)
        self.dxmove.place(relx=0.038, rely=0.153, height=50, relwidth=0.125)
        self.dxmove.configure(background="white")
        self.dxmove.configure(font="-family {Consolas} -size 14")
        self.dxmove.configure(selectbackground="#c4c4c4")

        self.dymove = tk.Entry(self)
        self.dymove.place(relx=0.163, rely=0.153, height=50, relwidth=0.125)
        self.dymove.configure(background="white")
        self.dymove.configure(font="-family {Consolas} -size 14")
        self.dymove.configure(selectbackground="#c4c4c4")

        self.xrotate = tk.Entry(self)
        self.xrotate.place(relx=0.038, rely=0.417, height=50, relwidth=0.084)
        self.xrotate.configure(background="white")
        self.xrotate.configure(font="-family {Consolas} -size 14")
        self.xrotate.configure(selectbackground="#c4c4c4")

        self.yrotate = tk.Entry(self)
        self.yrotate.place(relx=0.121, rely=0.417, height=50, relwidth=0.084)
        self.yrotate.configure(background="white")
        self.yrotate.configure(font="-family {Consolas} -size 14")
        self.yrotate.configure(selectbackground="#c4c4c4")

        self.angrotate = tk.Entry(self)
        self.angrotate.place(relx=0.205, rely=0.417, height=50, relwidth=0.084)
        self.angrotate.configure(background="white")
        self.angrotate.configure(font="-family {Consolas} -size 14")
        self.angrotate.configure(selectbackground="#c4c4c4")

        self.xscale = tk.Entry(self)
        self.xscale.place(relx=0.038, rely=0.667, height=50, relwidth=0.063)
        self.xscale.configure(background="white")
        self.xscale.configure(font="-family {Consolas} -size 14")
        self.xscale.configure(selectbackground="#c4c4c4")

        self.yscale = tk.Entry(self)
        self.yscale.place(relx=0.101, rely=0.667, height=50, relwidth=0.063)
        self.yscale.configure(background="white")
        self.yscale.configure(font="-family {Consolas} -size 14")
        self.yscale.configure(selectbackground="#c4c4c4")

        self.kxscale = tk.Entry(self)
        self.kxscale.place(relx=0.163, rely=0.667, height=50, relwidth=0.063)
        self.kxscale.configure(background="white")
        self.kxscale.configure(font="-family {Consolas} -size 14")
        self.kxscale.configure(selectbackground="#c4c4c4")

        self.kyscale = tk.Entry(self)
        self.kyscale.place(relx=0.226, rely=0.667, height=50, relwidth=0.063)
        self.kyscale.configure(background="white")
        self.kyscale.configure(font="-family {Consolas} -size 14")
        self.kyscale.configure(selectbackground="#c4c4c4")

        self.movelabel = tk.Label(self)
        self.movelabel.place(relx=0.038, rely=0.042, height=41, width=320)
        self.movelabel.configure(activebackground="#000080")
        self.movelabel.configure(activeforeground="white")
        self.movelabel.configure(background="#000080")
        self.movelabel.configure(font="-family {Consolas} -size 18")
        self.movelabel.configure(foreground="#ffffff")
        self.movelabel.configure(text="ПЕРЕМЕЩЕНИЕ")

        self.dxmovelabel = tk.Label(self)
        self.dxmovelabel.place(relx=0.038, rely=0.111, height=19, width=160)
        self.dxmovelabel.configure(activebackground="#f9f9f9")
        self.dxmovelabel.configure(background="#000080")
        self.dxmovelabel.configure(font="-family {Consolas} -size 14")
        self.dxmovelabel.configure(foreground="#ffffff")
        self.dxmovelabel.configure(text="dx - по оси X")

        self.dymovelabel = tk.Label(self)
        self.dymovelabel.place(relx=0.163, rely=0.111, height=19, width=160)
        self.dymovelabel.configure(activebackground="#f9f9f9")
        self.dymovelabel.configure(background="#000080")
        self.dymovelabel.configure(font="-family {Consolas} -size 14")
        self.dymovelabel.configure(foreground="#ffffff")
        self.dymovelabel.configure(text="dy - по оси Y")

        self.movebtn = tk.Button(self)
        self.movebtn.place(relx=0.039, rely=0.236, height=29, width=320)
        self.movebtn.configure(activebackground="#f9f9f9")
        self.movebtn.configure(font="-family {Consolas} -size 14")
        self.movebtn.configure(text="Переместить")

        self.rotatelabel = tk.Label(self)
        self.rotatelabel.place(relx=0.039, rely=0.306, height=41, width=320)
        self.rotatelabel.configure(activebackground="#000080")
        self.rotatelabel.configure(activeforeground="white")
        self.rotatelabel.configure(background="#000080")
        self.rotatelabel.configure(font="-family {Consolas} -size 18")
        self.rotatelabel.configure(foreground="#ffffff")
        self.rotatelabel.configure(text="ПОВОРОТ")

        self.xrotatelabel = tk.Label(self)
        self.xrotatelabel.place(relx=0.038, rely=0.375, height=19, width=107)
        self.xrotatelabel.configure(activebackground="#f9f9f9")
        self.xrotatelabel.configure(background="#000080")
        self.xrotatelabel.configure(font="-family {Consolas} -size 14")
        self.xrotatelabel.configure(foreground="#ffffff")
        self.xrotatelabel.configure(text="Rx")

        self.yrotatelabel = tk.Label(self)
        self.yrotatelabel.place(relx=0.121, rely=0.375, height=18, width=107)
        self.yrotatelabel.configure(activebackground="#f9f9f9")
        self.yrotatelabel.configure(background="#000080")
        self.yrotatelabel.configure(font="-family {Consolas} -size 14")
        self.yrotatelabel.configure(foreground="#ffffff")
        self.yrotatelabel.configure(text="Ry")

        self.angrotatelabel = tk.Label(self)
        self.angrotatelabel.place(relx=0.203, rely=0.375, height=18, width=107)
        self.angrotatelabel.configure(activebackground="#f9f9f9")
        self.angrotatelabel.configure(background="#000080")
        self.angrotatelabel.configure(font="-family {Consolas} -size 14")
        self.angrotatelabel.configure(foreground="#ffffff")
        self.angrotatelabel.configure(text="Угол°")

        self.rotatebtn = tk.Button(self)
        self.rotatebtn.place(relx=0.039, rely=0.5, height=29, width=320)
        self.rotatebtn.configure(activebackground="#f9f9f9")
        self.rotatebtn.configure(font="-family {Consolas} -size 14")
        self.rotatebtn.configure(text="Повернуть")

        self.scalelabel = tk.Label(self)
        self.scalelabel.place(relx=0.039, rely=0.556, height=41, width=320)
        self.scalelabel.configure(activebackground="#000080")
        self.scalelabel.configure(activeforeground="white")
        self.scalelabel.configure(background="#000080")
        self.scalelabel.configure(font="-family {Consolas} -size 18")
        self.scalelabel.configure(foreground="#ffffff")
        self.scalelabel.configure(text="МАСШТАБИРОВАНИЕ")

        self.xscalelabel = tk.Label(self)
        self.xscalelabel.place(relx=0.039, rely=0.625, height=18, width=81)
        self.xscalelabel.configure(activebackground="#f9f9f9")
        self.xscalelabel.configure(background="#000080")
        self.xscalelabel.configure(font="-family {Consolas} -size 14")
        self.xscalelabel.configure(foreground="#ffffff")
        self.xscalelabel.configure(text="Mx")

        self.yscalelabel = tk.Label(self)
        self.yscalelabel.place(relx=0.102, rely=0.625, height=18, width=80)
        self.yscalelabel.configure(activebackground="#f9f9f9")
        self.yscalelabel.configure(background="#000080")
        self.yscalelabel.configure(font="-family {Consolas} -size 14")
        self.yscalelabel.configure(foreground="#ffffff")
        self.yscalelabel.configure(text="My")

        self.kxscalelabel = tk.Label(self)
        self.kxscalelabel.place(relx=0.164, rely=0.625, height=18, width=81)
        self.kxscalelabel.configure(activebackground="#f9f9f9")
        self.kxscalelabel.configure(background="#000080")
        self.kxscalelabel.configure(font="-family {Consolas} -size 14")
        self.kxscalelabel.configure(foreground="#ffffff")
        self.kxscalelabel.configure(text="kx")

        self.kyscalelabel = tk.Label(self)
        self.kyscalelabel.place(relx=0.227, rely=0.625, height=18, width=80)
        self.kyscalelabel.configure(activebackground="#f9f9f9")
        self.kyscalelabel.configure(background="#000080")
        self.kyscalelabel.configure(font="-family {Consolas} -size 14")
        self.kyscalelabel.configure(foreground="#ffffff")
        self.kyscalelabel.configure(text="ky")

        self.scalebtn = tk.Button(self)
        self.scalebtn.place(relx=0.039, rely=0.75, height=29, width=320)
        self.scalebtn.configure(activebackground="#f9f9f9")
        self.scalebtn.configure(font="-family {Consolas} -size 14")
        self.scalebtn.configure(text="Масштабировать")

        self.backbtn = tk.Button(self)
        self.backbtn.place(relx=0.039, rely=0.861, height=29, width=320)
        self.backbtn.configure(activebackground="#f9f9f9")
        self.backbtn.configure(font="-family {Consolas} -size 14")
        self.backbtn.configure(text="Шаг назад")

        self.resetbtn = tk.Button(self)
        self.resetbtn.place(relx=0.039, rely=0.917, height=29, width=320)
        self.resetbtn.configure(activebackground="#f9f9f9")
        self.resetbtn.configure(font="-family {Consolas} -size 14")
        self.resetbtn.configure(text="Сброс")


if __name__ == "__main__":
    ROOT = RootWindow()
    ROOT.mainloop()