collection=[1,2,3,4,5]
for i in collection:
    print(i)

print("printing only even umbers from list")

collection=[1,2,3,4,5,6,7,8,9,10]
for i in collection:
    if i%2==0:
        print(i)


for letter in 'python':
    print(letter)

collection=[(1,2,8),(3,4),(5,6),(7,8)]

for i in collection:
    print(i)
    

for i in collection:
    for j in i:
        print(j)

collection={'a':1,'b':2,'c':3,'d':4}
for i in collection:
    #iterator on dict return only key, to get value
    #do something like this or use unpacking feature of tuples
    print(i)
    print(collection[i])

#to use unpacking for dict use dict methods on iterable
for i,j in collection.items():
    print(j)

