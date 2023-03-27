from tkinter import *
from tkinter import messagebox as mb
from math import *
import os


try:
    data = open('result.txt', 'r')
except IOError:
    data = open('result.txt', 'w')


name = ""
result1 = int()
result2 = int()


def clear_file():
    data = open('result.txt', 'w')
    mb.showinfo("Геометрические фигуры", "Файл 'result.txt' очищен")


def rectangleForm():
    """Поля для прямоугольника"""
    aLbl.pack(anchor=W)
    aEnt.pack(anchor=W)
    aLbl['text'] = "Введите длину стороны А, см: "
    bLbl.pack(anchor=W)
    bEnt.pack(anchor=W)
    cEnt.pack_forget()
    cLbl.pack_forget()


def circusForm():
    """Поля для круга"""
    aLbl.pack(anchor=W)
    aEnt.pack(anchor=W)
    aLbl['text'] = "Введите радиус R круга, см: "
    bEnt.pack_forget()
    bLbl.pack_forget()
    cEnt.pack_forget()
    cLbl.pack_forget()


def triangleForm():
    """Поля для треугольника"""
    aLbl.pack(anchor=W)
    aEnt.pack(anchor=W)
    aLbl['text'] = "Введите длину стороны А, см: "
    bLbl.pack(anchor=W)
    bEnt.pack(anchor=W)
    cLbl.pack(anchor=W)
    cEnt.pack(anchor=W)


def trSquare(a, b, c):
    """Расчет площади треугольника"""
    p = (a + b + c) / 2
    result1 = sqrt(abs(p * (p - a) * (p - b) * (p - c)))
    result2 = lambda a, b, c: a+b+c
    result2 = result2(a, b, c)
    name = "Треугольника"
    resultPrint(name, result1, result2)


def recSquare(a, b):
    """Расчет площади прямоугольника"""
    result1 = a*b
    result2 = lambda a, b: (a+b)*2
    result2 = result2(a, b)
    name = "Прямоугольника"
    resultPrint(name, result1, result2)


def cirSquare(a):
    """Расчет площади круга"""
    result1 = pi*(a**2)
    result2 = lambda a: 2*pi*a
    result2 = result2(a)
    name = "Круга"
    resultPrint(name, result1, result2)


def calculate():
    """Расчет формул"""
    try:
        data = open('result.txt', 'a')
        if r_var.get() == 0:
            a = int(aEnt.get().strip())
            b = int(bEnt.get().strip())
            c = int(cEnt.get().strip())
        elif r_var.get() == 1:
            a = int(aEnt.get().strip())
        elif r_var.get() == 2:
            a = int(aEnt.get().strip())
            b = int(bEnt.get().strip())
    except Exception:
        squareLbl['text'] = "Введите число!"
        squareLbl['fg'] = 'red'
        aEnt.delete(0, END)
        bEnt.delete(0, END)
        cEnt.delete(0, END)
    else:
        print(r_var.get())
        if r_var.get() == 0 and a > 0 and b > 0 and c > 0:
            trSquare(a, b, c)
        elif r_var.get() == 1 and a > 0:
            cirSquare(a)
        elif r_var.get() == 2 and a > 0 and b > 0:
            recSquare(a, b)
        else:
            squareLbl['text'] = "Число не может быть отрицательным!"
            squareLbl['fg'] = 'red'
            aEnt.delete(0, END)
            bEnt.delete(0, END)
            cEnt.delete(0, END)
        data.close()
        
        
def resultPrint(name, result1, result2):
    """Печать результата"""
    squareLbl['text'] = f"Площадь {name} равна: {round(result1, 2)} см2\n"
    squareLbl['fg'] = 'purple'
    perLbl['text'] = f"Периметр {name} равен: {round(result2, 2)} см\n"
    perLbl['fg'] = 'green'
    data = open('result.txt', 'a')
    data.write(squareLbl['text'])
    data.write(perLbl['text'])
    aEnt.delete(0, END)
    bEnt.delete(0, END)
    cEnt.delete(0, END)
    os.startfile('result.txt')


root = Tk()
root.geometry("600x600")
root.title("Расчет площади и периметра геометрическо фигуры")
root.resizable(0, 0)

lblMain = Label(
    text="Расчет площади и периметра \nгеометрической фигуры", font="Calibri 20")
lblMain.pack(side=TOP)

lblEnter = Label(text="Выберите фигуру: ", font="Calibri 12")
lblEnter.pack(anchor=W)

r_var = IntVar()
r_var.set(0)

figureRbtnRectangle = Radiobutton(
    text='Прямоугольник', variable=r_var, value=2, command=rectangleForm)
figureRbtnRectangle.pack(anchor=W)
figureRbtnCircus = Radiobutton(
    text='Круг', variable=r_var, value=1, command=circusForm)
figureRbtnCircus.pack(anchor=W)
figureRbtnTriangle = Radiobutton(
    text='Треугольник', variable=r_var, value=0, command=triangleForm)
figureRbtnTriangle.pack(anchor=W)

aLbl = Label(text="Введите длину стороны A, см: ")
aLbl.pack(anchor=W)
aEnt = Entry(width=14, font="Calibri 12")
aEnt.pack(anchor=W)
bLbl = Label(text="Введите длину стороны B, см: ")
bLbl.pack(anchor=W)
bEnt = Entry(width=14, font="Calibri 12")
bEnt.pack(anchor=W)
cLbl = Label(text="Введите длину стороны C, см: ")
cLbl.pack(anchor=W)
cEnt = Entry(width=14, font="Calibri 12")
cEnt.pack(anchor=W)

answerBtn = Button(text="Рассчитать", font="Calibri 12", command=calculate)
answerBtn.place(x=250, y=350)

squareLbl = Label(
    text=f"Площадь {name} равна: {result1} см2", font="Calibri 14")
squareLbl.place(x=250, y=400)

perLbl = Label(
    text=f"Периметр {name} равен: {result2} см2", font="Calibri 14")
perLbl.place(x=250, y=450)

btnExit = Button(text="Выход", fg="red", command=exit)
btnExit.pack(side=BOTTOM)

btnClearFile = Button(text="Очистить файл полностью",
                      font="Calibri 12", command=clear_file)
btnClearFile.pack(side=BOTTOM)


root.mainloop()
