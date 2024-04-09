def highestEven(*args):
    value = []
    i = 0
    for item in args:
        for i in item:
            if i % 2 == 0:
                value.append(i)

    return value


result = highestEven([1, 2, 10, 20, 21, 24, 11, 30])
print(max(result))


# another method


def even(li):
    evens = []

    for item in li:
        if item % 2 == 0:
            evens.append(item)

    return max(evens)


print(even([1, 2, 10, 15, 24]))
