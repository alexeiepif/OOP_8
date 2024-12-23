#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Решите задачу: напишите программу по следующему описанию. Нажатие Enter в
# однострочном текстовом поле приводит к перемещению текста из него в список (экземпляр
# Listbox ). При двойном клике ( <Double-Button-1> ) по элементу-строке списка,
# она должна копироваться в текстовое поле.

import tkinter as tk
from typing import Any


def move_to_list(event: Any, l1: tk.Listbox) -> str:
    t1 = event.widget
    text = t1.get("1.0", tk.END)
    l1.insert(tk.END, text)
    t1.delete("1.0", tk.END)
    return "break"


def move_to_text(event: Any, t1: tk.Text) -> None:
    l1 = event.widget
    item = l1.get(l1.curselection())
    if item:
        t1.delete("1.0", tk.END)
        t1.insert("1.0", item)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Продукты")
    root.minsize(300, 300)

    t1 = tk.Text(root, width=30, height=10)
    t1.pack(side="left", padx=5, pady=5)

    l1 = tk.Listbox(root)
    l1.pack(side="left", fill="y")

    t1.bind("<Return>", lambda event: move_to_list(event, l1))
    l1.bind("<Double-Button-1>", lambda event: move_to_text(event, t1))

    root.mainloop()
