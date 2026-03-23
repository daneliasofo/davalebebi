class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city


p = Person("ლუკა", 20, "თბილისი")


p.age += 1
print("ასაკი:", p.age)

del p.city

try:
    print(p.city)
except AttributeError:
    print("city ატრიბუტი აღარ არსებობს")