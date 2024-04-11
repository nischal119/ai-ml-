# Map
def multiplyBy2(item):
    return item * 2


result = list(map(multiplyBy2, [1, 2, 3, 4]))
print(result)


# filter -> only filters out and returns the condition matching values
def chechOdd(item):
    return item % 2 != 0


onlyOdd = list(filter(chechOdd, [1, 3, 4, 6, 7]))
print(onlyOdd)


# zip
myList = [1, 2, 3]
yourList = [10, 20, 30]

zipped = list(zip(myList, yourList))
print(zipped)


# reduce
from functools import reduce


def accumulator(acc, item):
    print(acc, item)
    return acc + item


print(reduce(accumulator, myList, 0))
