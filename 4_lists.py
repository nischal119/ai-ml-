# List are the forrm of array
# List is a data structure

li=[1,2,4]
li2= ['a','b']
li3=[1,2,4,True,'a']

#Unlike strings lists are mutable

darazCart= ["Monitor","Monitor stand","Iphone"]

darazCart[0]= "JBL SoundBar"

# newCart = darazCart

# If we do this we will modify the darazCart too . This means modifying in list
# But instead if we do this we will copy the list

newCart = darazCart[:] # This means copying 
newCart[0]= "Fridge"
print(newCart)
print(darazCart)

#List methods

#append
myList = [1,2,3,4,5]
myList.append(100)
print('----------------------Append-------------------')
print(myList)

#insert
myList.insert(1,200)
print('-----------------------Insert-------------------')
print(myList)

#extend
myList.extend([100,101,102])
print('------------------------Extend------------------')
print(myList)

#!pop=> returns the popped value
myList.pop()
print("------------------------Pop---------------------")
print(myList)
#!remove => doesnot return anything
myList.remove(101)
print("------------------------Remove-------------------")
print(myList)

#clear
myList.clear()
print("------------------------Clear---------------------")
print(myList)

#index searching
indexList = ['a','b','c','a','a']
print("--------------------Index Searching---------------")
print(indexList.index('c', 0,3)) #! search from 0 index to index 2

#better way to avoid errors

print("--------------------Searching using in---------------")
print('a' in indexList)

#count
print("----------------------------Count--------------------")
print(indexList.count('a'))

#range
print("----------------------------Range--------------------")
print(list(range(1,11)))

#Join
sentence = ' '
newSentence = sentence.join(['Hi','my','name','is','Nischal'])
print("----------------------------Join--------------------")
print(newSentence)

#List unpacking

a,b,c, *other= [1,2,3,4,5,6,7,8,9]
print("----------------------------List unpacking --------------------")
print(a)
print(b)
print(c)


print(other)