import tkinter
from tkinter import *
from tkinter import messagebox
import math

window = Tk()
window.title("Определение простого числа или сложного")
window.geometry('400x300')

def types_1():
    one_true = int(height_main_inf.get()) #парсим инпуты
    simple = True
    i = 2
    while i < one_true:
        if one_true % i == 0:
            simple = False
        i += 1

    if simple:
        messagebox.showinfo('простое','простое')
    else:
        messagebox.showinfo('сложное','сложное')
#парсим инпуты

#указываем заготовку
frame = Frame(
    window,
    padx=10,
    pady=10
)
frame.pack(expand=True) # растягивание фрейма во всё поле
#указываем заготовку


# поле тайтла
height_main = Label(
    frame,
    text="Введите число")
height_main.grid(row=3, column=1)
# поле тайтла


# поле ввода
height_main_inf = Entry(
    frame,
)
height_main_inf.grid(row=4, column=1)
# поле ввода


#Создаём кнопки и события
Calc_btn = Button(
    frame,
    text = 'определить',
    command = types_1
)
Calc_btn.grid(row=5, column=1)
#Создаём кнопки и события

window.mainloop()
