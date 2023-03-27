Норма веса
==========================================
Приложение рассчитывает рекомендуемую норму веса пользователя, в зависимости от его роста и пола


Проверка веса осуществляется через **Button**

.. code::

    chkWeight = Button(text="Проверить", command=checkWeight)
    chkWeight.pack(side=TOP)


Поле для введение пользователем его роста реализовано через **Entry**

.. code::

    entHeight = Entry(width=14, font="Calibri 12")
    entHeight.pack(side=TOP)


.. function:: checkWeight()

Принимает вводимое пользователем значение и обрабатывает его для выведения результата

.. code::

    try:
        userHeight = int(entHeight.get().strip())
    else:
        entHeight.delete(0, END)
        if r_var.get() == 0:
            userWeight = userHeight - 100
            if userWeight >= 20 and userWeight < 141:
                recomm['text'] = "При росте " + str(
                    userHeight) + " см." + "\nРекомендуемый вес для мужчины: " + str(userWeight) + " кг."
                recomm['fg'] = 'black'
            else:
                recomm['text'] = "Некорректный вес! Введите число от 120 до 240"
        else:
            userWeight = userHeight - 110
            if userWeight >= 20 and userWeight < 141:
                recomm['text'] = "При росте " + str(
                    userHeight) + " см." + "\nРекомендуемый вес для женщины: " + str(userWeight) + " кг."
                recomm['fg'] = 'black'
            else:
                recomm['text'] = "Некорректный вес! Введите число от 130 до 240"


Во избежание ввода пользователем некорректных символов, реализовано исключение **Except**

.. code::

    except Exception:
        recomm['text'] = "Введите число!"
        recomm['fg'] = 'red'
        entHeight.delete(0, END)


Возможность выбора пола осуществляется через **Radiobutton**

.. code::

    btnMen = Radiobutton(text='Мужской', variable=r_var, value=0)
    btnMen.pack(side=TOP)
    btnWomen = Radiobutton(text='Женский', variable=r_var, value=1)
    btnWomen.pack(side=TOP)

По умолчанию установлен пол "Мужской"

.. code::

    r_var = BooleanVar()
    r_var.set(0)


.. function:: chkWeightEvent(event)

Функция позволяет запускать расчет программы по нажатию клавишы **ENTER**

.. code::

    root.bind('<Return>', chkWeightEvent)





