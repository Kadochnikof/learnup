from tkinter import *
import winsound


def play():
    winsound.PlaySound("sounds/tick.wav", winsound.SND_ASYNC)


root = Tk()
root.geometry("400x400")
root.title("LearnUP")
root.resizable(0, 0)

lbl_main = Label(text="LearnUp", font="Calibri 20")
lbl_main.place(x=20, y=20)

img_logo = PhotoImage(file="img/learnup.png")
lbl_logo = Label(image=img_logo)
lbl_logo.place(x=20, y=60)

btn_sound = Button(text="Play!", font="Calibri 20", command=play)
btn_sound.place(x=100, y=325)

root.mainloop()
