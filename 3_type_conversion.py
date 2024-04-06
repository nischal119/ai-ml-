from datetime import datetime

birth_year = input ("What is your birth year \n")

current_year = datetime.today().year
age =current_year - int(birth_year)

print(f'Your age is {age}')