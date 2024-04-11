simpleDictionary = {"a": 2, "b": 4, "c": 3}

myDictionary = {
    key: value**2 for key, value in simpleDictionary.items() if value % 2 == 0
}
print(myDictionary)
