# #8. X, y, z - laturile unui triunghi. Afișează dacă triunghiul este isoscel, echilateral sau oarecare.
#
# x = 2
# y = 3
# z = 4
# if x == y == z:
#     print('triunghi echilateral')
# elif x == y or y == z or x == z:
#     print('triunghi isoscel')
# else:
#     print('triunghi oarecare')
#
# #9. Citește o literă de la tastatură.     Verifică și afișează dacă este vocală sau nu.
#
# l= input('Introdu o litera: ')
# # if(l =='a' or l =='e' or l == 'i' or l == 'o' or l == 'u' or l == 'ă' or l == 'â' or l == 'î'):
# if l in ('a', 'e', 'i', 'o', 'u', 'ă', 'â', 'î'):
#     print('Litera introdusa este o vocala.')
# else:
#     print('Litera introdusa este o consoana.')
#
# # 10.Transformă și printează notele din sistem românesc în  cel american Peste 9 => A / Peste 8 - B / Peste 7 - C / Peste 6 - D / Peste 4 - E / 4 sau sub - F
#
# intrebare=float(input('Introdu nota obtinuta: '))
# if 0<=intrebare<=4:
#     print('Nota obtinuta este echivalenta cu F')
# elif 4<interbare>6:
#     print('Nota obtinuta este echivalenta cu E')
# elif 6<=intrebare<7:
#     print('Nota obtinuta este echivalenta cu D')
# elif 7<=intrebare<8:
#     print('Nota obtinuta este echivalenta cu C')
# elif 8<=intrebare<9:
#     print('Nota obtinuta este echivalenta cu B')
# else:
#     print('Nota obtinuta este echivalenta cu A')
#
# # 11.Verifică dacă x are minim 4 cifre (x e int).
# # (ex: 7895 are 4 cifre, 10 nu are minim 4 cifre)


# 12.Verifică dacă x are exact 6 cifre.

# x=int(input('nr= '))
# if 100_000<=abs(x)<=1_000_000:
#     print('x are exact 6 cifre')
# else:
#     print('x nu are exact 6 cifre')




# 11.Verifică dacă x are minim 4 cifre (x e int).
# x = int(input('Introdu un numar: '))
# x = str(x)
# # if len(x) >= 4:
# #     print('Numarul introdus este format din minim 4 cifre.')
# # else:
# #     print('Numarul introdus are mai putin de 4 cifre.')
#
# # (ex: 7895 are 4 cifre, 10 nu are minim 4 cifre)
#
# # 12.Verifică dacă x are exact 6 cifre.
#
# # solutia urmatoare nu este valabila pt nr negative
# # x = int(input('Introdu un numar: '))
# # # x = str(x)
# # if len(x) == 6:
# #     print('Numar introdus este format din 6 cifre.')
# # elif len(x) < 6:
# #     print('Numarul introdus este format din mai putin de 6 cifre.')
# # else:
# #     print('Numarul introdus este format din mai mult de 6 cifre.')
#
# x = int(input('Introdu un numar: '))
# if 100_000 <= abs(x) <1_000_000:
#     print('x are exact 6 cifre')
# else:
#     print('x nu are exact 6 cifre')

# 13.Verifică dacă x este număr par sau impar (x e int).

# x=int(input('introdu un numar: '))
# if x%2==0:
#     print('numarul introdus este un numar par')
# else:
#     print('numarul introdus este un numar impar')


