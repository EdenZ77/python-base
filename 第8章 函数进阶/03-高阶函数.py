# 当一个函数的『参数是函数』或者『返回值是函数』那该函数就是『高阶函数』。

# 高阶函数的意义：
# 1.代码复用性高：可以把行为“独立出去”，传入不同函数实现不同逻辑。
# 2.能让函数更灵活，更通用。
# 3.高阶函数是：装饰器、闭包的基础。（后面会讲）

def welcome():
    print('你好啊！')
# caller函数的参数是函数，所以caller是高阶函数
def caller(f):
    print('call函数开始调用')
    f()
caller(welcome)


# outer函数的返回值是函数，所以outer函数是高阶函数
def outer():
    print('我是outer')

    def inner():
        print('我是inner')
    return inner

