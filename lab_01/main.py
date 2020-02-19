import tkinter as tk
import itertools as it
import math
import os


def clean_entry(*entries):
    for entry in entries:
        entry.config(state="normal")
        entry.delete(0, tk.END)


def about(root):
    """ Вывод окна "О программе" """
    about_window = tk.Toplevel(root)
    about_window.grab_set()
    about_window.iconbitmap("icon.png")
    about_window.geometry("330x200+425+250")
    about_window.resizable(False, False)
    about_window.title("О TriangleDots")
    about_window.config(bg="#000080")

    about_label1 = tk.Label(about_window,
                            text="\nВизуализация треугольника\n "
                            "содержащего одинаковое количество точек\n"
                            "из двух различных множеств,\n"
                            "построенного на точках из первого множества"
                            "\n\n"
                            "Kononenko Sergey ICS7-23B",
                            font="consolas 10",
                            bg="#000080",
                            fg="white")
    about_label1.pack()

    about_label2 = tk.Label(about_window,
                            text="@hackfeed",
                            font="consolas 10 bold",
                            bg="white",
                            fg="#000080")
    about_label2.pack()

    exit_about = tk.Button(about_window, text="Выйти",
                           width=6,
                           height=2,
                           font="consolas 10 bold",
                           bg="#000080",
                           fg="white",
                           relief="flat",
                           command=lambda: wexit(about_window))
    exit_about.pack()


def wexit(root):
    """ Выход из программы. """
    root.destroy()


def main():
    """ Создание каскада окна программы. """
    root = tk.Tk()
    root.iconbitmap("icon.png")
    root.geometry("400x200+400+200")
    root.resizable(False, False)
    root.title("TriangleDots")

    """ Создание меню. """
    main_menu = tk.Menu(root)
    root.config(menu=main_menu, bg="#000080")

    clean_menu = tk.Menu(main_menu, tearoff=0)
    clean_menu.add_command(label="Очистить поле ввода точек первого множества",
                           command=lambda: clean_entry(first_dot_set_entry))
    clean_menu.add_command(label="Очистить поле ввода точек второго множества",
                           command=lambda: clean_entry(second_dot_set_entry))
    clean_menu.add_separator()
    clean_menu.add_command(label="Очистить поле ввода точек обоих множеств",
                           command=lambda: clean_entry(first_dot_set_entry,
                                                       second_dot_set_entry))

    action_menu = tk.Menu(main_menu, tearoff=0)
    action_menu.add_command(label="Визуализировать",
                            command=lambda: draw_triangle(first_dot_set_entry,
                                                          second_dot_set_entry))

    about_menu = tk.Menu(main_menu, tearoff=0)
    about_menu.add_command(label="О программе", command=lambda: about())

    main_menu.add_cascade(label="Визуализация", menu=action_menu)
    main_menu.add_cascade(label="Очистка", menu=clean_menu)
    main_menu.add_cascade(label="Справка", menu=about_menu)

    """ Организация UI. """
    welcome_label = tk.Label(root,
                             text="Нахождение магического треугольника",
                             font="consolas 10 bold",
                             bg="white",
                             fg="#000080")
    welcome_label.place(x=200, y=20, anchor="center")

    first_dot_set_label = tk.Label(root,
                                   text="Введите координаты точек первого множества",
                                   font="consolas 10 bold",
                                   bg="#000080",
                                   fg="white")
    first_dot_set_label.place(x=200, y=45, anchor="center")

    first_dot_set_start = "x1 y1 ..."
    first_dot_set_entry = tk.Entry(root, width=60)
    first_dot_set_entry.insert(0, first_dot_set_start)
    first_dot_set_entry.place(x=200, y=65, anchor="center")

    second_dot_set_label = tk.Label(root,
                                    text="Введите координаты точек второго множества",
                                    font="consolas 10 bold",
                                    bg="#000080",
                                    fg="white")
    second_dot_set_label.place(x=200, y=85, anchor="center")

    second_dot_set_start = "x1 y1 ..."
    second_dot_set_entry = tk.Entry(root, width=60)
    second_dot_set_entry.insert(0, second_dot_set_start)
    second_dot_set_entry.place(x=200, y=105, anchor="center")

    draw_button = tk.Button(root, text="Визуализировать",
                            width=16,
                            height=2,
                            font="consolas 10 bold",
                            bg="white",
                            fg="#0ad325",
                            command=lambda: draw_triangle(first_dot_set_entry,
                                                          second_dot_set_entry))
    draw_button.place(x=130, y=145, anchor="center")

    exit_button = tk.Button(root, text="Выйти",
                            width=16,
                            height=2,
                            font="consolas 10 bold",
                            bg="white",
                            fg="#ff0000",
                            command=lambda: wexit(root))
    exit_button.place(x=270, y=145, anchor="center")

    root.mainloop()
