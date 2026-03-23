operations = {
    "გამოკლება": lambda a, b: a - b,
    "გაყოფა": lambda a, b: a / b,
    "ხარისხში": lambda a, b: a ** b
}

print(operations["გამოკლება"](20, 4))
print(operations["გაყოფა"](20, 4))
print(operations["ხარისხში"](20, 4))