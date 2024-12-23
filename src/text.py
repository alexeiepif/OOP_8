#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Решите задачу: напишите программу по описанию. Размеры многострочного текстового поля
# определяются значениями, введенными в однострочные текстовые поля. Изменение
# размера происходит при нажатии мышью на кнопку, а также при нажатии клавиши Enter.
# Цвет фона экземпляра Text светлосерый ( lightgrey ), когда поле не в фокусе, и белый,
# когда имеет фокус.

import tkinter as tk
from typing import Any


def change_size(event: Any, e1: tk.Entry, e2: tk.Entry, t1: tk.Text) -> None:
    try:
        width = int(e1.get())
        t1.config(width=width)
    except ValueError:
        pass

    try:
        height = int(e2.get())
        t1.config(height=height)
    except ValueError:
        pass


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Текст")
    root.minsize(300, 300)

    f1 = tk.Frame(root)
    f1.pack()

    f2 = tk.Frame(f1)
    f2.pack(side="left")

    e1 = tk.Entry(f2)
    e1.pack()

    e2 = tk.Entry(f2)
    e2.pack()

    b1 = tk.Button(f1, text="Изменить")
    b1.pack(side="left", padx=5)

    t1 = tk.Text(root, bg="lightgrey", width=40, height=24)
    t1.pack()

    b1.bind("<Button-1>", lambda event: change_size(event, e1, e2, t1))
    e1.bind("<Return>", lambda event: change_size(event, e1, e2, t1))
    e2.bind("<Return>", lambda event: change_size(event, e1, e2, t1))
    t1.bind("<FocusIn>", lambda event: t1.config(bg="white"))
    t1.bind("<FocusOut>", lambda event: t1.config(bg="lightgrey"))

    root.mainloop()
