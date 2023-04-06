# # 1. În cadrul unui comentariu, explică cu cuvintele tale ce este o variabilă.
#
# #R: o variabila este o 'cutie' cu valori
#
# # 2. Declară și initializează câte o variabilă din fiecare din următoarele tipuri de variabilă:
#
# nume='Marius'
# varsta=44
# inaltime=1.78
# conditie=False
#
# # 3. Utilizează funcția type pentru a verifica dacă au tipul de date așteptat.
#
# print(type('nume'))
# print(type(varsta))
# print(type(inaltime))
# print(type(conditie))
#
# # 4. Rotunjește ‘float’-ul folosind funcția round() și salvează această modificare în aceeași variabilă (suprascriere)
# # Verifică tipul acesteia.
#
# inaltime=round(inaltime)
# print(inaltime)
# print(type(inaltime))
#
# # 5. Folosește print() și printează în consolă 4 propoziții folosind cele 4 variabile.
# # Rezolvă nepotrivirile de tip prin ce modalitate dorești.
#
# print(f'Numele meu este {nume}.')
# print(f'Am varsta de {varsta} de ani.')
# print(f'Am {inaltime}m inaltime.')
# print(f'Propozitia de mai sus este {conditie}.')
#
# # 6. Citește de la tastatură: numele; prenumele. Afișează: 'Numele complet are x caractere'.
#
# Prenume=str(input('Introdu prenumele '))
# Nume=str(input('Introdu numele '))
# nume_complet=len(Prenume)+len(Nume)
# n_complet=len(Prenume+Nume)
# #print(f'Numele complet are {nume_complet} caractere.')
# #print(f'Numele complet are {len(Prenume+Nume)} caractere')
# print(f'Numele complet are {n_complet} caractere')
#
# # 7. Citește de la tastatură: lungimea; lățimea. Afișează: 'Aria dreptunghiului este x'.
#
# L=float(input('Introdu lungimea: '))
# l=float(input('Introdu latimea: '))
# A=L*l
# print(f'Aria dreptunghiului este: {A}')

# # 8. Având stringul: 'Coral is either the stupidest animal or the smartest rock': afișează de câte ori apare
# cuvântul 'the';
#
# str1='Coral is either the stupidest animal or the smartest rock'
# nr_de_ori=str1.count('the')
# print(f'Grupul de litere "the" apare in propozitie de {nr_de_ori} ori')
# print(str1.count('the'))

# 9. Același string: Afișează de câte ori apare cuvântul 'the';  Printează rezultatul.

# str1='Coral is either the stupidest animal or the smartest rock'
# same

# #10. Același string: Folosește un assert ca să verifici dacă acest string conține doar numere.
#
# str1 = 'Coral is either the stupidest animal or the smartest rock'
# assert str1.isnumeric()

# # 11. Exercițiu: citește de la tastatură un string de dimensiune impară; afișează caracterul din mijloc.
#
# str2 = input('Introdu un string de dimensiune impara: ')
# L = len(str2)
# if L % 2 == 1:
#     print(str2[(L // 2)])
# else:
#     print(f'\nNumarul de caractere introdus este par')

# # 12. Folosind o singură linie de cod : citește un string de la tastatură (ex: 'alabala portocala'); salvează fiecare
# cuvânt într-o variabilă; printează ambele variabile pentru verificare.
#
# print(input('Introdu 2 cuvinte: ').split())


# # 13. Exercițiu: citește un string de la tastatură (ex: alabala portocala); salvează primul caracter într-o variabilă -
# # indiferent care este el, încearcă cu 2 stringuri diferite; capitalizează acest caracter peste tot, mai puțin pentru
# # primul și ultimul caracter => alAbAlA portocAla.
#
# str3 = input('Introdu un text: ')
# char_unu = str3[0]
# print(char_unu)
# str4 = str3[1:-1].replace(char_unu, char_unu.upper())
# print(f'\n{str3}')
# print(f' {str4}')
# print(char_unu + str4 + str3[-1])




# 14.Exercițiu:
# citește un user de la tastatură;
# citește o parolă;
# afișează: 'Parola pt user x este ***** și are x caractere';
# ***** se va calcula dinamic, indiferent de dimensiunea parolei, trebuie să afișeze corect.
#
# eg: parola abc => ***
#       parola abcd => ****

# user = input('user = ')
# parola = input('parola = ')
# p = len(parola)
# parola_ascunsa = '*' * p
# print(f'Parola pentru user-ul {user} este {parola_ascunsa} si are {p} caractere')