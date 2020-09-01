class A():
    pub_var=1
    __priv_var=2
    def pub_meth(self):
         print("This is a public method ")
         print("from pub function pub var is {} and priv var is {}".format(A.pub_var,A.__priv_var))
         print("calling private method..")
         self.__priv_method()

    def __priv_method(self):
        print("This is a public method ")
        print("from priv function pub var is {} and priv var is {}".format(A.pub_var,A.__priv_var))


obj=A()
obj.pub_meth()  
## to call a private method use obj._classname__methodname
obj._A__priv_method()        


