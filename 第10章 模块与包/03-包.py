### 包（Package）概述
# •	包是一种组织模块的方式，包中可以包含：各种模块、子包、其他资源等。
# •	在 Python 中，【包含__init__.py 的文件夹】就是一个包（Package）。
# •	我们通常会把【某个特定功能相关的所有模块】放入一个包中。
# •	使用包可以进一步提升代码的：可维护性、可复用性，便于管理大型项目。


### 包与模块的关系
# •	一个模块就是一个.py文件，包是用来“管理模块”的目录(文件夹)。
# •	一个包中可以有多个模块，也可以有多个子包。


### 包的分类
# Python 中的包分为三类，分别是：标准库包、自定义包、第三方包。


### 1、import 包名.模块名
# import trade.order
# import trade.pay
#
# trade.order.create_order() # 订单创建成功！
# trade.pay.wechat_pay() # 我是微信支付！


### 2、import 包名.模块名 as 别名
# import trade.order as dd
# import trade.pay as zf
#
# dd.create_order()
# zf.wechat_pay()


### 3、from 包名.模块名 import 具体内容1
# from trade.order import max_order_amount, create_order
# from trade.pay import timeout, wechat_pay
#
# print(max_order_amount)
# print(timeout)
# create_order()
# wechat_pay()


### 4、from 包名.模块名 import 具体内容 as 别名
# from trade.order import max_order_amount as max_amt, create_order
# from trade.pay import timeout, wechat_pay as w_pay
#
# print(max_amt)
# print(timeout)
# create_order()
# w_pay()


### 5、from 包名.模块名 import *
# from trade.order import *
# from trade.pay import *
#
# # print(max_order_amount)
# create_order()
# cancel_order()
# show_info()
#
# print(timeout)
# wechat_pay()
# ali_pay()
# show_info()


### 6、from 包名 import 模块名
# from trade import order, pay
#
# order.create_order()
# pay.wechat_pay()


### 7、from 包名 import 模块名 as 别名
# from trade import order as dd, pay as p
#
# dd.create_order()
# p.wechat_pay()


# 关于 __init__.py 文件
# 1.__init__.py 是包的初始化文件，在包被导入时，__init__.py 会被自动调用
# 2.__init__.py 中可以编写一些包的初始化逻辑
# 3.__init__.py 中所定义的内容，会被 from 包名 import * 形式全部引入
# 4.__init__.py 中也可以使用 __all__ 来控制包中的哪些模块可以被 from 包名 import * 引入


### 8、from 包名 import *
# from trade import *
#
# # print(a)
# # print(b)
# print(order.max_order_amount)
# order.create_order()
# print(pay.timeout)
# pay.wechat_pay()


### 9、import 包名
# 注意：想通过import 包名形式进行引入，就必须在__init__.py中定义好具体的内容
# import trade
#
# print(trade.a)
# print(trade.b)
# trade.order.create_order()
# trade.pay.wechat_pay()

