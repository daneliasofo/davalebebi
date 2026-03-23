number = int(input("დადებითი რიცხვი: "))

if number < 0:
    print("უარყოფითი რიცხვი არ შეიძლება")
else:
    count = 0

    for i in range(1, number + 1):
        if i % 5 == 0:
            print(i)
            count += 1

    print("5-ის ჯერადი რიცხვების რაოდენობა:", count)