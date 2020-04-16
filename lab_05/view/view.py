from tkinter import colorchooser


def get_color(root):
    _, hex_code = colorchooser.askcolor(
        parent=root,
        title="Выюерите цвет для закрашивания",
        initialcolor="black"
    )
    root.colorpicker.configure(
        background=hex_code,
        activebackground=hex_code
    )

    return hex_code
