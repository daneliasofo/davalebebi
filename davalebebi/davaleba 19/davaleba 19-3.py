class Device:
    def __init__(self, brand):
        self.brand = brand


class Phone(Device):
    def __init__(self, brand, model):
        super().__init__(brand)  
        self.model = model


p = Phone("iphone", "17")

print(p.brand, p.model)