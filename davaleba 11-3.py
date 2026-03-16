data = [1, 2, 3, 4, 5]

reversed_list = []

for i in range(len(data) - 1, -1, -1):
    reversed_list.append(data[i])

print(reversed_list)