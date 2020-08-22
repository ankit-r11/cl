##Zip is opposite of enumerate function, it zips the two list and retun list of tuples

list1=[1,2,3]
list2=['a','b','c']
list3=['d','e']
#Note: Zip returns tuples of size shortest list

zipped=zip(list1,list2,list3)
print(zipped)


for item in zipped:
    print(item)


##to get list cast into list

print(list(zipped))