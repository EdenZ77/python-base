# 一、函数的多返回值
# def calculate(x, y):
#     res1 = x + y
#     res2 = x - y
#     return res1, res2 # 实际返回的是：(res1, res2)
#
# result = calculate(10, 20)
# r1, r2 = calculate(10, 20)
#
# print(result)  # (30, -10)
# print(r1)      # 30
# print(r2)      # -10



# 二、参数的打包与解包
# 打包接收参数：
# *args    ：打包所有的位置参数（会形成一个元组）
# **kwargs ：打包所有的关键字参数（会形成一个字典）
def show_info(*args, **kwargs):
    print(args)
    print(kwargs)
show_info(10, 20, 30, name='张三', age=18)

nums = (10, 20, 30)
person = {'name': '张三', 'age': 18}

# 解包传递参数：
# *nums    ：将元组拆解成一个一个独立的位置参数
# **person ：将字典拆解一个一个 key=value 形式的关键字参数
show_info(*nums, **person)

