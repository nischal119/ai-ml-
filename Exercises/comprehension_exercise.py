someList = [1, 2, 3, 4, 5, 1, 2, 3]


duplicates = list(set([numbers for numbers in someList if someList.count(numbers) > 1]))
print(duplicates)

# Comprehension
