class Student():
    pass
#定义一个对象
mingyue = Student()

class  PythonStudent():
    name = None
    age = 18
    course = "python"

    def doHomework(self):
        print("I 在写作业")

        #函数末尾使用return none
        return None
yueyue = PythonStudent()
print(yueyue.name)
print(yueyue.age)
yueyue.course

yueyue.doHomework()