def superFunction(*args, **kwargs):
    total = 0
    for item in kwargs.values():
        total += item

    return sum(args) + total


print(superFunction(1, 2, 3, 4, 5, num1=5, num2=10))
