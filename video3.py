# class Parent1(object):
#     pass
#
# class Parent2(object):
#     pass
#
# class Child1(Parent1):  # 单继承
#     pass
#
# class Child2(Parent1, Parent2):  #多继承
#     pass
#
#
# print(Child1.__bases__)
# print(Child2.__bases__)

# class Human:
#     star = 'earth'
#
#     def __init__(self, name, age, gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
#
#
# class American(Human):
#     # star = 'earth'
#     nation = 'America'
#
#     def speak_english(self):
#         print(f'{self.name}我在说英语')
#         print(f'{self.name}我在说英语')
#
#
# class Chinese(Human):
#     # star = 'earth'
#     nation = 'China'
#
#     def __init__(self, name, age, gender, balance):
#         # Human.__init__(self, name, age, gender)
#         super(Chinese, self).__init__(name, age, gender)
#         self.balance = balance
#
#     def speak_chinese(self):
#         print(f'{self.name}我在说普通话')

#
#
#
#
# dy_obj = Chinese('董永', 18, '男')
# print(dy_obj.__dict__)
# print(dy_obj.nation)
#
# iron_man_obj = American('iron_man', 19, '男')
# print(iron_man_obj.__dict__)
# print(iron_man_obj.nation)
# print(iron_man_obj.star)
# iron_man_obj.speak_english()


# 属性查找
# 对象-类-父类-。。。 object

# class Test1:
#     def f1(self):
#         print('Test1.f1')
#
#     def f2(self):
#         print('Test1.f2')
#         self.f1()
#
#
# class Test2(Test1):
#     def f1(self):
#         print('Test2.f1')
#
#
# obj = Test2()
# obj.f2()


# class Car:
#     def run(self):
#         print('开始跑',end=' ')
#
# class Benz(Car):
#     def run(self):
#         super().run()
#         print('加98号汽油')
#
# class Lx(Car):
#     def run(self):
#         super().run()
#         print('充电')
#
# class Auto(Car):
#     def run(self):
#         super().run()
#         print('加92号汽油')
#
# car1 = Benz()
# car2 = Lx()
# car3 = Auto()
# car1.run()
# car2.run()
# car3.run()
# def drive_car(Car):
#     Car.run()
#
# drive_car(car1)
# drive_car(car2)
# drive_car(car3)


import abc  # abstract method


class Car(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def run(self):
        pass

class Benz(Car):
    pass

class Lx(Car):
    pass


class Auto(Car):
    pass

car1=Benz()