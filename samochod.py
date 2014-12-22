__author__ = 'Sylwia'

class Auto(object):
    def __init__(self, m, n, p):
        self.model = m
        self.numer_rejestracyjny = n
        self.przebieg = p

    def wyswietl(self):
        print "Model samochodu to: %s"% self.model
        print "Numer rejestracyjny to: %s"% self.numer_rejestracyjny
        print "Przebieg samochodu to w KM: %s"% self.przebieg
        print "Auto jest: %s" %self.nowe()
        print "-------------"

    def nowe(self):
        if self.przebieg <= 1000:
            return "Nowe niesmigane"
        elif self.przebieg >1000 and self.przebieg < 300000:
            return "Jeszcze pojezdzisz ale sprawdzaj"
        else:
            return "Za pare km zlom"

class Osobowe(Auto):

    def __init__(self, m, n, p, d=5, r =4, t="suw"):
        super(Osobowe, self).__init__(m, n, p)
        self.drzwi = d
        self.rozstaw_osi = r
        self.typ = t

    def wyswietl(self):
        print "Ilosc drzw : %s" %self.drzwi
        print "Rozstaw osi wynosi %s" % self.rozstaw_osi
        print "Typ : %s" % self.typ
        print "Wymiana oleju %s"% self.wymiana()

    def wymiana(self):
        if self.przebieg % 20000 == 0:
            return True
        else:
            return False

auto1 = Auto("Audi", "RZE 12345", 52800)
auto2 = Auto("Fiat", "EL542134", 0)
auto3 = Auto("Ford", "ZUSIA", 7878945231)

auto1.wyswietl()
auto2.wyswietl()
auto3.wyswietl()

SantaFe = Osobowe("SantaFe","jhsdfdsg", 4447562)
SantaFe.wyswietl()