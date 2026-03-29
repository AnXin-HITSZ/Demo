# 常见数据类型 -> type()：获取指定的字面量或变量的类型
# print("Hello")
# print(type("Hello"))    # str
#
# print(type(10)) # int
# print(type(3.14))   # float
# print(type(True))   # bool
# print(type(False))  # bool
# print(type(None))   # NoneType
#
# num = -100
# print(type(num))    # int

# 常见数据类型 -> isinstance(数据, 类型) -> bool 值 -> 判定数据是否是指定的类型，如果是：True，否则：False
# print(isinstance(num, int)) # True
# print(isinstance(num, float))   # False
# print(isinstance(num, bool))    # False


# 字符串
# 定义字符串的三种方式
# s1 = "Hello"    # 双引号定义
# s2 = 'Python'   # 单引号定义
# s3 = """
# Hello:
#     World!
#     Python!
# """ # 三引号定义（多行字符串）
#
# print(s1)
# print(s2)
# print(s3)
#
# print(type(s1))
# print(type(s2))
# print(type(s3))

# 定义字符串 -> It's very good
# 转义字符 \'、\"、\n、\t
# msg1 = 'It\'s very good'
# print(msg1)
#
# msg2 = "It's very good"
# print(msg2)
#
# msg3 = "Hello 的意思就是 \"您好\""
# print(msg3)
#
# msg4 = 'Hello 的意思就是 "您好"'
# print(msg4)
#
# print("Hello:\n\tWorld!\n\tPython!")    # \n：换行，\t：Tab 缩进


# 字符串拼接
# s1 = "人生苦短，" "我用 Python"
# print(s1)
#
# msg1 = "人生苦短"
# msg2 = "我用 Python"
# print(msg1 + "，" + msg2)

# 案例：-> str(int数字) -> 将 int 类型的数字转为字符串
# name = "Me"
# age = 22
# pro = "计算机技术"
# hobby = "Python、Java"
# print("大家好，我是 " + name + "，今年 " + str(age) + " 岁，学习的专业是 " + pro + "，爱好 " + hobby)


# 字符串格式化 -> 方式一：%s 占位符
# name = "Me"
# age = 22
# pro = "计算机技术"
# hobby = "Python、Java"
# print("大家好，我是 %s，今年 %s 岁，学习的专业是 %s，爱好 %s" % (name, age, pro, hobby))

# 字符串格式化 -> 方式二：f"... {变量名 / 表达式} ..." -> 推荐方式
name = "Me"
age = 22
pro = "计算机技术"
hobby = "Python、Java"
print(f"大家好，我是 {name}，今年 {age} 岁，学习的专业是 {pro}，爱好 {hobby}")
