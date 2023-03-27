Ксилофон
==========================================
Приложение Ксилофон с воиспроизведением 6 различных нот


Воспроизведение звука осуществляется через **Button**

.. code::

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


.. function:: playDo()

Воиспроизводит ноту с частотой ноты ДО первой октавы.

.. code::

    frequency = 261
    duration = 500
    Beep(frequency, duration)


.. function:: playRe()

Воиспроизводит ноту с частотой ноты ДО первой октавы.

.. code::

    frequency = 293
    duration = 500
    Beep(frequency, duration)


.. function:: playMi()

Воиспроизводит ноту с частотой ноты ДО первой октавы.

.. code::

    frequency = 329
    duration = 500
    Beep(frequency, duration)

.. function:: playFa()

Воиспроизводит ноту с частотой ноты ДО первой октавы.

.. code::

    frequency = 349
    duration = 500
    Beep(frequency, duration)


.. function:: playSol()

Воиспроизводит ноту с частотой ноты ДО первой октавы.

.. code::

    frequency = 392
    duration = 500
    Beep(frequency, duration)


.. function:: playLa()

Воиспроизводит ноту с частотой ноты ДО первой октавы.

.. code::

    frequency = 440
    duration = 500
    Beep(frequency, duration)



Воспроизведение производится с помощью встроенной функции **Beep**

.. code::

    Beep(frequency, duration)


.. function:: infoWindowEvent()

Реализовано выведение информационного поля по нажатию клавишы на клавиатуре **F1** с именем автора программы

.. code::

    windows = Toplevel(root)
    windows.title("Информация")
    windows.geometry("200x100")
    windows.resizable(0, 0)
    lbl_author = Label(windows, text="Автор: Kad", font="Calibri 20")
    lbl_author.pack(side=TOP)



