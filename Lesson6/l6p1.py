class Prof():
    def __init__(self, year = 0, proff = "") -> None:
        self.year = year
        self.proff = proff 
    def get_info(self):
        print("Профессия: ", self.proff)
        print("Возраст: ", self.year)

class med_rab(Prof):
    def __init__(self, year = 31, proff = "Медработник") -> None:
        super(med_rab, self).__init__(year, proff)

    def get_info(self):
        super(med_rab, self).get_info()

class med_sis(Prof):
    def __init__(self, year = 45, proff = "Медсестра") -> None:
        super(med_sis, self).__init__(year, proff)

    def get_info(self):
        super(med_sis, self).get_info()

class hirirg(Prof):
    def __init__(self, year = 56, proff = "Хирург") -> None:
        super(hirirg, self).__init__(year, proff)

    def get_info(self):
        super(hirirg, self).get_info()
      

medrab = med_rab()
medrab.get_info()
medsis = med_sis()
medsis.get_info()
hirurg = hirirg()
hirurg.get_info()

