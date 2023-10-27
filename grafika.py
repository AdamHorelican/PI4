import tkinter

canvas = tkinter.Canvas()


class Tvar:
    def __init__(self, x, y, dlzka, farba="white"):
        self.x = x
        self.y = y
        self.dlzka = dlzka
        self._farba = farba
    def __str__(self):
        return "Ja som Tvar, x: " + str(self.x) + " y: " + str(self.y) + " dlzka: " + str(self.dlzka) + " farba: " + str(self._farba)


class Stvorec(Tvar):



    def vypis_sa(self):
        canvas.create_rectangle(self.x, self.y, self.x + self.dlzka, self.y + self.dlzka, fill=self._farba)


canvas.pack()

tvar = Tvar(10, 10, 100)
print(tvar)

stvorec = Stvorec(10,10,100)
stvorec.vypis_sa()
canvas.mainloop()





