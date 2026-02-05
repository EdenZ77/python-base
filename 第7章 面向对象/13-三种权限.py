class Person:
    def __init__(self, name, age, idcard):
        self.name = name        # 公有属性：当前类内部、子类内部、类外部，可都可访问
        self._age = age         # 受保护属性：当前类内部、子类内部，可以访问
        self.__idcard = idcard  # 私有属性：仅能在当前类内部访问

    def speak(self):
        # 类的内部，可以访问任何权限的属性（公有属性、受保护属性、私有属性）。
        print(f"我叫：{self.name}，年龄：{self._age}，身份证：{self.__idcard}")

class Student(Person):
    def hello(self):
        # 子类的内部可以访问：公有属性、受保护属性
        print(f"我是学生，我叫：{self.name}，年龄：{self._age}")

p1 = Person('张三', 18, '110101199001011234')
print(p1.name)

# 类的外部，仅能访问公有属性
# 注意：如果在类的外部，强制访问【受保护的属性】，也能访问，但最好别这么做
print(p1._age)

# 强制访问【私有属性】会报错
# print(p1.__idcard)

# 扩展：Python保护【私有属性】的方式，是重命名，例如：__idcard属性，会被重命名为：_Person__idcard
print(p1.__dict__)
print(p1._Person__idcard)

