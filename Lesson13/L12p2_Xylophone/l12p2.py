from tkinter import *
from winsound import *
from tkinter import messagebox as mb


def playDo():
    frequency = 261  # Set Frequency To 2500 Hertz
    duration = 500  # Set Duration To 1000 ms == 1 second
    Beep(frequency, duration)


def playRe():
    frequency = 293  # Set Frequency To 2500 Hertz
    duration = 500  # Set Duration To 1000 ms == 1 second
    Beep(frequency, duration)


def playMi():
    frequency = 329  # Set Frequency To 2500 Hertz
    duration = 500  # Set Duration To 1000 ms == 1 second
    Beep(frequency, duration)


def playFa():
    frequency = 349  # Set Frequency To 2500 Hertz
    duration = 500  # Set Duration To 1000 ms == 1 second
    Beep(frequency, duration)


def playSol():
    frequency = 392  # Set Frequency To 2500 Hertz
    duration = 500  # Set Duration To 1000 ms == 1 second
    Beep(frequency, duration)


def playLa():
    frequency = 440  # Set Frequency To 2500 Hertz
    duration = 500  # Set Duration To 1000 ms == 1 second
    Beep(frequency, duration)


def infoWindowEvent(event):
    windows = Toplevel(root)
    windows.title("Информация")
    windows.geometry("200x100")
    windows.resizable(0, 0)
    lbl_author = Label(windows, text="Автор: Kad", font="Calibri 20")
    lbl_author.pack(side=TOP)


root = Tk()
root.title("Норма веса")
root.geometry("650x400")
root.resizable(0, 0)


lblMain = Label(
    text="Добро пожаловать в 'Ксилофон'.\nНажимайте клавиши и играйте!", font="Calibri20")
lblMain.pack(side=TOP)

sheetDo = Button(text="ДО", height=15, width=12, bg='white', command=playDo)
sheetDo.pack(side=LEFT)
sheetRe = Button(text="РЕ", height=15, width=12, bg='yellow', command=playRe)
sheetRe.pack(side=LEFT)
sheetMi = Button(text="МИ", height=15, width=12, bg='blue', command=playMi)
sheetMi.pack(side=LEFT)
sheetFa = Button(text="ФА", height=15, width=12, bg='red', command=playFa)
sheetFa.pack(side=LEFT)
sheetSol = Button(text="СОЛЬ", height=15, width=12, bg='green', command=playSol)
sheetSol.pack(side=LEFT)
sheetLa = Button(text="Ля", height=15, width=12, bg='purple', command=playLa)
sheetLa.pack(side=LEFT)

btn_exit = Button(text="Выход", fg="red", command=exit)
btn_exit.pack(side=BOTTOM)

root.bind('<F1>', infoWindowEvent)

root.mainloop()
