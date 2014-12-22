__author__ = 'Sylwia'

class Budynek():
    def __init__(self, a='', w='Jan Kowalski'):
        print "Uruchomilem funkcje INIT"
        self.adres = a
        self.wlasciciel = w
        self.powierzchnia = 0

    def wyswielt(self):
        '''
        wyswietl - wyswietala dane klasy budynek
        :param: None
        :return:  None
        '''
        print "Wlasciel budynku to: %s" % self.wlasciciel
        print "Adres budynku to: %s" % self.adres

    def koszt(self, cena):
        return cena * self.powierzchnia

    def ustaw_powierzchnie(self, pow):
        self.powierzchnia = pow

budynek1 = Budynek("Waclawa 53/77")
budynek2 = Budynek("Nowy Borek 156", "Sylwia Kos")
budynek3 = Budynek()

budynek2.ustaw_powierzchnie(160)
budynek1.ustaw_powierzchnie(65)

print budynek2.powierzchnia
print budynek1.powierzchnia

print budynek2.koszt(3500.00)

# #print budynek1.__adres
# print budynek1.adres
# print budynek1.wlasciciel
# print budynek2.wlasciciel
# print budynek2.adres
# print budynek3.adres
# print budynek3.wlasciciel

budynek1.wyswielt()
budynek2.wyswielt()
budynek3.wyswielt()