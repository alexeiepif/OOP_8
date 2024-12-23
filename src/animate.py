#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk

# Решите задачу: в данной программе создается анимация круга, который движется
# от левой границы холста до правой: Выражение c.coords(ball) возвращает список
# текущих координат объекта (в данном случае это ball). Третий элемент списка
# соответствует его второй координате x. Метод after вызывает функцию, переданную
# вторым аргументом, через количество миллисекунд, указанных первым аргументом.
# Изучите приведенную программу и самостоятельно запрограммируйте постепенное
# движение фигуры в ту точку холста, где пользователь кликает левой кнопкой мыши.


def update_target(event: tk.Event) -> None:  # type: ignore
    global target
    target = (event.x, event.y)


def motion(c: tk.Canvas, ball) -> None:  # type: ignore
    global target
    if target != (-1, -1):
        center_x = (c.coords(ball)[0] + c.coords(ball)[2]) / 2
        center_y = (c.coords(ball)[1] + c.coords(ball)[3]) / 2
        k = ((center_x - target[0]) ** 2 + (center_y - target[1]) ** 2) ** 0.5
        if k > 1:
            move_x = 1 * (target[0] - center_x) / k
            move_y = 1 * (target[1] - center_y) / k
            c.move(ball, move_x, move_y)
        else:
            target = (-1, -1)

    root.after(10, lambda: motion(c, ball))


if __name__ == "__main__":
    global target
    target = (-1, -1)
    root = tk.Tk()
    c = tk.Canvas(root, width=300, height=200, bg="white")
    c.pack()
    ball = c.create_oval(0, 100, 40, 140, fill="green")
    motion(c, ball)
    c.bind("<Button-1>", lambda event: update_target(event))
    root.mainloop()
