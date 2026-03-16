a = [1, 2, 3, 4, 5]
b = [3, 4, 5, 6, 7]

common = []

for x in a:
    if x in b:
        common.append(x)

print("საერთო:", common)
print("ჯამი:", sum(common))