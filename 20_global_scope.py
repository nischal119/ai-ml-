total = 0


def sum():

    global total  # refer to global scope
    total += 1
    return total


sum()
sum()
sum()
sum()
print(sum())
