class Creature:
    def __init__(self, name):
        self.name = name

    def say_name(self):
        print("მე ვარ", self.name)


class Wolf(Creature):
    def howl(self):
        print(self.name, "ყმუის")


class Bird(Creature):
    def fly(self):
        print(self.name, "ფრინავს")


w = Wolf("მგელი")
b = Bird("ჩიტი")

w.say_name()
w.howl()

b.say_name()
b.fly()