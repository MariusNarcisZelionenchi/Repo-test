"""

PARTEA 2: CICLURI REPETITIVE

Exerciții - studiu în workshopul de weekend

"""

"""
1.Având lista:
mașini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel'] 

Folosește un for că să iterezi prin toată lista și să afișezi;
‘Mașina mea preferată este x’.
Fă același lucru cu un for each.
Fă același lucru cu un while.
"""
#masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
# #v0
# for i in range(0,len(masini)):
#     print(f"\nMașina mea preferată este {masini[i]}")
# #
# # # v1 - v2 prescurtat
# # [print(f"\nMașina mea preferată este {m}") for m in masini]
# #
# #v2
# for m in masini:
#     print(f"\nMașina mea preferată este {m}")
# #
# #v3
# m = 0
# while m < len(masini):
#     print(f"\nMașina mea preferată este {masini[m]}")
#     m += 1
"""
2. Aceeași listă:
Folosește un for else
În for:
Modifică elementele din listă astfel încât să fie scrise cu majuscule, exceptând primul și ultimul.
În else:
  Printează lista.
"""
# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
# for i in range(0,len(masini)):
#     if i == 0 or i == len(masini)-1:
#         continue
#     masini[i] = masini[i].upper()
#
# else:
#     print(masini)
"""
3. Aceeași listă:
Vine un cumpărător care dorește să cumpere un Mercedes.
Iterează prin ea prin modalitatea aleasă de tine.
Dacă mașina e mercedes:
   Printează ‘am găsit mașina dorită de dvs’
   Ieși din ciclu folosind un cuvânt cheie care face acest lucru
Altfel:
   Printează ‘Am găsit mașina X. Mai căutam‘
"""
# #v1
# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
# i = 0
# while i < len(masini):
#     print(masini[i])
#     if (masini[i]) == 'Mercedes':
#         print('Am gasit masina dorita de dumneavoastra')
#         break
#     print(f'Am găsit mașina {masini[i]}. Mai căutam')
#     i +=1
# #v2
# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
# for i in range(0,len(masini)):
#     if masini[i] == 'Mercedes':
#         print("Am gasit masina dorita de dumneavoastra")
#         break
#     print(f'Am gasit masina {masini[i]}. Mai cautam')
# #v3
# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
# for m in masini:
#     if m == 'Mercedes':
#         print("Am gasit masina dorita de dumneavoastra")
#         break
#     print(f'Am gasit masina {m}. Mai cautam')
"""
4. Aceeași listă;
Vine un cumpărător bogat dar indecis. Îi vom prezenta toate mașinile cu excepția Trabant și Lăstun. 

Dacă mașina e Trabant sau Lăstun:
   Folosește un cuvânt cheie care să dea skip la ce urmează (nu trebuie else).
Printează S-ar putea să vă placă mașina x.
"""
# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
# for m in masini:
#     if m == 'Trabant' or m == 'Lastun':
#         continue
#     print(f'S-ar putea să vă placă mașina {m}')
"""
5. Modernizează parcul de mașini:

Crează o listă goală, masini_vechi.
Iterează prin mașini.
Când găsesti Lăstun sau Trabant:
Salvează aceste mașini în masini_vechi.
Suprascrie-le cu ‘Tesla’ (în lista inițială de mașini).
Printează Modele vechi: x.
Modele noi: x.
"""
# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
# masini_vechi=[]
# for m in masini:
#     if m == 'Trabant' or m == 'Lastun:':
#         masini_vechi.append(m)
#         masini.remove(m)
#         masini.append('Tesla')
# print(f'Modelele vechi: {masini_vechi}')
# print(f'Modele noi: {masini}')
"""
6. Având dict:
pret_masini = {
    'Dacia': 6800,
    'Lăstun': 500,
    'Opel': 1100,
    'Audi': 19000,
    'BMW': 23000
}

Vine un client cu un buget de 15000 euro.

Prezintă doar mașinile care se încadrează în acest buget.
Iterează prin dict.items() și accesează mașina și prețul.
Printează Pentru un buget de sub 15000 euro puteți alege mașină xLastun
Iterează prin listă.
"""
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
pret_masini = {
    'Dacia': 6800,
    'Lastun': 500,
    'Opel': 1100,
    'Audi': 19000,
    'BMW': 23000}
# #INFO GENERALE
# #accesam cheile din dictionar folosind keys()
# for cheie in pret_masini.keys():
#     print(cheie)
# #accesam valorile din dictionar folosind values()
# for val in pret_masini.values():
#     print(val)
# #accesam cheile si valorile din dictionar folosinf items()
# for cheie, val in pret_masini.items():
#     print(cheie, val)

# PENTRU EXERCITIU
# for masina, pret in pret_masini.items():
#     print(masina,pret)
#     if pret < 15_000:
#         print(f'Pentru un buget de sub 15000 euro puteți alege mașina {masina}')
#     else:
#         print(f'Bugetul nu este suficient pentru a cumpara masina {masina}, care costa {pret}')
"""
7. Având lista:
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
Iterează prin ea.
Afișează de câte ori apare 3 (nu ai voie să folosești count).
"""
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# #print(numere.count(3))
# trei = 0
# for trei in numere:
#     if trei == 3:
#         trei += 1
# print(trei)
"""
8. Aceeași listă:
Iterează prin ea
Calculează și afișează suma numerelor (nu ai voie să folosești sum).
"""
# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# # print(sum(numere))
# sum = 0
# for numar in numere:
#    # print(numar)
#     sum += numar
# print(sum)
"""
9. Aceeași listă:
Iterează prin ea.
Afișază cel mai mare număr (nu ai voie să folosești max).
"""
# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# maxim = numere [0]
# for nr in numere:
#     if nr > maxim:
#         maxim = nr
# print(maxim)
"""
10. Aceeași listă:
Iterează prin ea.
Dacă numărul e pozitiv, înlocuieste-l cu valoarea lui negativă.
Ex: dacă e 3, să devină -3
Afișază noua listă.
"""
# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# print(numere)
# for i in range(0, len(numere)):
#     if numere[i] > 0:
#         numere[i] =numere[i] * (-1)
#     else:
#         numere[i] = 0 - numere[i]
# print(numere)


# # foreach
# my_list = []
#
# for numar in numere:
#     if numar > 0:
#         nr_negativ = numar * -1
#         my_list.append(nr_negativ)
#     else:
#         my_list.append(numar)
# print(my_list)
"""
11.
alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []
Itereaza prin listă alte_numere 
Populează corect celelalte liste
Afișează cele 4 liste la final
"""

alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_pare = []
numere_impare = []
numere_negative = []
numere_pozitive = []

# for nr in alte_numere:
#     if nr % 2 == 0:
#         numere_pare.append(nr)
#     else:
#         numere_impare.append(nr)
# for nr in alte_numere:
#     if nr < 0:
#         numere_negative.append(nr)
#     else:
#         numere_pozitive.append(nr)
#
# print(numere_pare)
# print(numere_impare)
# print(numere_negative)
# print(numere_pozitive)


"""
12. Aceeași listă:
Ordonează crescător lista fară să folosești sort.
Te poți inspira vizual de aici.
https://www.youtube.com/watch?v=lyZQPjUT5B4
"""

alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]

for nr in alte_numere:
    if

"""
13. Ghicitoare de număr:
numar_secret = Generați un număr random între 1 și 30
Numar_ghicit = None
Folosind un while
   User alege un număr
   Programul îi spune:
Nr secret e mai mare
Nr secret e mai mic
Felicitări! Ai ghicit!
"""

"""
14. Alege un număr de la tastatură
Ex: 7
Scrie un program care să genereze în consolă următoarea piramidă
1
22
333
4444
55555
666666
7777777

Ex:3
1
22
333
"""

"""
15.
tastatura_telefon = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9],
  [0]
]
Iterează prin listă 2d
Printează ‘Cifra curentă este x’
(hint: nested for - adică for în for)
"""

"""
Exerciții Recomandate - studiu individual                                        .

1. Revizualizează sesiunile din această săptămână și ia notițe în caz că ți-a scăpat ceva.

2. Vizualizează din cursul  ‘Primii pași în Programare’ de la sectiunile de mai jos:
Structuri de date 
Flow Control
"""
