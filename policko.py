cisla = [6, 18, 17, 4, 5, 1]
hledane_cislo = int(input("Zadej číslo, které chceš najít: "))
nasel = False 
for i in range(len(cisla)):
    if cisla[i] == hledane_cislo:
        print("Našel jsem tuto hodnotu na pozici", i+1, "!")
        nasel = True
        break 
if not nasel:
    print("Zadaná hodnota tady není.")