firstList = [char for char in "Nischal"]
print(f"first list {firstList}")

secondList = [num for num in range(1, 10)]
print(f"second list {secondList}")

thirdList = [num**2 for num in range(1, 10)]
print(f"Third List {thirdList}")

fourthList = [num**2 for num in range(1, 10) if num % 2 == 0]
print(f"Fourth list {fourthList}")
