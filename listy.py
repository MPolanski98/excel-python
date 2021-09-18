# lista = ['jebac', 'konfidentow', 'kurwy', 'policje']
# lista2 = [1, 50, 2321, 87]

# if 'jebac' in lista:
#     print('iks de')

# if 2321 in lista2:
#     print('halo')

# lista = []
# lista.append(7)
# print(lista)

# wartości: 300 51

# zapisz te 2 wartości w zmiennych, nastepnie wyslij do funkcji, ktora zwroci w liscie ich iloraz, iloczyn, sume i roznice, nastepnie wyswietl
# Nastepnie sprawdz czy w tej liscie znajduje sie 249, jesli tak wyswietl "Mafia Gang kurwy"

zmienna, zmienna_1 = 300, 51

def mafia(a, b):
    iloraz = a/b
    iloczyn = a*b
    suma = a+b
    roznica = a-b
    return [iloraz, iloczyn, suma, roznica]

lista = mafia(zmienna, zmienna_1)

print(lista)

if 249 in lista:
    print("Mafia gang kurwy")
