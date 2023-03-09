from tkinter import *
from random import *

root = Tk()
root.title("Игральная кость")
root.geometry("400x300")
root.resizable(0, 0)

def setCube():
    try:
        user_num = int(ent_num.get().strip())
    except Exception:
        lbl_message['text'] = "Введите число!"
        lbl_message['fg'] = 'red'
        ent_num.delete(0, END)
    else:
        ent_num.delete(0, END)
        btn_go['text'] = "Ещё раз!"
        rand_num = randint(1, 6)
        path = "Lesson12/images/" + "Pic" + str(rand_num) + ".png"
        img['file'] = path

        if user_num == rand_num:
            lbl_message['text'] = "отлично!"
            lbl_message['fg'] = 'green'
        else:
            lbl_message['text'] = "Попробуй ещё раз!"
            lbl_message['fg'] = 'purple'
    
 
def setCubeEvent(event):
    setCube()   

def infoWindowEvent(event):
    windows = Toplevel(root)
    windows.title("Информация")
    windows.geometry("200x100")
    windows.resizable(0, 0)
    lbl_author = Label(windows, text= "Автор: Kad", font="Calibri 20")
    lbl_author.pack(side=TOP)
    
        
def exit():
    root.destroy()
    
    
lbl_main = Label(text = "Игральная кость", font = "Calibri 20", justify = CENTER)
lbl_rules = Label(text = "Бросайте кости и угадывайте выпавшее число", font = "Calibri 14", justify = CENTER)

"""grid - размещает объекты по сетке"""
# lbl_rules.grid(row = 1, column = 0, columnspan = 2)
# lbl_main.grid(row = 0, column = 0, columnspan = 2)

"""place - по координатам"""
# lbl_rules.place(x = 20,y = 70)

"""pack - по стороне"""
lbl_main.pack(side = TOP)
lbl_rules.pack(side = TOP)

img = PhotoImage(file="Lesson12/images/Pic1.png")
lbl_img = Label(image=img)
lbl_img.pack(side=TOP)

lbl_message = Label(text = "Введите предполагаемое число", font = "Calibri 14")
lbl_message.pack(side=TOP)

ent_num = Entry(width = 3, font = "Calibri 20")
ent_num.pack(side=TOP)

btn_go = Button(text = "Играть!", command = setCube)
btn_go.pack(side=TOP)

root.bind('<Return>', setCubeEvent)
root.bind('<Tab>', infoWindowEvent)


btn_exit = Button(text = "Выход", command = exit)
btn_exit.pack(side=TOP)







root.mainloop()