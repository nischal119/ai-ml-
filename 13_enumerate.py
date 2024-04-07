# enumerate and range are similar but emumerate gives us a index of the iterable

for index, item in enumerate("Nischal"):
    print(index, item)


for i, char in enumerate(list(range(0, 100))):
    if char == 50:
        print(i)
