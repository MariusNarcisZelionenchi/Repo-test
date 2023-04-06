"""
PARTEA 1 - FUNCTII

Exerciții - studiu în workshopul de weekend

Pentru toate exercițiile: Apelați funcția de cel puțin 2 ori cu valori diferite pentru a testa.
Dacă funcția are return, printează răspunsul.
"""

"""
1. Funcție care să calculeze și să returneze suma a două numere.
"""
# x = int(input('introdu un numar: '))
# y = int(input('Introdu un alt numar: '))
# def suma(a, b):
#     return a + b
# k = suma(x, y)
# print(k)
"""
2. Funcție care să returneze TRUE dacă un număr este par, FALSE pentru impar.
"""
# nr = int(input('Introdu un numar: '))
# def paritate(nr):
#     if nr % 2 == 0:
#         print(f'Numarul {nr} este un numar par')
#     else:
#         print(f'Numarul {nr} este un numar impar')
# paritate(nr)

# def par_sau_impar(nr):
#     if nr % 2 == 0:
#         return True
#     else:
#         return False
#
# print(par_sau_impar(21))

"""
3. Funcție care returnează numărul total de caractere din numele tău complet.
(nume, prenume, nume_mijlociu)
"""
# def contorizor(prenume, nume, p_mij = ''):
#     tot_nume = prenume + p_mij + nume
#     print(tot_nume)
#     return len(tot_nume)
# print(contorizor(prenume = 'Marius', p_mij = 'Narcis', nume ='Zelionenchi'))
# print(contorizor(prenume = 'Bianca', nume = 'Nume'))
"""
4. Funcție care returnează aria dreptunghiului.
"""
# def aria_dreptunghi (lungime, latime):
#     arie = lungime * latime
#     return arie
#
# print(aria_dreptunghi(5, 9))
"""
5. Funcție care returnează aria cercului.
"""
# def aria_cerc(r): #r=raza cercului
#     import math #importam libraria math de unde luam vaoarea lui Pi
#     aria = (r ** 2) * math.pi
#     return aria
# print(aria_cerc(2))

"""
6. Funcție care returnează True dacă un caracter x se găsește într-un string dat și False dacă nu găsește.
"""
# def find_char(string, char):
#     if char in string:
#         return True
#     return False
#
# # Exemplu
# string = "Hello, Pythonistas!"
# char = "q"
#
# result = find_char(string, char)
# print(result)
"""
7. Funcție fără return, primește un string și printează pe ecran:
Numărul de caractere lower case este x.
Numărul de caractere upper case exte y.
"""
# def count_case(string):
#     lowercase_count = 0
#     uppercase_count = 0
#
#     for char in string:
#         if char.islower():
#             lowercase_count += 1
#         elif char.isupper():
#             uppercase_count += 1
#
#     print(f"Lowercase characters: {lowercase_count}")
#     print(f"Uppercase characters: {uppercase_count}")
#
# # Exemplu
# input_string = "AlaBaLa PortoCalA"
# print(len(input_string))
# count_case(input_string)
"""
8. Funcție care primește o LISTĂ de numere și returnează o LISTĂ doar cu numerele pozitive.
"""
# lista1=[-3,4,-6,13,8,-20,-17,29,20]
# lista2=[]
# def nr_pozitive(lista):
#     for nr in lista:
#         if nr > 0:
#             print(nr)
#             lista2.append(nr)
#     return lista2
#
#
# nr_pozitive(lista1)
# print(lista2)
"""
9. Funcție care nu returneaza nimic. Primește două numere și PRINTEAZĂ:
Primul număr x este mai mare decat al doilea număr y.
Al doilea număr y este mai mare decat primul număr x.
Numerele sunt egale.
"""
# def comparatie(x, y):
#     if x > y:
#         print(f'Primul număr {x} este mai mare decat al doilea număr {y}')
#     elif x < y:
#         print(f'Al doilea număr {y} este mai mare decat primul număr {x}')
#     else:
#         print('Numerele sunt egale')
# comparatie(5, 6)
"""
10. Funcție care primește un număr și un set de numere.
Printează ‘am adaugat numărul nou în set’ + returnează True
Printează ‘nu am adaugat numărul în set. Acesta există deja’ + returnează False
"""
# def add_nr_to_set(nr, set):
#     print(f'{nr}, // {set}')
#     set.add(nr)
#     print(set)
#     if nr in set:
#         print('Nu am adaugat numărul în set. Acesta există deja!')
#         return False
#     else:
#         print('Am adaugat numărul nou în set.')
#         return True
# print(add_nr_to_set(1,{1,3,4}))
# print(add_nr_to_set(1,{2,3,4}))

#varianta mai eleganta:
# def add_number_to_set(numar, set_numere):
#     if numar in set_numere:
#         print("Nu am adaugat numarul in set.Acesta exista deja")
#         return False
#     set_numere.add(numar)
#     print("am adaugat numărul nou în set")
#     return True
#
# print(add_number_to_set(1, {2,3,4}))
# print(add_number_to_set(1, {1,2,3,4}))
"""
11. Funcție care primește o lună din an și returnează câte zile are acea lună.
"""
# def luna_an(luna):
#     luni = {'ianuarie': 31, 'februarie': 28, 'martie': 31, 'aprilie': 30, 'mai': 31, 'iunie': 30, 'iulie': 31,
#             'august': 31, 'septembrie': 30, 'octombrie': 31, 'noiembrie': 30, 'decembrie': 31} #dictionarul trebuie sa
#     # fie in functie asa cand importam functia, importam si dictionarul
#     for key, value in luni.items():
#         if luna == key:
#             print(value)
#             return value
#
# luna_an('iunie')


# #solutie itfactory:
# def count_days(month):
#     if month in (1, 3, 5, 7, 8, 10, 12):
#         return 31
#     elif month in (4, 6, 9, 11):
#         return 30
#     elif month == 2:
#         return 28  # 29 daca este an bisect
#     return 0
#
#
# print(count_days(1))
# print(count_days(4))
# print(count_days(2))
#
# def count_days2(month):
#     if month in ('ianuarie', 'martie', 'mai', 'iulie', 'august', 'octombrie', 'decembrie'):
#         return 31
#     elif month in ('aprilie','iunie', 'septembrie', 'noiembrie'):
#         return 30
#     elif month == 'februarie':
#         return 28  # 29 daca este an bisect
#     return 0
#
# print(count_days2('ianuarie'))
# print(count_days2('iunie'))


# #solutie cu import calendar
# from calendar import monthrange
#
# def luna_anului(luna):
#     rezultat = monthrange(2023, luna)
#     print(rezultat)
#     return rezultat[1]
#
# print(luna_anului(3))
"""
12. Funcție calculator care să returneze 4 valori. Suma, diferența, înmulțirea, împărțirea a două numere.

În final vei putea face:
a, b, c, d = calculator(10, 2)
print("Suma: ", a)
print("Diferenta: ", b)
print("Inmultirea: ", c)
print("Impartirea: ", d)
"""

"""
13. Funcție care primește o listă de cifre (adică doar 0-9).
Exemplu: [1, 3, 1, 5, 9, 7, 7, 5, 5]
Returnează un DICT care ne spune de câte ori apare fiecare cifră
=> dict {
0: 0
1 :2
2: 0
3: 1
4: 0
5: 3
6: 0
7: 2
8: 0
9: 1
}
"""

"""
14. Funcție care primește 3 numere. Returnează valoarea maximă dintre ele.
"""

"""
15. Funcție care să primească un număr și să returneze suma tuturor numerelor de la 0 la acel număr.
Exemplu: dacă dăm numărul 3, suma va fi 6 (0+1+2+3)
"""

"""
16.Funcție care primește 2 liste de numere (numerele pot fi dublate). Returnați numerele comune.

Exemplu:
list1 = [1, 1, 2, 3]
list2 = [2, 2, 3, 4]
Răspuns: {2, 3}
"""

"""
17. Funcție care să aplice o reducere de preț.
Dacă produsul costă 100 lei și aplicăm reducere de 10%. Pretul va fi 90 de lei.
Tratează cazurile în care reducerea e invalidă. De exemplu o reducere de 110% e invalidă.
"""

"""
18.Funcție care să afișeze data și ora curentă din România.
(bonus: afișează și data și ora curentă din China)
"""

"""
19. Funcție care să afișeze câte zile mai sunt până la ziua ta / sau până la Crăciun dacă nu vrei să ne zici cand e ziua ta :)
"""
