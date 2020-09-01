
## getter,setter,deleter method must have same name
class sample():
    def __init__(self,var):
        self.__var1=var

    @property
    def getter_setter(self):
        return self.__var1

    @getter_setter.setter
    def getter_setter(self,value):
        self.__var1=value

s=sample(10)

print(s.getter_setter)
s.getter_setter=11
print(s.getter_setter)
