"""
PARTEA 2 - OOP: Clase & Obiecte
"""

"""
1.Clasa Cerc
    Atribute: rază, culoare
    Constructor pentru ambele atribute
    Metode:
descrie_cerc() - va PRINTA culoarea și raza
aria() - va RETURNA aria
diametru()
circumferinta()
"""
# class Cerc:
#     def __init__(self, raza, culoare):
#         self.raza = raza
#         self.culoare = culoare
#     def descrie_cerc(self):
#         print(f'Cercul are raza {self.raza} si culoarea {self.culoare}')
#     def aria(self):
#         a = 3.14 * self.raza ** 2
#         return a
#     def diametru(self):
#         d = 2 * self.raza
#         return d
#     def circumferinta(self):
#         c = 3.14 * self.raza * 2
#         return c
# cerc_obj = Cerc(2, 'portocaliu')
# print(cerc_obj.raza)
# print(cerc_obj.culoare)
# cerc_obj.descrie_cerc()
# print(cerc_obj.aria())
# print(cerc_obj.diametru())
# print(cerc_obj.circumferinta())


# #varianta lor
# class Cerc:
#     def init(self, raza, culoare):
#         self.raza = raza
#         self.culoare = culoare
#
#     def descrie_cerc(self):
#         print(f"Cercul are raza {self.raza} si culoarea {self.culoare}.")
#
#     def calculeaza_arie(self):
#         arie = 3.14 * self.raza ** 2
#         return arie
#
#     def diametru(self):
#         diametru = 2 * self.raza
#         return diametru
#
#     def circumferinta(self):
#         circumferinta = 3.14 * 2 * self.raza
#         return circumferinta
#
# cerc1 = Cerc(5, "portocaliu")
# print(cerc1.raza)
# print(cerc1.culoare)
# cerc1.descrie_cerc()
# print(cerc1.calculeaza_arie())
# print(cerc1.diametru())
# print(cerc1.circumferinta())
#
# cerc2 = Cerc (9, "verde")
# print(cerc2.raza)
# print(cerc2.culoare)
# cerc2.descrie_cerc()
# print(cerc2.calculeaza_arie())
# print(cerc2.diametru())
# print(cerc2.circumferinta())

"""
2. Clasa Dreptunghi
     Atribute: lungime, lățime, culoare
     Constructor pentru toate atributele
     Metode:
descrie()
aria()
perimetrul()
schimbă_culoarea(noua_culoare) - această metodă nu returneaza nimic. Ea va lua ca și parametru o nouă culoare și va suprascrie atributul self.culoare. Poți verifica schimbarea culorii prin apelarea metodei descrie().
"""
# class Dreptunghi:
#     def init(self, lungime, latime, culoare):
#         self.lungime = lungime
#         self.latime = latime
#         self.culoare = culoare
#
#     def descrie(self):
#         print(self.culoare)
#
#     def calculeaza_aria(self):
#        aria = self.latime * self.lungime
#        print(aria)
#        return aria
#
#     def perimetrul(self):
#         perimetru = 2*(self.lungime + self.latime)
#         print(perimetru)
#         return perimetru
#
#     def schimba_culoarea(self, noua_culoare):
#         self.culoare = noua_culoare
#         print(noua_culoare)
#
#
# dreptunghi1 = Dreptunghi(latime=2,lungime=6,culoare='rosu')
#
# dreptunghi1.calculeaza_aria()
# dreptunghi1.perimetrul()
# dreptunghi1.descrie()
# dreptunghi1.schimba_culoarea('verde')
# print(dreptunghi1.latime)
# print(dreptunghi1.lungime)
# print(dreptunghi1.culoare)
#
# dreptunghi2 = Dreptunghi(4,5,'alb')
#
# dreptunghi2.calculeaza_aria()
# dreptunghi2.perimetrul()
# dreptunghi2.descrie()
# dreptunghi2.schimba_culoarea('albastru')
# print(dreptunghi2.latime)
# print(dreptunghi2.lungime)
# print(dreptunghi2.culoare)

"""
3. Clasa Angajat
     Atribute: nume, prenume, salariu
     Constructor pentru toate atributele
     Metode:
descrie()
nume_complet()
salariu_lunar()
salariu_anual()
marire_salariu(procent)
"""
# class Angajat:
#     def init(self, nume, prenume, salariu):
#         self.nume = nume
#         self.prenume = prenume
#         self.salariu = salariu
#
#     def descrie(self):
#         print(f"\nAngajatul {self.nume} {self.prenume} are un salariu de {self.salariu} lei.")
#
#     def nume_complet(self):
#         return f"{self.nume} {self.prenume}"
#
#     def salariu_lunar(self):
#         return {self.salariu}
#
#     def salariu_anual(self):
#         return self.salariu * 12
#
#     def marire_salariu(self, procent):
#         self.salariu += round(self.salariu * procent / 100)
#
# # Exemplu
# angajat = Angajat("Popescu", "Ion", 3500)
# angajat.descrie()  # Output: Angajatul Popescu Ion are un salariu de 3500 lei.
# print("Nume complet:", angajat.nume_complet())  # Output: Nume complet: Popescu Ion
# print("Salariu anual:", angajat.salariu_anual()) # Output: Salariu anual: 84000
# angajat.marire_salariu(10)
# print(f"Salariul angajatului {angajat.nume_complet()} a fost mărit și este acum {angajat.salariu}") # Salariul angajatului Lupu Andrei a fost mărit și este acum 7350
#
#
# angajat1= Angajat("Lupu", "Andrei", 7000)
# angajat1.descrie()
# print("Nume complet:", angajat1.nume_complet())
# print("Salariu anual:", angajat1.salariu_anual())
# angajat1.marire_salariu(5)
# print(f"Salariul angajatului {angajat1.nume_complet()} a fost mărit și este acum {angajat1.salariu}")
#
# angajat2 = Angajat("Manea", "Andreea", 5500)
# angajat2.descrie()
# print("Nume complet:", angajat2.nume_complet())
# print("Salariu anual:", angajat2.salariu_anual())
# angajat2.marire_salariu(17)
# print(f"Salariul angajatului {angajat2.nume_complet()} a fost mărit și este acum {angajat2.salariu}")
"""
4. Clasa Cont
   Atribute: iban, titular_cont, sold
   Constructor pentru toate atributele
   Metode:
afisare_sold() - Titularul x are în contul y suma de n lei
debitare_cont(suma)
creditare_cont(suma)
"""
# class Cont:
#     def __init__(self, iban, titular, sold):
#         self.iban = iban
#         self.titular = titular
#         self.sold = sold
#     def afisare_sold(self):
#         print(f'{self.titular} are in contul {self.iban} suma de {self.sold} ')
#     def debitare_cont(self):
#         return self.sold - suma
#     def creditare_cont(self):
#         return self.sold + suma

#     #varianta lor:
# class Cont:
#     def init(self, iban, titular_cont, sold):
#         self.iban = iban
#         self.titular_cont = titular_cont
#         self.sold = sold
#     def afisare_sold(self):
#         print(f"Titulatul {self.titular_cont} are in contul {self.iban} suma de {self.sold} lei.")
#     def debitare_cont(self, suma):
#         if suma > self.sold:
#             print(f"Tranzactie esuata, soldul disponibil in contul {self.iban} este {self.sold}")
#         else:
#             self.sold -= suma
#             print(f"Tranzactie acceptata. Suma de {suma} lei a fost debitata din contul {self.iban}. Soldul disponibil este acum de {self.sold} lei.")
#     def creditare_cont(self, suma):
#         self.sold += suma
#         print(f"Contul {self.iban} a fost alimentat cu suma de {suma} lei. Soldul disponibil este acum de {self.sold} lei.")
#
# cont1 = Cont("ROU1234567890", "Andrei Ivan", 8000)
# cont1.afisare_sold()
# cont1.debitare_cont(2000)
# cont1.creditare_cont(6000)
# cont1.debitare_cont(7500)
"""
5. Clasa Factură
     Atribute: seria (va fi constantă, nu trebuie constructor, toate facturile vor avea aceeași serie), număr, nume_produs, cantitate, pret_buc
     Constructor: toate atributele, fără serie
     Metode:
schimbă_cantitatea(cantitate)
schimbă_prețul(pret)
schimbă_nume_produs(nume)
generează_factura() - va printa tabelar dacă reușiți

Factura seria x număr y
Data: generează automat data de azi
Produs | cantitate | preț bucată | Total
Telefon |      7       |       700       | 49000

Indiciu pentru dată: https://www.geeksforgeeks.org/get-current-date-using-python/
"""
