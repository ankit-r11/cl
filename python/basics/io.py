myfile=open('basics.txt')
print(myfile.read())
print(myfile.read())
myfile.seek(0)
print(myfile.read())

myfile.seek(10)

print(myfile.read())

with open('basics.txt') as myfile_1:
     content=myfile_1.read()

print("conetent is::::  "+content)