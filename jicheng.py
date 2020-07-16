# import jicheng1
# python支持多继承
from jicheng1 import person
class student(person):
    # sum = 0
    # def __init__(self):
    #     self.name = name
    #     self.age = age
    #     self.__score = 0
    #     self.__class__.sum += 1
    def __init__(self,school,name,age):
        # person.__init__(self,name,age)
        super(student, self).__init__(name,age)
        self.school = school
    def homework(self):
        # super(student, self).homework()
        print("do homework")
# s1 = student("xiaoa",19,'jingying')
s1 = student("jingying",'wwwww',12)
print(s1.sum)
print(student.sum)
print(s1.name)
print(s1.age)
print(s1.school)
# print(s1.getname())
s1.getname()
