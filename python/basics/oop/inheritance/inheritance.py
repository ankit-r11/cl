# class DerivedClass(baseClass):
#     class_body

class Person():
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.__priv_name=name+"secret"
        self.name_2="_2"
    def display(self):
        print("name is {} and age is {}".format(self.name,self.age))
    @property
    def name_priv(self):
        return self.__priv_name

    

class Teacher(Person):
    def __init__(self,name1,age,experience,teaching_area):
        Person.__init__(self,name1,age)
        self.experience=experience
        self.teaching_area=teaching_area

    def displayData(self):
        Person.display(self)
        print("experience is {} and teaching_area is {}".format(self.experience,self.teaching_area))
    
class Student(Person):
    def __init__(self,name,age,course,marks):
        Person.__init__(self,name,age)
        self.course=course
        self.marks=marks

    def displayData(self):
        Person.display(self)
        print("course is {} and marks is {}".format(self.course,self.marks))

person=Person("abc",25)
person.display()
print("#########################")
teacher=Teacher("def",24,5,"Math")
teacher.display()
teacher.displayData()
print("#########################")
student=Student("ghi",24,"Science",98)
student.displayData()
student.display()

print ("***************")
print("accessing public variable of base class ",student.name_priv)





