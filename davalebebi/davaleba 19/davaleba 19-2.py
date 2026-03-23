class Employee:
    def __init__(self, name, position, salary):
        self.name = name          
        self._position = position
        self.__salary = salary    

    def show_salary(self, code):
        if code == "1234":
            print("ხელფასი:", self.__salary)
        else:
            print("არასწორი კოდი")


e = Employee("გიორგი", "მენეჯერი", 3000)

e.show_salary("0000")
e.show_salary("1234")