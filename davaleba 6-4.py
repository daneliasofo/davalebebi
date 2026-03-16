pin = 1234
attempts = 5

while attempts > 0:
    user_pin = int(input("შეიყვანე PIN კოდი: "))

    if user_pin == pin:
        print("შესვლა ნებადართულია!")
        break
    else:
        attempts -= 1

        if attempts > 0:
            print("არასწორი PIN! დარჩა", attempts, "მცდელობა")
        else:
            print("ანგარიში დაბლოკილია!")