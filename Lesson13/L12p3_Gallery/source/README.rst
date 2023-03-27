Галерея
==========================================
Галерея фото с возможностью переключения изображений

В коде введена глобальная переменная определяющая номер текущего 
отображаемого изображения. Значение по умолчанию **1**

.. code::

    num = 1

Переключение изображения осуществляется через **Button**

.. code::

btnRight = Button(text=" Вправо ", command=nextPic)
btnRight.pack(side=RIGHT, padx=20)

btnLeft = Button(text=" Влево ", command=prevPic)
btnLeft.pack(side=RIGHT, padx=20)


Изображение реализовано через **Label** со свойством *image*

.. code::

img = PhotoImage(file="images/1.png")
lbl_img = Label(image=img)
lbl_img.pack(side=TOP)



.. function:: prevPic()

Выводит на экран предыдущее изображение и работает с **global num**

Реализована проверка на наличие предыдущего изображения

.. code::

    try:
        num += 1
        path = "images/" + str(num) + ".png"
        img['file'] = path

В случае отсутствия предыдщуего изображения глобальная возникает ошибка и переменная **num** изменяется на 5.

    except Exception:
        num = 5
        path = "images/" + str(num) + ".png"
        img['file'] = path


.. code::


.. function:: nextPic()

Выводит на экран следующее изображение и работает с **global num**

Реализована проверка на наличие следующего изображения

.. code::

    try:
        num += 1
        path = "images/" + str(num) + ".png"
        img['file'] = path

В случае отсутствия следующего изображения глобальная возникает ошибка и переменная **num** изменяется на 1.

.. code::

    except Exception:
        num = 1
        path = "images/" + str(num) + ".png"
        img['file'] = path


Смена изображения происходит заменой значения в свойстве *img*

.. code::

        path = "images/" + str(num) + ".png"
        img['file'] = path






