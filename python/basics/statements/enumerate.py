## purpose of enumerta eis to accomplish following
#types of tasks, to keep track of index count

word="letter"
count=0
for letter in word:
    print(word[count])
    count+=1

#with enumerate it can be done
#it retyrn tuples,enumerate can take any iterable object

for item in enumerate(word):
    print(item)
## so tuples expansion can be used like
for index,value in enumerate(word):
     print(index)
     print(value)
     print("\n")



