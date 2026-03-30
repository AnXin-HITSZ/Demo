# ---------------------------- 列表操作 ----------------------------
# # 定义列表
# s = [56, 90, 88, 65, 90, "A", "Hello", True]
#
# print(type(s))
#
# # 访问列表元素
# # 获取
# print(s[0]) # 正向索引，从 0 开始
# print(s[-8])    # 反向索引，从 -1 开始
#
# print(s[2])
# print(s[-6])
#
# # 修改
# s[5] = "ABC"
# print(s)
#
# # 注意：如果指定的索引超出范围，将会报错 list assignment index out of range
# # s[10] = "DEF"
# # print(s)
#
# # 删除
# del s[6]
# print(s)
#
# # 遍历
# for item in s:
#     print(item)


# ---------------------------- 列表 list 切片 ----------------------------
# # 定义列表
# s = ["A", "C", "H", "K", "L", "B", "D", "X", "C", "U"]
#
# # 切片操作 s[开始索引:结束索引:步长]
# print(s[0:5:1])
# print(type(s[0:5:1]))
#
# print(s[:5:1])
# print(s[:5:])
# print(s[:5])
#
# print(s[0:5:2])
# print(s[0:-2:1])


# ---------------------------- 列表 list 常用方法 ----------------------------
# # 列表定义
# s = [56, 90, 88, 65, 90, 100, 209, 72, 145]
# print(s)
#
# # append()：在列表尾部追加元素
# s.append(188)
# print(s)
#
# # insert()：在指定索引之前，插入元素
# s.insert(2, 80)
# print(s)
#
# # remove()：移除列表中第一个匹配到的元素
# s.remove(90)
# print(s)
#
# # pop()：删除列表中指定索引位置的元素并返回（如果未指定，默认删除最后一个）
# e = s.pop(1)
# print(e)
#
# e = s.pop()
# print(e)
#
# print(s)
#
# # sort():排序
# s.sort()
# print(s)
#
# # reverse()：反转列表元素
# s.reverse()
# print(s)


# ---------------------------- 列表 list 案例 ----------------------------
# 案例 1：将用户输入的 10 个数字，存储到一个列表中，并将列表中的数字进行排序，输出其中的最小值、最大值和平均值
#
# # 1. 定义列表
# num_list = []
#
# # 2. 将用户输入的 10 个数字存入列表
# for i in range(10):
#     num = int(input("请输入一个有效的数字："))
#     num_list.append(num)
#
# print("数字列表：", num_list)
#
# # 3. 排序
# num_list.sort()
# print("排序后的数字列表：", num_list)
#
# # 4. 输出其中的最小值、最大值和平均值
# print("最小值：", num_list[0])
# print("最大值：", num_list[-1])
# print("平均值：", sum(num_list) / len(num_list))    # sum() 求和，len() 获取元素的个数（列表的长度）

# 案例 2：合并两个列表中的元素，并对合并的结果进行去重处理（去除列表中的重复元素）
# num_list1 = [19, 23, 54, 64, 875, 20, 109, 232, 123, 54]
# num_list2 = [55, 80, 72, 35, 60, 123, 54, 29, 91]
#
# # 1. 合并列表
# for num in num_list2:
#     num_list1.append(num)
#
# print("合并后的原始列表：", num_list1)
#
# # 2. 去重重复记录
# new_list = []   # 去重重复记录后的列表
#
# for num in num_list1:
#     # 判断 new_list 中是否存在 num 元素，如果不存在，再添加
#     if num not in new_list: # 判断元素是否存在于列表中，如果存在则返回 True，如果不存在则返回 False
#         new_list.append(num)
#
# print("去重重复记录后的列表：", new_list)

# 案例 2（简化）：合并两个列表中的元素，并对合并的结果进行去重处理（去除列表中的重复元素）
# num_list1 = [19, 23, 54, 64, 875, 20, 109, 232, 123, 54]
# num_list2 = [55, 80, 72, 35, 60, 123, 54, 29, 91]
#
# # 1. 合并列表
# # 解包：将列表这一类容器解开成一个一个独立的元素
# # 组包：将多个值合并到一个容器
# num_list = [*num_list1, *num_list2]
#
# print("合并后的原始列表：", num_list)
#
# # 2. 去重重复记录
# new_list = []   # 去重重复记录后的列表
#
# for num in num_list:
#     # 判断 new_list 中是否存在 num 元素，如果不存在，再添加
#     if num not in new_list: # 判断元素是否存在于列表中，如果存在则返回 True，如果不存在则返回 False
#         new_list.append(num)
#
# print("去重重复记录后的列表：", new_list)

# 案例 2（简化）：合并两个列表中的元素，并对合并的结果进行去重处理（去除列表中的重复元素）
# num_list1 = [19, 23, 54, 64, 875, 20, 109, 232, 123, 54]
# num_list2 = [55, 80, 72, 35, 60, 123, 54, 29, 91]
#
# # 1. 合并列表
# num_list = num_list1 + num_list2
# print("合并后的原始列表：", num_list)
#
# # 2. 去重重复记录
# new_list = []   # 去重重复记录后的列表
#
# for num in num_list:
#     # 判断 new_list 中是否存在 num 元素，如果不存在，再添加
#     if num not in new_list: # 判断元素是否存在于列表中，如果存在则返回 True，如果不存在则返回 False
#         new_list.append(num)
#
# print("去重重复记录后的列表：", new_list)


# 案例 3：生成 1 - 20 的平方列表 -> range(1, 21)

# 方式一：传统方式
# num_list = []
# for i in range(1, 21):
#     num_list.append(i ** 2)
#
# print(num_list)

# 方式二：列表推导式 -> 按照一定的规则快速生成一个列表的方法 -> 语法格式 1：[要插入的值 for i in 序列/列表]
# num_list = [i ** 2 for i in range(1, 21)]
# print(num_list)


# 案例 4：从一个数字列表中提取所有偶数，并计算其平方，组成一个新的列表 -> 判断偶数：num % 2 == 0
# 列表推导式 -> 按照一定的规则快速生成一个列表的方法 -> 语法格式 2：[要插入的值 for i in 序列/列表 if 条件]
num_list = [12, 32, 45, 77, 80, 92, 33, 57, 97, 98, 110, 111, 122]
new_list = [i ** 2 for i in num_list if i % 2 == 0]

print(new_list)
