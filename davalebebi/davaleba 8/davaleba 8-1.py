for i in range(1, 11):
    for j in range(1, 11):
        result = i * j
        if result % 2 == 0:  
            print(result, end=' ')
    print()