# # ex1
#
# from abc import ABC, abstractmethod
#
# class Abstract_Video(ABC):
#     @abstractmethod
#     def show_details(self):
#         pass
#     def paly(self):
#         print('Video is playing')
#
# # ex2
#
# class Videoclip(Abstract_Video):

'''
    OOP - advance

    Exerciții - studiu în workshopul de weekend

    1. ABSTRACTION
    Clasa abstractă FormaGeometrica
    Conține un field PI=3.14
    Conține o metodă abstractă aria (opțional)
    Conține o metodă a clasei descrie() - aceasta printează pe ecran ‘Cel mai probabil am colturi’

from abc import ABC, abstractmethod


class FormaGeometrica(ABC):
    pi = 3.14

    @abstractmethod
    def aria(self):
        pass

    def descrie(self):
        print('Cel mai probabil am colturi')
"""
    2. INHERITANCE
    Clasa Pătrat - moștenește FormaGeometrica
    constructor pentru latură

    ENCAPSULATION
    latura este proprietate privată
    Implementează getter, setter, deleter pentru latură
    Implementează metoda cerută de interfață (opțional, doar dacă ai ales să implementezi metoda abstractă aria)
"""

# class Patrat(FormaGeometrica):
#     def __init__(self, latura):
#         self.__latura = latura
#     @property

    2.
    INHERITANCE
    Clasa Pătrat - moștenește FormaGeometrica
    constructor
    pentru
    latură

    ENCAPSULATION
    latura
    este
    proprietate
    privată
    Implementează
    getter, setter, deleter
    pentru
    latură
    Implementează
    metoda
    cerută
    de
    interfață(opțional, doar
    dacă
    ai
    ales
    să
    implementezi
    metoda
    abstractă
    aria)
    """
    # class Patrat(FormaGeometrica):
    # 
    #     def init(self, latura):
    #         self.latura = latura
    # 
    #     # @abstractmethod
    #     def aria(self):
    #         aria = self.latura * self.latura
    #         return aria
    # 
    #     @property
    #     def latura(self):
    #         return self.latura
    # 
    #     @latura.getter
    #     def latura(self):
    #         print("Get")
    #         return self.latura
    # 
    #     @latura.setter
    #     def latura(self, value):
    #         print("Set")
    #         self.latura = value
    # 
    #     @latura.deleter
    #     def latura(self):
    #         print("Delete")
    #         self.__latura = 0
    # 
    # patrat1 = Patrat(55)
    # print(patrat1.aria())
    # patrat1.descrie()
    # print(patrat1.latura)
    # patrat1.latura = 11
    # print(patrat1.latura)
    # print(patrat1.aria())
    # del patrat1.latura
    # print(patrat1.latura)
"""
    3. Clasa Cerc - moștenește FormaGeometrica
    constructor pentru rază
    raza este proprietate privată
    Implementează getter, setter, deleter pentru rază
    Implementează metoda cerută de interfață - în calcul folosește field PI mostenit din clasa părinte (opțional, doar dacă ai ales să implementezi metoda abstractă aria)
"""
class Cerc(FormaGeometrica):
    def init(self, raza):
        self.raza = raza

    def aria(self):
        aria = self.PI * self.raza * self.raza
        return aria

    @property
    def raza(self):
        return self.raza

    @raza.getter
    def raza(self):
        print("Get")
        return self.raza

    @raza.setter
    def raza(self, value):
        print("Set")
        self.raza = value

    @raza.deleter
    def raza(self):
        print("Delete")
        self.__raza = 0

cerc1 = Cerc(10)
print(cerc1.aria())
print(cerc1.raza)
cerc1.raza = 4
print(cerc1.aria())
print(cerc1.raza)
del cerc1.raza
print(cerc1.raza)
print(cerc1.PI)
print(cerc1.aria())
cerc1.descrie()

"""
    4. POLYMORPHISM 
    Definește o nouă metodă descrie - printează ‘Eu nu am colturi’
"""
#trebuie pus in Cerc:
def descrie(self):
        print('Eu nu am colturi')

"""
    5. Creează un obiect de tip Pătrat și joacă-te cu metodele lui
    Creează un obiect de tip Cerc și joacă-te cu metodele lui
"""

#l-am facut deja mai sus
"""
    6. Actualizează proiectul pe github facand un push la noul cod
    În Folderul de teme ajunge să pui doar linkul cu proiectul tău public

    Sa avem github-ul instalat și să ne incarcam în acesta fișierele python lucrate în workshop-urile de weekend.



### EXERCITII EXTRA


EXERCITII BONUS - OOP - EXTRA


1.
a. Defineste clasa User.
Clasa User va avea urmatoarele atribute:
username (public) - se seteaza in constructor
email (public) - se seteaza in constructor
password (privat) - Nu primim atribut pentru el in constructor,
ci il initializam noi cu None (self.__password == None).



class User:

    def init(self,username, email):
        self.username = username
        self.email = email
        self.__password = None


obiect1 = User('flaviu','flaviudetesan@gmail.com')
print(obiect1.email)
print(obiect1.username)


b. Implementeaza proprietatea password care va incapsula atributul privat
password.
Va avea:
- getter:
In getter verificam daca parola a fost setata (daca are valoare).
Daca are valoare, atunci vom returna ***, unde numarul de * va fi egal
cu lungimea parolei.
Daca nu e setata, atunci afisam un mesaj ca parola nu e setata.
- setter:
In setter vom verifica, inainte sa setam parola, ca aceasta indeplineste
urmatoarele conditii:
    -- are minim 10 caractere
    -- are cel putin o litera mare
Daca aceste conditii se indeplinesc atunci setam parola.
Daca nu, afisam un mesaj corespunzator pentru fiecare situatie.

c. Metode:
- Metoda login: verificam ca user-ul are atat username, email si parola.
Daca are, atunci afisam mesajul "Conectat".
Daca nu, afisam mesajul "Lipsesc credentiale de conectare. Nu va putem conecta"

d. Asigura-te ca creezi cel putin doua obiecte din clasa User.
Afiseaza toate atributele/metodele/proprietatile.
"""


"""
2.
a. Defineste clasa abstracta Person.
Metode abstracte: wake_up, sleep, eat.
Metoda: describe -> afiseaza mesajul "O persoana se trezeste, mananca si doarme."

b. Defineste clasa Student.
Clasa Student implementeaza clasa abstracta Person.
Atribute in constructor: name, university, grade.
Metode describe -> afiseaza SI mesajul:
Studentul x, studiaza la universitatea y si are nota generala z.

c. Defineste clasa Employee.
Clasa Employee implementeaza cls abstracta Person.
Atribute in constructor: name, experience, salary.
Salary este un atribut privat!
Metoda describe -> afiseaza SI mesajul:
Angajatul x lucreaza de y ani.

d. Creeaza proprietatea salary care sa incapsuleze atributul privat salary.
"""