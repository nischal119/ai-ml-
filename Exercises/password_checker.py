userName = input("What is your username\n")
password = input("What is your password\n")

secretPassword = '*' * len(password)

print(f'Hey {userName}, Your password is {secretPassword} and it is {len(password)} letters long')