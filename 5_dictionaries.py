# data type and a data structure
#! It is like a object

user = {
'name':'Nischal',
'address':"Pepsicola",

}
#This will not produce any error but it will print none
print(user.get('age'))
#here we can set a default value too if you want

print('Default age is',user.get('age', 22))

print('age' in user)
print('name'in user)

user2 = user.copy()

print('Copied user dictionary is ', user2)

user2.update({'address':'12 Shutter chowk'})
print(f'Updated user2 dictionary {user2}')
