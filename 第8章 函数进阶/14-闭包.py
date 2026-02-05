# 前置知识 1： 局部作用域的生命周期。
# •	每次调用函数时，都会创建一个新的局部作用域。
# •	函数执行完毕后，该作用域就会被销毁，其中的局部变量，也会随之释放。
# def outer():
#     num = 10
#     num += 1
#     print(num)
#
# outer() #11
# outer() #11
# outer() #11



# 前置知识 2：内层函数访问外层变量。
# •	【内层函数】可以访问到【外层函数】作用域中的变量。
# •	访问外层变量不用nonlocal，修改外层变量时要使用nonlocal。
# def outer():
#     num = 10
#     def inner():
#         print(num)
#     inner()
# outer()

# 如下代码验证了：理论上num变量应该在outer函数调用完销毁，但实际并没有。
# def outer():
#     num = 10
#     def inner():
#         print(num)
#     inner()
# outer()



# • 闭包 = 内层函数 + 被内层函数引用的外层变量。
# • 产生闭包的三个条件如下：
# 1.必须有函数嵌套
# 2.内层函数使用了外层函数的变量
# 3.外层函数返回内层函数

# 我们在inner函数中不仅要打印num，还要去修改num（修改时记得加上nonlocal num）。
# 最终发现：num的值居然还可以一直增加，所以截至目前，证明了一件事：本应该随着outer函数调用结束而死去的num，并没有死去，
# 并且inner函数依然可以对num进行读取和修改。所以我们观察如下的代码形式，完全符合上述的闭包产生条件，所以此时就出现了闭包。
# def outer():
#     num = 10
#     def inner():
#         nonlocal num
#         num += 1
#         print(num)
#     return inner
#
# f = outer()
# f() # 11
# f() # 12
# f() # 13


# 外层变量会被保存到 闭包单元（cell）中，例如下面代码中，那些被 inner函数所使用到的outer函数中的局部变量，
# 会被封存在闭包单元（cell） 中，这些cell组成一个 __closure__ 元组，保存在了inner函数上。
# def outer():
#     num = 10
#     print(id(num)) # 140707460170952
#
#     def inner():
#         nonlocal num
#         num += 1
#         print(num)
#
#     return inner
#
# f = outer()
# print(f.__closure__) # __closure__的值是一个元组，元组中保存着被inner函数所“挽救”下来的数据
# print(f.__closure__[0].cell_contents) # 10
# print(id(f.__closure__[0].cell_contents)) # 140707460170952


# 思考：内层函数inner会保存外层函数outer中所有的数据吗？ 不会，只会保存inner中所用到的。
# def outer():
#     num = 10
#     msg = '你好啊！'
#     print(msg)
#
#     def inner():
#         nonlocal num
#         num += 1
#         print(num)
#
#     return inner
#
# f = outer()
# print(f.__closure__) # 发现__closure__中只有num，没有msg


### 注意点
# 1、每次获得一个新闭包，互不影响（闭包之间是互相独立的）。
# def outer():
#     num = 10
#
#     def inner():
#         nonlocal num
#         num += 1
#         print(num)
#
#     return inner
#
# f1 = outer()
# f1()
# f1()
# f1()
# print('*****************')
# f2 = outer()
# f2()


# 2、外层变量为可变对象时仍互不影响。
def outer():
    nums = []

    def inner(value):
        nums.append(value)
        print(nums)

    return inner

# 每次调用 outer() 都创建一个新的 nums
f1 = outer()
f1(10)
f1(20)
f1(30)
print('**********************')
f2 = outer()
f2(666)



