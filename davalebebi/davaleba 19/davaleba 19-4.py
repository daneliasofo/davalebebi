class Student:
    def __init__(self):
        self.__grade = 0

    def set_grade(self, value):
        if 1 <= value <= 10:
            self.__grade = value
        else:
            print("1-დან 10-მდე")

    def get_grade(self):
        return self.__grade


s = Student()

s.set_grade(8)
print(s.get_grade())

s.set_grade(15)  