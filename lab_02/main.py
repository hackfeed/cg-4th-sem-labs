"""
    Main routine.
"""

import tkinter as tk
from imgact.draw import Fish
from imgact import view


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

        # Move section.
        self.movelabel = tk.Label(self)
        self.movelabel.place(relx=0.038, rely=0.042, height=41, width=320)
        self.movelabel.configure(
            activebackground="#000080",
            activeforeground="white",
            background="#000080",
            font="-family {Consolas} -size 18",
            foreground="#ffffff",
            text="ПЕРЕМЕЩЕНИЕ"
        )

        self.dxmovelabel = tk.Label(self)
        self.dxmovelabel.place(relx=0.038, rely=0.111, height=19, width=160)
        self.dxmovelabel.configure(
            activebackground="#f9f9f9",
            background="#000080",
            font="-family {Consolas} -size 14",
            foreground="#ffffff",
            text="dx"
        )

        self.dymovelabel = tk.Label(self)
        self.dymovelabel.place(relx=0.163, rely=0.111, height=19, width=160)
        self.dymovelabel.configure(
            activebackground="#f9f9f9",
            background="#000080",
            font="-family {Consolas} -size 14",
            foreground="#ffffff",
            text="dy"
        )

        self.dxmove = tk.Entry(self)
        self.dxmove.place(relx=0.038, rely=0.153, height=50, relwidth=0.125)
        self.dxmove.configure(
            background="white",
            foreground="black",
            justify="center",
            highlightthickness=0,
            font="-family {Consolas} -size 14",
            selectbackground="#c4c4c4"
        )
        self.dxmove.insert(tk.END, "0")

        self.dymove = tk.Entry(self)
        self.dymove.place(relx=0.163, rely=0.153, height=50, relwidth=0.125)
        self.dymove.configure(
            background="white",
            foreground="black",
            justify="center",
            highlightthickness=0,
            font="-family {Consolas} -size 14",
            selectbackground="#c4c4c4"
        )
        self.dymove.insert(tk.END, "0")

        self.movebtn = tk.Button(self)
        self.movebtn.place(relx=0.039, rely=0.236, height=29, width=320)
        self.movebtn.configure(
            background="#d9d9d9",
            foreground="black",
            activebackground="#000080",
            font="-family {Consolas} -size 14",
            text="Переместить",
            command=lambda: view.move(ROOT, FISH, STATES)
        )

        # Rotate section.
        self.rotatelabel = tk.Label(self)
        self.rotatelabel.place(relx=0.039, rely=0.306, height=41, width=320)
        self.rotatelabel.configure(
            activebackground="#000080",
            activeforeground="white",
            background="#000080",
            font="-family {Consolas} -size 18",
            foreground="#ffffff",
            text="ПОВОРОТ"
        )

        self.xrotatelabel = tk.Label(self)
        self.xrotatelabel.place(relx=0.038, rely=0.375, height=19, width=107)
        self.xrotatelabel.configure(
            activebackground="#f9f9f9",
            background="#000080",
            font="-family {Consolas} -size 14",
            foreground="#ffffff",
            text="Rx"
        )

        self.yrotatelabel = tk.Label(self)
        self.yrotatelabel.place(relx=0.121, rely=0.375, height=18, width=107)
        self.yrotatelabel.configure(
            activebackground="#f9f9f9",
            background="#000080",
            font="-family {Consolas} -size 14",
            foreground="#ffffff",
            text="Ry"
        )

        self.angrotatelabel = tk.Label(self)
        self.angrotatelabel.place(relx=0.203, rely=0.375, height=18, width=107)
        self.angrotatelabel.configure(
            activebackground="#f9f9f9",
            background="#000080",
            font="-family {Consolas} -size 14",
            foreground="#ffffff",
            text="Угол°"
        )

        self.xrotate = tk.Entry(self)
        self.xrotate.place(relx=0.038, rely=0.417, height=50, relwidth=0.084)
        self.xrotate.configure(
            background="white",
            foreground="black",
            justify="center",
            highlightthickness=0,
            font="-family {Consolas} -size 14",
            selectbackground="#c4c4c4"
        )
        self.xrotate.insert(tk.END, "420")

        self.yrotate = tk.Entry(self)
        self.yrotate.place(relx=0.121, rely=0.417, height=50, relwidth=0.084)
        self.yrotate.configure(
            background="white",
            foreground="black",
            justify="center",
            highlightthickness=0,
            font="-family {Consolas} -size 14",
            selectbackground="#c4c4c4"
        )
        self.yrotate.insert(tk.END, "340")

        self.angrotate = tk.Entry(self)
        self.angrotate.place(relx=0.205, rely=0.417, height=50, relwidth=0.084)
        self.angrotate.configure(
            background="white",
            foreground="black",
            justify="center",
            highlightthickness=0,
            font="-family {Consolas} -size 14",
            selectbackground="#c4c4c4"
        )
        self.angrotate.insert(tk.END, "0")

        self.rotatebtn = tk.Button(self)
        self.rotatebtn.place(relx=0.039, rely=0.5, height=29, width=320)
        self.rotatebtn.configure(
            background="#d9d9d9",
            foreground="black",
            activebackground="#000080",
            font="-family {Consolas} -size 14",
            text="Повернуть",
            command=lambda: view.rotate(ROOT, FISH, STATES)
        )

        # Scale section.
        self.scalelabel = tk.Label(self)
        self.scalelabel.place(relx=0.039, rely=0.556, height=41, width=320)
        self.scalelabel.configure(
            activebackground="#000080",
            activeforeground="white",
            background="#000080",
            font="-family {Consolas} -size 18",
            foreground="#ffffff",
            text="МАСШТАБИРОВАНИЕ"
        )

        self.xscalelabel = tk.Label(self)
        self.xscalelabel.place(relx=0.039, rely=0.625, height=18, width=81)
        self.xscalelabel.configure(
            activebackground="#f9f9f9",
            background="#000080",
            font="-family {Consolas} -size 14",
            foreground="#ffffff",
            text="Mx"
        )

        self.yscalelabel = tk.Label(self)
        self.yscalelabel.place(relx=0.102, rely=0.625, height=18, width=80)
        self.yscalelabel.configure(
            activebackground="#f9f9f9",
            background="#000080",
            font="-family {Consolas} -size 14",
            foreground="#ffffff",
            text="My"
        )

        self.kxscalelabel = tk.Label(self)
        self.kxscalelabel.place(relx=0.164, rely=0.625, height=18, width=81)
        self.kxscalelabel.configure(
            activebackground="#f9f9f9",
            background="#000080",
            font="-family {Consolas} -size 14",
            foreground="#ffffff",
            text="kx"
        )

        self.kyscalelabel = tk.Label(self)
        self.kyscalelabel.place(relx=0.227, rely=0.625, height=18, width=80)
        self.kyscalelabel.configure(
            activebackground="#f9f9f9",
            background="#000080",
            font="-family {Consolas} -size 14",
            foreground="#ffffff",
            text="ky"
        )

        self.xscale = tk.Entry(self)
        self.xscale.place(relx=0.038, rely=0.667, height=50, relwidth=0.063)
        self.xscale.configure(
            background="white",
            foreground="black",
            justify="center",
            highlightthickness=0,
            font="-family {Consolas} -size 14",
            selectbackground="#c4c4c4"
        )
        self.xscale.insert(tk.END, "420")

        self.yscale = tk.Entry(self)
        self.yscale.place(relx=0.101, rely=0.667, height=50, relwidth=0.063)
        self.yscale.configure(
            background="white",
            foreground="black",
            justify="center",
            highlightthickness=0,
            font="-family {Consolas} -size 14",
            selectbackground="#c4c4c4"
        )
        self.yscale.insert(tk.END, "340")

        self.kxscale = tk.Entry(self)
        self.kxscale.place(relx=0.163, rely=0.667, height=50, relwidth=0.063)
        self.kxscale.configure(
            background="white",
            foreground="black",
            justify="center",
            highlightthickness=0,
            font="-family {Consolas} -size 14",
            selectbackground="#c4c4c4"
        )
        self.kxscale.insert(tk.END, "1")

        self.kyscale = tk.Entry(self)
        self.kyscale.place(relx=0.226, rely=0.667, height=50, relwidth=0.063)
        self.kyscale.configure(
            background="white",
            foreground="black",
            justify="center",
            highlightthickness=0,
            font="-family {Consolas} -size 14",
            selectbackground="#c4c4c4"
        )
        self.kyscale.insert(tk.END, "1")

        self.scalebtn = tk.Button(self)
        self.scalebtn.place(relx=0.039, rely=0.75, height=29, width=320)
        self.scalebtn.configure(
            background="#d9d9d9",
            foreground="black",
            activebackground="#000080",
            font="-family {Consolas} -size 14",
            text="Масштабировать",
            command=lambda: view.scale(ROOT, FISH, STATES)
        )

        # Additional buttons.
        self.backbtn = tk.Button(self)
        self.backbtn.place(relx=0.039, rely=0.861, height=29, width=320)
        self.backbtn.configure(
            state="disabled",
            background="#d9d9d9",
            foreground="black",
            activebackground="#000080",
            font="-family {Consolas} -size 14",
            text="Шаг назад",
            command=lambda: view.step_back(ROOT, STATES)
        )

        self.resetbtn = tk.Button(self)
        self.resetbtn.place(relx=0.039, rely=0.917, height=29, width=320)
        self.resetbtn.configure(
            background="#d9d9d9",
            foreground="black",
            activebackground="#000080",
            font="-family {Consolas} -size 14",
            text="Сброс",
            command=lambda: view.reset(ROOT, FISH, STATES)
        )


if __name__ == "__main__":
    ROOT = RootWindow()
    STATES = []
    FISH = Fish()
    FISH.scale(420, 340, 0.7, 0.7)
    FISH.draw(ROOT.image)
    ROOT.mainloop()
