total = 0

while True:
    number = float(input("რიცხვი: "))

    if number == 0:
        break

    if number > 0:
        total += number

print("დადებითი რიცხვების ჯამი:", total)