'''
定义一个学生类，用来形容学生
'''
# 定义一个空的类
class Student():
    # 一个空类，pass直接跳过
    # 此处pass必须有
    pass

# 定义一个对象
wei = Student()

#　再定义一个类，用来描述Ｐython的学生
class PythonStudent():
    #用None给不确定的值赋值
    name = None
    age = 18
    course = "Python"

    # 需要注意
    #　１．def　doHomework的缩进层级
    #　２．系统默认由一个self函数
    def doHomework(self):
        print("做作业")

        # 推荐在函数末尾使用return语句
        return None

#　实例化一个叫wei的学生，是一个具体的人
wei = PythonStudent()
print(wei.name)
print(wei.age)
#注意成员函数的调用没有传递进入参数
wei.doHomework()