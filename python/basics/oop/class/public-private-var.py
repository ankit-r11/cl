class ABC():
    pub_var=10
    __priv_var=11

    def myfunc(self):
        print("public variable within class  ",ABC.pub_var)
        print("public variable within class ",ABC.__priv_var)

obj=ABC()
obj.myfunc()
print("public variable outside func is ",obj.pub_var)
#print("private variable outside func is ",obj.__priv_var)


class DEF():
    def myfunc(self):
        obj=ABC()
        print("pub var from other function is ",obj.pub_var)

obj2=DEF()
obj2.myfunc()
