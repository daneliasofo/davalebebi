age = int(input("შეიყვანე ასაკი: "))

if age < 5:
    print("უფასოა")
elif age <= 12:
    print("5 ლარი")
elif age <= 17:
    print("8 ლარი")
elif age >= 65:
    print("6 ლარი")
else:
    print("12 ლარი")