class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade


s1 = Student("გიორგი", 80)
s2 = Student("ნინო", 90)


print(s1.name, s1.grade)
print(s2.name, s2.grade)

s1.grade += 5

print("გაზრდის შემდეგ:", s1.name, s1.grade)