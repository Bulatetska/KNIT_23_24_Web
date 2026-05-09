#Імпорт візуальної частини
import tkinter as tk
import customtkinter as ctk
import random as rn

# Візуальна частина
app = ctk.CTk()
app.geometry("500x700")
app.title("KAFE CALCULATOR")

# Текст
title_label = ctk.CTkLabel(app, text = "KFculation",
                           font = ("Arial", 40, "bold"))
title_label.place(x = 15, y = 20)

result_label = ctk.CTkLabel(app, text = "Result",
                           font = ("Arial", 40, "bold"))
result_label.place(x = 200, y = 550)

# Перевірка на цифри у полі
def field_numbers(num):
    if num == "" or num.isdigit():
        return True
    return False
vcmd = app.register(field_numbers)

# Поле введеня А
field_a = ctk.CTkEntry(app, width = 200,
                       height = 50,
                       text_color = "white",
                       font = ("Arial", 30, "bold"),
                       corner_radius = 20,
                       validate = "key",
                       validatecommand=(vcmd, "%P"))
field_a.place(x = 25, y = 100)

# Поле введеня Б
field_b = ctk.CTkEntry(app, width = 200,
                       height = 50,
                       text_color = "white",
                       font = ("Arial", 30, "bold"),
                       corner_radius = 20,
                       validate = "key",
                       validatecommand=(vcmd, "%P"))
field_b.place(x = 275, y = 100)

# Поле результату
field_result = ctk.CTkEntry(app, width = 350,
                       height = 50,
                       state = "disabled", 
                       text_color = "#A84CB3",
                       font = ("Arial", 30, "bold"),
                       corner_radius = 20)
field_result.place(x = 75, y = 600)

#Імпорт модуля для математики
import math

#Функція котра робить додаваня
def plus():
    try:
        A = int(field_a.get())
        B = int(field_b.get())
        field_result.configure(state="normal")
        field_result.delete(0, "end")
        field_result.insert(0, str(A + B))
        field_result.configure(state="disabled")
    except:
            field_result.configure(state="normal")
            field_result.delete(0, "end")
            field_result.insert(0, "Помилка вводу")
            field_result.configure(state="disabled")

#Функція котра робить відніманя
def minus():
    try:
        A = int(field_a.get())
        B = int(field_b.get())
        field_result.configure(state="normal")
        field_result.delete(0, "end")
        field_result.insert(0, str(A - B))
        field_result.configure(state="disabled")
    except:
            field_result.configure(state="normal")
            field_result.delete(0, "end")
            field_result.insert(0, "Помилка вводу")
            field_result.configure(state="disabled")

#Функція котра робить діленя
def divide():
    try:
        A = int(field_a.get())
        B = int(field_b.get())
        field_result.configure(state="normal")
        field_result.delete(0, "end")
        field_result.insert(0, str(A / B))
        field_result.configure(state="disabled")
    except:
            field_result.configure(state="normal")
            field_result.delete(0, "end")
            field_result.insert(0, "Помилка вводу")
            field_result.configure(state="disabled")

#Функція котра робить множення
def times():
    try:
        A = int(field_a.get())
        B = int(field_b.get())
        field_result.configure(state="normal")
        field_result.delete(0, "end")
        field_result.insert(0, str(A * B))
        field_result.configure(state="disabled")
    except:
            field_result.configure(state="normal")
            field_result.delete(0, "end")
            field_result.insert(0, "Помилка вводу")
            field_result.configure(state="disabled")
    
#Функція піднесення до степеня
def power():
    try:
        A = int(field_a.get())
        B = int(field_b.get())
        field_result.configure(state="normal")
        field_result.delete(0, "end")
        field_result.insert(0, str(A ** B))
        field_result.configure(state="disabled")
    except:
            field_result.configure(state="normal")
            field_result.delete(0, "end")
            field_result.insert(0, "Помилка вводу")
            field_result.configure(state="disabled")
    
#Функція знаходження корення n-го степеня
def root():
    if B==0:
        return "Invalid" #На 0 ділити не можна
    return A**(1/B)

#Функція знаходження логарифма A з основою B
def log():
    if A<=0 or B<=0 or B==1:
        return "invalid values"
    return math.log(A, B)

#Функція знаходження синуса A (в градусах)
def sin():
    return math.sin(math.radians(A))

#Функція знаходження косинуса A (в градусах)
def cos():
    return math.cos(math.radians(A))

#Функція знаходження тангенса A (в градусах)
def tan():
    radians=math.radians(A)
    c=math.cos(radians)
    if abs(c)<1e-10:
        return "Undefined"
    return math.tan(radians)
    
#Функція знаходження котангенса А (в градусах)
def ctg():
    t=math.tan(math.radians(A))
    if abs(t)<1e-10:
        return "Undefined"
    c=1/t
    if c<1e-10:
        return 0
    return 1/t

#Функція знаходження факторіала А
def factorial():
    try:
        n = int(field_a.get())
        if n < 0:
            result = "Only >0"
        else:
            result = math.factorial(n)
        field_result.configure(state="normal")
        field_result.delete(0, "end")
        field_result.insert(0, str(result))
        field_result.configure(state="disabled")
    except:
        field_result.configure(state="normal")
        field_result.delete(0, "end")
        field_result.insert(0, "Integer only")
        field_result.configure(state="disabled")

    
# Кнопки

# Кнопка +
button_plus = ctk.CTkButton(app, text="+",
                            width = 100,
                            height = 100,
                            command = plus,
                            fg_color = "#bb09f6",
                            text_color = "white",
                            hover_color = "#ff86f7",
                            corner_radius = 25,
                            font = ("Arial", 50, "bold"),
                            compound = "top")

button_plus.place(x = 50, y = 200)

# Кнопка - 
button_minus = ctk.CTkButton(app, text="-",
                            width = 100,
                            height = 100,
                            command = minus,
                            fg_color = "#bb09f6",
                            text_color = "white",
                            hover_color = "#ff86f7",
                            corner_radius = 25,
                            font = ("Arial", 50, "bold"),
                            compound = "top")

button_minus.place(x = 200, y = 200)

# Кнопка / 
button_divide = ctk.CTkButton(app, text="/",
                            width = 100,
                            height = 100,
                            command = divide,
                            fg_color = "#bb09f6",
                            text_color = "white",
                            hover_color = "#ff86f7",
                            corner_radius = 25,
                            font = ("Arial", 50, "bold"),
                            compound = "top")

button_divide.place(x = 350, y = 200)

# Кнопка * 
button_times = ctk.CTkButton(app, text="*",
                            width = 100,
                            height = 100,
                            command = times,
                            fg_color = "#bb09f6",
                            text_color = "white",
                            hover_color = "#ff86f7",
                            corner_radius = 25,
                            font = ("Arial", 50, "bold"),
                            compound = "top")

button_times.place(x = 50, y = 350)

# Кнопка ^
button_power = ctk.CTkButton(app, text="^",
                            width = 100,
                            height = 100,
                            command = power,
                            fg_color = "#bb09f6",
                            text_color = "white",
                            hover_color = "#ff86f7",
                            corner_radius = 25,
                            font = ("Arial", 50, "bold"),
                            compound = "top")

button_power.place(x = 200, y = 350)

# Кнопка !
button_factorial = ctk.CTkButton(app, text="!",
                            width = 100,
                            height = 100,
                            command = factorial,
                            fg_color = "#bb09f6",
                            text_color = "white",
                            hover_color = "#ff86f7",
                            corner_radius = 25,
                            font = ("Arial", 50, "bold"),
                            compound = "top")

button_factorial.place(x = 350, y = 350)

app.mainloop()

    
