#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Решите задачу: Создайте на холсте изображение
# Для создания травы используется цикл.

import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Изображение")
    root.geometry("300x300")

    canvas = tk.Canvas(root, bg="white")
    canvas.pack(fill="both", expand=True)

    canvas.create_oval(200, 10, 250, 60, fill="orange")

    canvas.create_rectangle(80, 150, 220, 270, fill="lightblue", width=0)

    canvas.create_polygon(60, 150, 150, 100, 240, 150, fill="lightblue")

    for i in range(0, 315, 10):
        canvas.create_line(
            i,
            260,
            i - 5,
            265,
            i - 9,
            270,
            i - 12,
            275,
            i - 14,
            280,
            i - 15,
            285,
            i - 15,
            300,
            fill="green",
            width=2,
        )  # type: ignore

    root.mainloop()
