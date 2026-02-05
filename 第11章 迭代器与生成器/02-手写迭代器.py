### 迭代器是一次性的，状态只会向前推进，且不会自动重置（迭代器在遍历的过程中会被“消耗”）。
names = ['张三', '李四', '王五']
it1 = iter(names)
it2 = iter(names)

print(it1)
print(it2)

# print(next(it1))
# print(next(it1))
# print(next(it1))
# print(next(it1)) # 此行代码会抛出异常，因为此时迭代器已经被耗尽了

# 如想重新依次获取元素，需要使用新的迭代器it2
# print(next(it2))
# print(next(it2))
# print(next(it2))

for item in it1:
    print(item)

for item in it1:
    print(item)


##############################需求：让for循环可以遍历Person的实例对象。