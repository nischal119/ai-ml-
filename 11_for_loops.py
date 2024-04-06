for multiplicant in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    for multiplier in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
        print(f"{multiplicant} * {multiplier} = {multiplicant * multiplier} ")
    print("\n")

myself = {"name": "Nischal", "age": 21, "Address": "Pepsicola"}
for item in myself:
    print(item)


for key, value in myself.items():
    print(key, value)


for item in myself.keys():
    print(item)


for item in myself.values():
    print(item)
