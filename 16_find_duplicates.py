randomList = [1, 2, 3, 1, 2, 4, 5, 6]
duplicates = []
for item in randomList:
    if randomList.count(item) > 1:
        if item not in duplicates:
            duplicates.append(item)


print(duplicates)
