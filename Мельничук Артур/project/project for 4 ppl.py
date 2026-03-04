#Імпорт візуальної частини
from tkinter as tk
from random as rn

#Імпорт модуля для математики
import math

#Два поля введення чисел
A =int(input(" " : ))
B =int(input(" " :  ))

#Функція котра робить додаваня
def plus():
    return A + B

#Функція котра робить відніманя
def minus():
    return A - B

#Функція котра робить діленя
def divide():
    return A / B

#Функція котра робить множення
def times():
    return A * B
    
#Функція піднесення до степеня
def power():
    return A**B
    
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
        n=int(A)
        if n<0:
            return "Only >0"
        return math.factorial(n)
    except:
        return "Integer only"



    
