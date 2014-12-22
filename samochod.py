__author__ = 'Sylwia'

class Auto():
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


auto1 = Auto("Audi", "RZE 12345", 52800)
auto2 = Auto("Fiat", "EL542134", 0)
auto3 = Auto("Ford", "ZUSIA", 7878945231)

auto1.wyswietl()
auto2.wyswietl()
auto3.wyswietl()