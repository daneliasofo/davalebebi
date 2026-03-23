class Car:
    manufacturer = "Toyota"   

    def __init__(self, model):
        self.model = model    


c1 = Car("Camry")
c2 = Car("Corolla")
c3 = Car("RAV4")

print(c1.model, Car.manufacturer)
print(c2.model, Car.manufacturer)
print(c3.model, Car.manufacturer)