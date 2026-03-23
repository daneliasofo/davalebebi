class Animal:
    def sound(self):
        print("ცხოველი გამოსცემს ხმას")


class Dog(Animal):
    def sound(self):
        super().sound()     
        print("ძაღლი ყეფს ")


d = Dog()
d.sound()