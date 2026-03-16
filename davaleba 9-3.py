students = ["გიორგი", "ნინო", "დავითი", "მარიამი", "ლუკა"]
grades = [85, 90, 78, 92, 88, 76, 95, 89]


print("students სიგრძე:", len(students))
print("ბოლო სტუდენტი:", students[len(students) - 1])
print("ბოლოდან მეორე:", students[len(students) - 2])

print("მე-3 ქულა:", grades[2])
print("ბოლო ქულა:", grades[-1])

grades[0] = 100
print("შეცვლილი grades:", grades)

print("საშუალო 4 ქულა:", grades[2:6])
print("ყველა გარდა პირველი 2-ის:", grades[2:])


print("grades სიგრძე:", len(grades))
print("მაქსიმალური:", max(grades))
print("მინიმალური:", min(grades))
print("ჯამი:", sum(grades))