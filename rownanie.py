__author__ = 'skos'

if __name__ == "__main__":
    pass

    try:
        x = float(raw_input("Podaj x \n"))
        if x != 0.5:
            y = (2 * x ** 2 + 3 * x + 1 )/((x - 1) * (2 * x + 3))
        else:
            print "Nie mozna wyznaczyc wartosci rownania dla x rownego 0.5"
        print "Wynik rownania to %s" % str(y)



    except ValueError as e1:
        print e1.message
        print "Zla liczba. podaj inna liczbe"
    except NameError as e2:
        print e2.message + " Zmienna y nie powstala"
    finally:
        print "Wykonalo sie "
