d1={"a":1,'b':2}
#print("dict value is "+ d1['b'])
print(d1['a'])

d2={'c':['a',"b",d1],2:d1}
print(d2['c'][2]['b'])
print(d2[2]['b'])

d1['a']='1-edited'
d1['c']='c-added'
print(d1)

print(type(d1))