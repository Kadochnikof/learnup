from tkinter import *
from tkinter import messagebox as mb


def checkWeight():
    try:
        userHeight = int(entHeight.get().strip())
        # userWeight = userHeight - 100
    except Exception:
        recomm['text'] = "Введите число!"
        recomm['fg'] = 'red'
        entHeight.delete(0, END)    
    else:
        entHeight.delete(0, END) 
        if r_var.get() == 0:
            userWeight = userHeight - 100
            if userWeight >= 20 and userWeight < 141:
                recomm['text'] = "При росте " + str(userHeight) + " см." + "\nРекомендуемый вес для мужчины: " + str(userWeight) + " кг."
                recomm['fg'] = 'black'
            else:
                recomm['text'] = "Некорректный вес! Введите число от 120 до 240"
        else:
            # r_var.get() == 1:        
            userWeight = userHeight - 110
            if userWeight >= 20 and userWeight < 141:
                recomm['text'] = "При росте " + str(userHeight) + " см." + "\nРекомендуемый вес для женщины: " + str(userWeight) + " кг."
                recomm['fg'] = 'black'
            else:
                recomm['text'] = "Некорректный вес! Введите число от 130 до 240"                
        
        
        
def chkWeightEvent(event):
    checkWeight()   



root = Tk()
root.title("Норма веса")
root.geometry("600x400")
root.resizable(0, 0)


lblMain = Label(text="Добро пожаловать в 'Норму веса'.\nПриложение рассчитывает норму веса пользователя, \nв зависимости от его роста и пола", font="Calibri20")
lblMain.pack(side=TOP)

lblSex = Label(text="Выберите Ваш пол:", font="Calibri 14")
lblSex.pack(side=TOP)

r_var = BooleanVar()
r_var.set(0)

btnMen = Radiobutton(text='Мужской', variable=r_var, value=0)
btnMen.pack(side=TOP)
btnWomen = Radiobutton(text='Женский', variable=r_var, value=1)
btnWomen.pack(side=TOP)

lblRules = Label(text="Введите Ваш рост для определения рекомендуемого веса:", font="Calibri 14")
lblRules.pack(side=TOP)

lblHeight = Label(text="Рост, см:")
lblHeight.pack(side=TOP)

entHeight = Entry(width = 14, font = "Calibri 12")
entHeight.pack(side=TOP)

chkWeight = Button(text = "Проверить", command = checkWeight)
chkWeight.pack(side=TOP)

btn_exit = Button(text = "Выход", fg="red", command = exit)
btn_exit.pack(side=BOTTOM)

recomm = Label(text="", font="Calibri 14")
recomm.pack(side=TOP)


root.bind('<Return>', chkWeightEvent)

root.mainloop()