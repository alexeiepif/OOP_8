#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Решите задачу: напишите программу, состоящую из двух списков Listbox . В первом будет,
# например, перечень товаров, заданный программно. Второй изначально пуст, пусть это
# будет перечень покупок. При клике на одну кнопку товар должен переходить из одного
# списка в другой.
# При клике на вторую кнопку – возвращаться (человек передумал покупать).
# Предусмотрите возможность множественного выбора элементов списка и их перемещения.

import tkinter as tk


def move(l1: tk.Listbox, l2: tk.Listbox) -> None:
    selected_items = l1.curselection()  # type: ignore
    for item in reversed(selected_items):
        l2.insert("0", l1.get(item))
        l1.delete(item)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Продукты")
    root.minsize(300, 300)

    l1 = tk.Listbox(root, selectmode=tk.EXTENDED)
    l1.pack(side="left", fill="y")

    frame = tk.Frame(root)
    frame.pack(side="left")
    b1 = tk.Button(frame, text=">>", width=10)
    b1.pack(padx=5, pady=5)
    b2 = tk.Button(frame, text="<<", width=10)
    b2.pack(padx=5, pady=5)

    l2 = tk.Listbox(root, selectmode=tk.EXTENDED)
    l2.pack(side="left", fill="y")

    b1.config(command=lambda: move(l1, l2))
    b2.config(command=lambda: move(l2, l1))

    products = [
        "Хлеб",
        "Молоко",
        "Яблоки",
        "Бананы",
        "Апельсины",
    ]

    for product in products:
        l1.insert("end", product)

root.mainloop()
