from tkinter import *
from random import *
from PIL import Image, ImageTk

root = Tk()
root.title("Галерея")
root.geometry("600x500")
root.resizable(1, 1)
num = 1

def prevPic():
    global num
    try:
        num -= 1
        path = "Lesson12/images/" + str(num) + ".png"
        img['file'] = path
    except Exception:
        num = 5
        path = "Lesson12/images/" + str(num) + ".png"
        img['file'] = path

def nextPic():
    global num
    try:
        num += 1
        path = "Lesson12/images/" + str(num) + ".png"
        img['file'] = path
    except Exception:
        num = 1
        path = "Lesson12/images/" + str(num) + ".png"
        img['file'] = path
            
        
def exit():
    root.destroy()
        
lbl_main = Label(text = "Приложение 'Галерея'", font = "Calibri 20", justify = CENTER)
lbl_rules = Label(text = "Нажимайте стрелки вправо и влево для переключения фотографий", font = "Calibri 14", justify = CENTER)

lbl_main.pack(side = TOP)
lbl_rules.pack(side = TOP)


img = PhotoImage(file="Lesson12/images/1.png")
lbl_img = Label(image=img)
lbl_img.pack(side=TOP)

btnRight = Button(text = " Вправо ", command = nextPic)
btnRight.pack(side=RIGHT, padx=20)
btnLeft = Button(text = " Влево ", command = prevPic)
btnLeft.pack(side=RIGHT, padx=20)


btn_exit = Button(text = " Выход ", command = exit)
btn_exit.pack(side=BOTTOM)







root.mainloop()