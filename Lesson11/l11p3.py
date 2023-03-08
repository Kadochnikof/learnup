from tkinter import *
from tkinter import messagebox as mb
data = open('log.txt', 'r')
print(data.readlines())

def add_words():
    data = open('log.txt', 'a')
    row = str(entWords.get().strip())
    
    if row != "off" and row != "":
        data.write(str(row) + "\n")
        mb.showinfo("Добавление текста", "Текст: " + row + " успешно добавлен")
    
    elif row == "":
         mb.showinfo("Добавление текста", "Введите текст")     
    else: 
        mb.showinfo("Добавление текста", "Программа завершена")
        data.close()
        exit()
        
def clear_file():
    data = open('log.txt', 'w')
    mb.showinfo("Добавление текста", "Файл 'log.txt' очищен")
       
root = Tk()
root.geometry("400x400")
root.title("Добавление текста")
root.resizable(0, 0)

lblMain = Label(text = "Добавление текста", font = "Calibri 20")
lblMain.place(x = 20, y = 20)

lblEnter = Label(text = 'Введите фразу для добавления текста. \nДля выхода из программы введите "off"', font = "Calibri 12")
lblEnter.place(x = 20, y = 100)

entWords = Entry(width = 14, font = "Calibri 12")
entWords.place(x = 80, y = 160)

btnEnter = Button(text = "Добавить", font = "Calibri 16", command = add_words)
btnEnter.place(x = 20, y = 200)

btnEnter = Button(text = "Очистить файл полностью", font = "Calibri 16", command = clear_file)
btnEnter.place(x = 20, y = 260)



root.mainloop()