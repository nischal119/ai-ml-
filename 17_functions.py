def sayHello(name="user", age="not defined"):
    print(f"Hello {name}, your age is {age}")


usetrName = input("What is your name:")
userAge = input("What is you age")

# This is called a positional argument..Position matters here
sayHello(usetrName, userAge)

# Keyword argument  . This is bad practice
sayHello(
    age=userAge,
    name=usetrName,
)
# This is a doc string and used to give some info about the function. We can see this info on the hilight while we are calling this function
"""
Info:This function has a defualt parameter.
"""


secondUsername = ""
secondUserAge = 21

# we also have default arguments
sayHello(secondUserAge)

# invoking default parameters
sayHello()
