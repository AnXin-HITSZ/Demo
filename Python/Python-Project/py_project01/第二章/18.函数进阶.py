# ---------------------------- 函数 - 变量的作用域 ----------------------------
# # 全局变量：在函数外部或函数的内部都是可以访问的
# num = 100
#
# # 定义函数
# def circle_area(r):
#     # 局部变量：只能在函数内部使用
#     pi = 3.14
#     area = pi * r * r
#
#     global num
#     num = 10000
#     print("num = ", num)    # 10000
#
#     return area
#
# # 调用函数
# c_area = circle_area(10)
# print(c_area)
#
# print("num = ", num)    # 10000


# ---------------------------- 函数 - 传参方式 ----------------------------
# # 定义函数
# def reg_stu(name, age, gender, city):
#     print(f"注册成功，姓名：{name}，年龄：{age}，性别：{gender}，城市：{city}")
#     return {"name": name, "age": age, "gender": gender, "city": city}
#
# # 传参方式一：位置参数
# stu = reg_stu("name_1", "age_1", "gender_1", "city_1")
# print(stu)
#
# # 传参方式二：关键字参数
# stu = reg_stu(name="name_2", age="age_2", gender="gender_2", city="city_2")
# print(stu)
#
# stu = reg_stu(age="age_3", gender="gender_3", city="city_3", name="name_3")
# print(stu)
#
# # 传参方式三：位置参数 + 关键字参数 -> 位置参数在前，关键字参数在后
# stu = reg_stu("name_4", "age_4", gender="gender_4", city="city_4")
# print(stu)

# ---------------------------- 函数 - 默认参数 ----------------------------
# # 定义函数
# def reg_stu(name, age, gender="default_gender", city="default_city"):
#     print(f"注册成功，姓名：{name}，年龄：{age}，性别：{gender}，城市：{city}")
#     return {"name": name, "age": age, "gender": gender, "city": city}
#
# # 调用函数
# stu = reg_stu("name", "age")
# print(stu)
#
# stu = reg_stu("name", "age", "gender")
# print(stu)
#
# stu = reg_stu("name", "age", city="city")
# print(stu)


# ---------------------------- 函数 - 不定长参数（位置参数 *args -> 元组） ----------------------------
# # 需求：根据传入的这批数据，计算这批数据的最小值、最大值、平均值
# def calc_data(*args):
#     min_data = min(args)
#     max_data = max(args)
#     avg_data = sum(args) / len(args)
#     return min_data, max_data, round(avg_data, 1)
#
# # 调用函数
# print(calc_data(2, 7, 9, 10, 45))
#
# print(calc_data(2, 7, 9, 10, 45, 73, 37, 93, 92, 111, 222))

# ---------------------------- 函数 - 不定长参数（关键字参数 **kwargs -> 字典） ----------------------------
# # 需求：根据传入的这批数据，计算这批数据的最小值、最大值、平均值
# def calc_data(*args, **kwargs):
#     """
#     根据传入的这批数据，计算这批数据的最小值、最大值、平均值
#     :param args: 不定长位置参数，需要计算的这批数据
#     :param kwargs: 不定长关键字参数
#         round: 保留的小数位个数
#         print: 是否打印输出
#     :return: 最小值、最大值、平均值
#     """
#     min_data = min(args)
#     max_data = max(args)
#     avg_data = sum(args) / len(args)
#
#     if kwargs.get("round") is not None:
#         avg_data = round(sum(args) / len(args), kwargs.get("round"))
#
#     if kwargs.get("print"):
#         print(f"计算出来的最小值：{min_data}，最大值：{max_data}，平均值：{avg_data}")
#
#     return min_data, max_data, avg_data
#
# # 调用函数
# # print(calc_data(2, 7, 9, 10, 45, round=3, print=True))
#
# print(calc_data(2, 7, 9, 10, 45, 73, 37, 93, 92, 111, 222, round=4, print=True))


# ---------------------------- 函数的参数类型 ----------------------------
# # 加
# def add(x, y):
#     return x + y
#
# # 减
# def subtract(x, y):
#     return x - y
#
# # 乘
# def multiply(x, y):
#     return x * y
#
# # 除
# def divide(x, y):
#     return x / y
#
# # 计算
# def calc(x, y, oper):
#     return oper(x, y)
#
# print(calc(10, 20, multiply))


# ---------------------------- 匿名函数 ----------------------------
# # 需求 1：打印一条分割线
# # def out_line():
# #     print("-----------------------------")
#
# out_line = lambda : print("-----------------------------")
# out_line()
#
# # 需求 2：计算两个数之和
# # def add(x, y):
# #     return x + y
#
# add = lambda x, y: x + y
# print(add(100, 200))
#
# # 需求 3：完成如下列表的排序操作，按照每一个元素的字符个数，从小到大排序
# data_list = ["C++", "C", "Python", "PHP", "Java", "Go", "JavaScript", "Rust"]
# print(data_list)
#
# data_list.sort(key=lambda item: len(item))  # 匿名函数典型的应用场景
# print(data_list)


# ---------------------------- 案例 ----------------------------
# 案例 1：计算 n 的阶乘
# # 递归调用（先层层递进，再逐层回归）：指的是在函数中自己调用自己的情况 -> 一定得有终结点
# """
# function(10) = 10 * function(9) = ...
# function(9) = 9 * function(8) = ...
# function(8) = 8 * function(7) = ...
# function(7) = 7 * function(6) = 7 * 720 = 5040
# function(6) = 6 * function(5) = 6 * 120 = 720
# function(5) = 5 * function(4) = 5 * 24 = 120
# function(4) = 4 * function(3) = 4 * 6 = 24
# function(3) = 3 * function(2) = 3 * 2 = 6
# function(2) = 2 * function(1) = 2 * 1 = 2
# function(1) = 1
# """
#
# def function(n):
#     if n == 1:
#         return 1
#     else:
#         return n * function(n - 1)
#
# result = function(10)
# print(result)


"""
案例 2：
    定义一个用于根据传入的一批商品信息（商品名、价格、数量）、优惠（优惠券、积分抵扣）、运费信息计算订单的总金额的函数
    具体规则如下：
        1. 优惠券需要商品金额满 5000 才可以使用，且优惠券金额不能超过商品总价
        2. 积分抵扣需要商品总金额满 5000 才可以使用，100 积分抵扣 1 元（且抵扣金额不能超过商品总价，积分只能整百抵扣）
"""
def calc_order_cost(*args, coupon=0, score=0, express=0.0):
    """
    根据传入的一批商品信息（商品名、价格、数量）、优惠（优惠券、积分抵扣）、运费信息计算订单的总金额
    :param args: 商品信息（商品名、价格、数量）
    :param coupon: 优惠券
    :param score: 积分
    :param express: 运费
    :return: 订单的总金额
    """
    # 订单的总金额 = 商品总金额 - 优惠券 - 积分抵扣 + 运费
    # 1. 计算商品总金额
    total_price = [goods[1] * goods[2] for goods in args]
    total_cost = sum(total_price)

    # 2. 扣减优惠券
    if total_cost >= 5000 and coupon <= total_cost:
        total_cost -= coupon

    # 3. 扣减积分抵扣
    if total_cost >= 5000 and score // 100 <= total_cost:
        total_cost -= score // 100

    # 4. 添加运费
    total_cost += express

    return total_cost

# 测试
# total = calc_order_cost(("good_1", 188, 2), ("goods_2", 388, 1), ("goods_3", 3999, 1), coupon=10, score=4000, express=9.9)
# print(total)

# total = calc_order_cost(("good_1", 188, 2), ("goods_2", 388, 1), ("goods_3", 6999, 1), coupon=10, score=4000, express=9.9)
# print(total)

# total = calc_order_cost(("good_1", 188, 2), ("goods_2", 388, 1), ("goods_3", 6999, 1), express=9.9)
# print(total)

total = calc_order_cost(("good_1", 188, 2), ("goods_2", 388, 1), ("goods_3", 6999, 1))
print(total)
