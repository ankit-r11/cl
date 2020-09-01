class A():
   def __init__(self,var):
       self.var1=var
   def display(self):
       print("value of var1 is ",self.var1)

obj=A(10)
obj.display()

print("check if var1 is availabe ",hasattr(obj,"var1"))
print("check if var2 is availabe ",hasattr(obj,"var2"))

print("value using built in func ", getattr(obj,'var1'))
#print("value using built in func ", getattr(obj,'var2')) ## will throw error,pass third parameter for default value and avoid this error
print("value using built in func ", getattr(obj,'var2',0))
setattr(obj,"var1",11)
setattr(obj,"var2",1)
print("value using built in func ", getattr(obj,'var1'))
print("value using built in func ", getattr(obj,'var2'))

delattr(obj,'var2')
print("value using built in func ", getattr(obj,'var2'))



