class User:

    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.__password = None

    @property
    def  password(self):
        return self.__password

    @password.getter
    def password(self):
        print('Get')
        if self.__password is not None:
            rezultat = len(self.__password) * '*'
            return rezultat
        else:
            print('Parola nu este setata')




obiect1 = User('flaviu','flaviudetesan@gmail.com')
print(obiect1.email)
print(obiect1.username)
print(obiect1.password)



# Exercitiu 1a EXTRA
#
# class User:
#     def init(self, username, email):
#         self.username = username
#         self.email = email
#         self.password = None
#
#     @property
#     def password(self):
#         return self.password
#
#     @password.getter
#     def password(self):
#         if (self.password) is not None:
#             rezultat = len(self.password) * "*"
#             return rezultat
#         else:
#             print("Parola nu este setata.")
#
#     @password.setter
#     def password(self, new_password):
#         if new_password is not None and len(new_password) >= 10:
#             for char in new_password:
#                 if char.isupper():
#                     self.__password = new_password
#                     break
#             else:
#                 print("Parola nu contine majuscule.")
#         else:
#             print("Parola trebuie sa aiba minim 10 caractere.")
#
#
#
# obiect1 = User("Claudiu" , "gradinaru_claudiu_t@yahoo.com")
# print(obiect1.username)
# print(obiect1.email)
# print(obiect1.password)
# obiect1.password = "A12345678910"
# print(obiect1.password)
# obiect1.password = "1234"
# print(obiect1.password)
# obiect1.password = "12345678910abc"
# print(obiect1.password)