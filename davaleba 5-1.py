total = 0

while True:
    price = float(input("ფასი: "))

    if price == 0:
        break

    if price < 0:
        print("შეცდომა! ფასი უარყოფითი არ შეიძლება")
        continue

    total += price

print("საერთო ჯამი:", total)

if total > 100:
    discount = total * 0.10
    new_total = total - discount
    print("თქვენ მიიღეთ 10% ფასდაკლება!")
    print("ახალი ჯამი:", new_total)