# 1.包含__call__方法的类，就是类装饰器。
# 2.像调用函数一样，去调用类装饰器的实例对象，就会触发__call__方法的调用。
# 3.__call__方法通常接收一个函数作为参数，并且会返回一个新函数。

def add(x, y):
    res = x + y
    print(f'{x}和{y}相加的结果是{res}')
    return res

### 使用类装饰器（手动装饰）
# 使用类装饰器的流程：先创建类的实例对象，随后调用实例对象，并传入要装饰的函数
# class SayHello:
#     def __call__(self, func):
#         def wrapper(*args, **kwargs):
#             print('你好，我要开始计算了')
#             return func(*args, **kwargs)
#
#         return wrapper
#
# # 使用 SayHello 去装饰 add 函数（手动装饰）
# say = SayHello()
# add = say(add)
# # 调用装饰后的函数
# result = add(10, 20)
# print(result)


### 使用类装饰器（语法糖 @）
# 通过语法糖@使用装饰器时，类名后要加圆括号调用
# class SayHello:
#     def __call__(self, func):
#         def wrapper(*args, **kwargs):
#             print('你好，我要开始计算了')
#             return func(*args, **kwargs)
#         return wrapper
#
# @SayHello()
# def add(x, y):
#     res = x + y
#     print(f'{x}和{y}相加的结果是{res}')
#     return res
#
# # 依然按照原本的方式调用，但调用的是被装饰后的新函数
# result = add(10, 20)
# print(result)


### 带参数的类装饰器
# 带参数的类装饰器写起来，要比带参数的函数装饰器简单，不需要三层嵌套结构
# class SayHello:
#     def __init__(self, msg):
#         self.msg = msg
#
#     def __call__(self, func):
#         def wrapper(*args, **kwargs):
#             print(f'你好，我要开始{self.msg}计算了')
#             return func(*args, **kwargs)
#         return wrapper
#
# @SayHello('加法')
# def add(x, y):
#     res = x + y
#     print(f'{x}和{y}相加的结果是{res}')
#     return res
#
# result = add(10, 20)
# print(result)


### 多个类装饰器一起使用
# 和之前的函数装饰器一样，离函数近的装饰器，先工作。
# 多个类装饰器的使用
# class Test1:
#     def __call__(self, func):
#         def wrapper(*args, **kwargs):
#             print('我是Test1追加的逻辑')
#             return func(*args, **kwargs)
#         return wrapper
#
# class Test2:
#     def __call__(self, func):
#         def wrapper(*args, **kwargs):
#             print('我是Test2追加的逻辑')
#             return func(*args, **kwargs)
#         return wrapper
#
# @Test1()
# @Test2()
# def add(x, y):
#     res = x + y
#     print(f'{x}和{y}相加的结果是{res}')
#     return res
#
# result = add(10, 20)
# print(result)



