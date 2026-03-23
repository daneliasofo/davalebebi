check_number = lambda x: "დადებითი" if x > 0 else ("უარყოფითი" if x < 0 else "ნული")

print(check_number(-5))
print(check_number(0))
print(check_number(7))