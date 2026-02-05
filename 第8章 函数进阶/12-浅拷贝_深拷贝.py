# 赋值语句：b = a ，只是让 b 指向和 a 一样的对象。
# 如果a和b指向的是一个可变对象，那通过b修改后，再通过a访问到的数据也是变化后的。


import copy
a = 666
# a是不可变对象，即便调用deepcopy也不会深拷贝，会直接引用
b = copy.deepcopy(a)

print(id(a))
print(id(b))

import copy
nums1 = (10, 20, 30, (40, 50))
# nums1元组中只包含不可变对象，即便调用deepcopy也不会深拷贝
nums2 = copy.deepcopy(nums1)

print(id(nums1))
print(id(nums2))
