a = int(input("პირველი რიცხვი: "))
b = int(input("მეორე რიცხვი: "))

total = 0

for i in range(a, b + 1):
    if i % 2 == 0:
        total += i

print("ლუწი რიცხვების ჯამი:", total)