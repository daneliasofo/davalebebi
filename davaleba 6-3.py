N = int(input("რიცხვი: "))

even = 0
odd = 0

for i in range(1, N + 1):
    if i % 2 == 0:
        even += 1
    else:
        odd += 1

print("ლუწი:", even)
print("კენტი:", odd)