# 1.函数类型注解：给函数的【参数】和【返回值】添加类型说明。
# 2.语法格式：函数名(参数1: 类型, 参数2: 类型) -> 返回值类型:

# 给参数和返回值加类型注解
def add1(x: int, y: int) -> int:
    return x + y


# 带默认值的参数，可以不写注解
def add2(x=1, y=1) -> int:
    return x + y


# 设置多个返回值的类型注解
def show_nums_info(nums: list[int]) -> tuple[int, int, float]:
    max_v = max(nums)
    min_v = min(nums)
    return max_v, min_v, max_v / min_v


# 可变参数类型注解
# 设置 *args 的类型注解，要求 args 中的每个参数都必须是 int 类型
def add(*args: int) -> int:
    return sum(args)

# 设置 **kwargs 的类型注解，要求 kwargs 中的每组参数的值，必须是 str 或 int 类型
def show_info(**kwargs: str | int):
    print(kwargs)

# 获取函数的注解信息
print(add.__annotations__)

