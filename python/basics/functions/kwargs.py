## *kwargs (key word argument) treated as dictionary

def display(**kwargs):
    print(kwargs)
    if 'a' in kwargs:
        print(kwargs['a'])

display(a='apple',b='boy')

def myfunc(*args,**kwargs):
    print(args)
    print(kwargs)
    print("i would like to have {} {} ".format(args[1],kwargs['food']))

myfunc(1,2,5,fruit='mango',food='egg')


def myfunc1(str):
    mString=''
    count=0
    for letters in str:
        if count%2==0:
            mString=mString+str[count].upper()
        else:
            mString=mString+str[count].lower()
        count=count+1
    return mString

print(myfunc1('aBc'))
