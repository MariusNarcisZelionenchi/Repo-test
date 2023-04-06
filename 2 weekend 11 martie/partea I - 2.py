# Partea 2 - Operatori, condiționale

# Exerciții - studiu în workshopul de weekend

# Pentru toate exercițiile se va folosi noțiunea de if în rezolvare.
# Indirect vei exersa și operatorii în cadrul condițiilor ramurilor din if.
# X poate fi inițializat direct în cod sau citit de la tastatură, după preferințe.
# X este un int.

# 1. Explică cu cuvintele tale în cadrul unui comentariu cum funcționează un if else.

# if-else este un conditional care ne ajuta sa executam cod in functie de anumite conditii.
# intr-un if avem prima data definita ramura if; aceasta se executa doar daca conditia de la if se egaleaza ca fiind
# adevarata
# daca nu e adevarata se va executa else
# elif ne ajuta sa punem mai multe conditii
# ex:

# x = int(input('Introdu un numar '))
# if x == 10:
#     print('Numarul ales este 10')
# elif x <= 0:
#     print('Ai introdus un numar negativ')
# elif x < 10:
#     print('Numarul ales este mai mic decat 10')
# else:
#     print('Numarul ales este mai mare decat 10')

# 2. Verifică și afișează dacă x este număr natural sau nu.

# x = float(input('Introdu un numar x = '))
# if x >= 0 and x == int(x):
#     print('x este un numar natural')
# else:
#     print('x nu este un numar natural')

# 3. Verifică și afișează dacă x este număr pozitiv, negativ sau neutru.

# if x > 0:
#     print(f'\nx este un numar pozitiv')
# elif x == 0:
#     print(f'\nx este un numar neutru')
# else:
#     print(f'\nx este un numar negativ')

# 4. Verifică și afișează dacă x este între -2 și 13.

# if -2 <= x <= 13:
#     print(f'\nx este cuprins intre -2 si 13, inclusiv')
# else:
#     print(f'\nx nu este cuprins intre -2 si 13')

# 5. Verifică și afișează dacă diferența dintre x și y este mai mică de 5.

# y = float(input(f'\nIntrodu un alt numar y = '))
# dif = x - y
# if dif < 5:
#     print(f'\nDiferenta dintre x si y este mai mica decat 5')
# else:
#     print(f'\nDiferenta dintre x si y este mai mare decat 5')

# 6. Verifică dacă x NU este între 5 și 27  - a se folosi ‘not’.
# if not(5 < x < 27):
#     print(f'\nx nu este cuprins intre 5 si 27')
# else:
#     print(f'\nx este cuprins intre 5 si 27')

# 7.
# x și y (int)
# Verifică și afișează dacă sunt egale, dacă nu afișează care din ele este mai mare.

# if x == y:
#     print(f'\nNumerele introduse sunt egale')
# elif x >= y:
#     print(f'\nx este mai mare decat y')
# else:
#     print(f'\nx este mai mic decat y')

# 8.
# x, y, z - laturile unui triunghi.
# Afișează dacă triunghiul este isoscel, echilateral sau oarecare.

# x = float(input('x = '))
# y = float(input('y = '))
# z = float(input('z = '))
#
# if x == y == z:
#     print('triunghi echilateral')
# elif x == y or x == z or y == z:
#     print('triunghi isoscel')
# else:
#     print('triunghi oarecare')

# 9. Citește o literă de la tastatură.
#     Verifică și afișează dacă este vocală sau nu.

# litera = input('introdu o litera: ')
# list = ['a', 'e', 'i', 'o', 'u' ]
#
# if litera in list:
#     print('litera introdusa este o vocala')
# else:
#     print('litera introdusa este o consoana')

# 10.Transformă și printează notele din sistem românesc în  sistem american
# Peste 9 => A
# Peste 8 => B
# Peste 7 => C
# Peste 6 => D
# Peste 4 => E
# 4 sau sub => F

# x = int(input('introdu un numar x = '))
#
# if x > 9:
#     print('ai luat nota A')
# elif 8 < x <= 9:
#     print('ai luat nota B')
# elif 7 < x <= 8:
#     print('ai luat nota C')
# elif 6 < x <= 7:
#     print('ai luat nota D')
# elif 4 < x <= 6:
#     print('ai luat nota E')
# else:
#     print('ai luat nota F')

# # 11.Verifică dacă x are minim 4 cifre (x e int).
# # (ex: 7895 are 4 cifre, 10 nu are minim 4 cifre)
#
# x = int(input('introdu valoarea lui x:  '))
#
# if len(str(x)) >= 4:
#     print('numarul introdus are minim 4 cifre')
# else:
#     print('nuamrul introdus are maxim 3 cifre')
#
# # 12.Verifică dacă x are exact 6 cifre.
#
# if len(str(x)) == 6:
#     print('numarul introdus are 6 cifre')
# else:
#     print('numarul introdus  nu are 6 cifre')
#
# # 13.Verifică dacă x este număr par sau impar (x e int).
#
# if x % 2 == 1:
#     print('numarul introdus este un nr impar')
# else:
#     print('numarul introdus este un nr par')

# 14.      x, y, z (int)
# Afișează care este cel mai mare dintre ele?

# x = int(input('introdu valoarea lui x: '))
# y = int(input('introdu valoarea lui y: '))
# z = int(input('introdu valoarea lui z: '))
#
# if x > y and x > z:
#     print(x)
# elif y > x and y > z:
#     print(y)
# else:
#     print(z)

# 15.
# x, y, z - reprezintă unghiurile unui triunghi
# Verifică și afișează dacă triunghiul este valid sau nu.

# x = int(input('introdu valoarea unghiului x: '))
# y = int(input('introdu valoarea unghiului y: '))
# z = int(input('introdu valoarea unghiului z: '))
#
# if x + y + z == 180:
#     print('triunghi valid')
# else:
#     print('triunghiul nu este valid')

# 16. Având stringul: 'Coral is either the stupidest animal or the smartest rock'
# Citește de la tastatură un int x
# Afișează stringul fără ultimele x caractere
# Exemplu: dacă ai ales 7 => 'Coral is either the stupidest animal or the smarte'

# str = 'Coral is either the stupidest animal or the smartest rock'
# x = int(input('introdu un nr: '))
# print(str[:len(str) - x])

# 17. Același string. Declară un string nou care să fie format din primele 5 caractere + ultimele 5.

# str = 'Coral is either the stupidest animal or the smartest rock'
# str_nou = str[:5] + str[-5:]
# print(str_nou)

# 18. Același string.
# Salvează într-o variabilă și afișează indexul de start al cuvântului rock (hint: este o funcție care te ajuta sa faci asta)
# Folosind această variabilă + slicing, afișează tot stringul până la acest cuvânt
# output: 'Coral is either the stupidest animal or the smartest'

# str = 'Coral is either the stupidest animal or the smartest rock'
# index_start_rock = str.index('rock')
# print(index_start_rock)
# print(str[:index_start_rock])

# 19. Joc ghicit zarul
# Caută pe net și vezi cum se generează un număr random
# Ne imaginăm ca dai cu zarul și salvăm acest număr în dice_roll
# Ia numărul ghicit de la utilizator
# Verifică și afișează dacă utilizatorul a ghicit
# Vei avea 3 opțiuni
# Ai pierdut. Ai ales un numar mai mic. Ai ales x dar a fost y.
# Ai pierdut. Ai ales un numar mai mare. Ai ales x dar a fost y.
# Ai ghicit. Felicitări! Ai ales x si zarul a fost y.

# import random
#
# x = int(input('alege un numar x: '))
# y = random.randint(1,6)
# print(y)
#
# if x == y:
#     print(f'Ai ghicit. Felicitări! Ai ales {x} si zarul a fost {y}.')
# elif x > y:
#     print(f'Ai pierdut. Ai ales un numar mai mare. Ai ales {x} dar a fost {y}.')
# else:
#     print(f'Ai pierdut. Ai ales un numar mai mic. Ai ales {x} dar a fost {y}.')

# 20.  Citește de la tastatură un string
# Verifică dacă primul și ultimul caracter sunt la fel. Se va folosi un assert
# Atenție: se dorește ca programul să fie case insensitive - 'apA' e acceptat

# str = input('introdu un text: ')
#
# assert str[0].lower() == str[-1].lower(), 'caracterele sunt diferite'
# print('caracterele sunt identice')



# 21. Având stringul '0123456789'
# Afișează doar numerele pare
# Afișează doar numerele impare
# (hint: folosește slicing, controlează din pas)

# str = '0123456789'
# print(str[::2])
# print(str[1::2])