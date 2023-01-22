def funkcja(imie, nazwisko, wiek):
    print('yo', imie)
    if wiek >=18:
        print('szanowny',nazwisko)

x = input('podaj imie nazwisko wiek').split()

funkcja(x[0], x[1], int(x[2]))
