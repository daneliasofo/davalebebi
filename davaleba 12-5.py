original = (1, 2, 3, 4, 5)

new_tuple = tuple(x * 2 for x in original)

new_tuple = new_tuple + (100,)   

print(new_tuple)