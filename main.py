import datetime
import random
class Osoba:
    def __init__(self, meno, priezvisko, rok):
        self.meno = meno
        self.priezvisko = priezvisko
        self.rok = rok
        self.vek = datetime.date.today().year - self.rok
    #konštruktor
    def pozdrav(self):
        print("Zdravím, ja som", self.meno, self.priezvisko, "a mám", self.vek, "rokov.")
    #metoda pozdrav
    def vypis_vek(self):
        print(self.vek)

class Ucitel(Osoba):
    def __init__(self, meno, priezvisko, rok, titul, predmet, trieda):
        Osoba.__init__(self, meno, priezvisko, rok)
        self.titul = titul
        self.predmet = predmet
        self.trieda = trieda
    def pozdrav(self):
        print("Dobrý deň, som učiteľ", self.titul, self.meno, self.priezvisko, "a mám", self.vek, "rokov a učím predmet", self.predmet, "v triede", self.trieda)

class Student(Osoba):
    def __init__(self, meno, priezvisko, rok, trieda):
        Osoba.__init__(self, meno, priezvisko, rok)
        self.trieda = trieda
    def pozdrav(self):
        print("Ahoj, som", self.meno, self.priezvisko, "a mám", self.vek, "rokov a som žiakom", self.trieda, "triedy.")

#adam = Osoba("Adam", "Horalka", 2007)
#adam.pozdrav()
#matej = Ucitel("Matej", "Češčo", 2006, "Ing.", "PROGRAMKO")
#matej.pozdrav()
#peto = Student("Peter", "Tatarka", 2005, "3.AG")
#peto.pozdrav()

pocet_studentov = 4
pocet_ucitelov = 3

studenti = list()
ucitelia = list()

for i in range(pocet_studentov):
    with open("mena.txt", "r", encoding="utf-8") as t:
        mena = tuple(t)
    meno = random.choice(mena)
    meno = meno[:-1]

    with open("priezviska.txt", "r", encoding="utf-8") as p:
        priezviska = tuple(p)
    priezvisko = random.choice(priezviska)
    priezvisko = priezvisko[:-1]

    rok = random.randint(2005, 2008)

    if rok == 2005:
        trieda = "IV."
    elif rok == 2006:
        trieda = "III."
    elif rok == 2007:
        trieda = "II."
    else:
        trieda = "I."

    trieda = trieda + random.choice(("A", "B", "C"))

    studenti.append(Student(meno, priezvisko, rok, trieda))
print("Študenti: ")
for i in range(pocet_studentov):
    print(i, studenti[i].meno, studenti[i].priezvisko, studenti[i].vek, studenti[i].rok, studenti[i].trieda)
print("\n")
studenti[1].pozdrav()
print("========================\n")
print("Učitelia: ")
for i in range(pocet_ucitelov):
    with open("mena.txt", "r", encoding="utf-8") as t:
        mena = tuple(t)
    meno = random.choice(mena)
    meno = meno[:-1]

    with open("priezviska.txt", "r", encoding="utf-8") as p:
        priezviska = tuple(p)
    priezvisko = random.choice(priezviska)
    priezvisko = priezvisko[:-1]

    rok = random.randint(1960, 2004)

    titul = random.choice(("Ing.", "Mgr.", "Bc."))
    predmet = random.choice(("Anj", "Mat", "Prx"))
    trieda =  random.choice(("I.", "II.", "III.", "IV."))
    trieda = trieda + random.choice(("A", "B", "C"))

    ucitelia.append(Ucitel(meno, priezvisko, rok, titul, predmet, trieda))
for i in range(pocet_ucitelov):
    print(i, ucitelia[i].meno, ucitelia[i].priezvisko, ucitelia[i].vek, ucitelia[i].rok, ucitelia[i].titul,ucitelia[i].predmet, ucitelia[i].trieda)
print("\n")
ucitelia[1].pozdrav()