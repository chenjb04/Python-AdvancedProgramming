a = 1
print(type(1))
print(type(int))
# type->int->1
# type->class->obj
# object是最顶层的基类，type是类型关系的顶端，所有的对象都是它的实例
# type是一个类，同时type也是一个对象
# object和type都是type的一个实例
# type继承自object

print(type(object))
print(object.__bases__)
print(type.__bases__)


class Student:
    pass


stu = Student()
print(type(stu))
print(Student.__bases__)  # 查看类的基类

