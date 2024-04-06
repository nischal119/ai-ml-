mySet = {1,2,3,4,5,5}

#set must be unique
print(mySet)#

#Only one 5 is printed
#there is no duplicate value in set

#we can append value
mySet.add(6)
# print(mySet)

#sets operation

oneSet = {1,2,3,4,5,6}
otherSet = {4,5,6,7,8,9}
# oneSet.discard(6)

# otherSet.difference_update(oneSet)
print(f'Diffrence is {oneSet.difference(otherSet)}')
print(f'After discarding 6 oneSet becomes {oneSet}')
# print(f'After diffrence updating otherSet becomes {otherSet}')
print(f'Intersection is {oneSet.intersection(otherSet)}')
print(f'Union is  is {oneSet.union(otherSet)}')