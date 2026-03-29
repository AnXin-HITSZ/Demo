# if 条件判断
# condition = 1
# if condition > 0:
#     print("Hello")
#     print("world")
# print("--------------------")


# if 案例：结合前面学习的输入输出及 if 条件判断的知识，完成登录功能的实现（正确账号和密码为 18888888888 / 666888）
# # 正确的账号和密码
# ok_account = "18888888888"
# ok_password = "666888"
#
# # 1. 接收用户输入的账号和密码
# account = input("请输入您的账号：")
# password = input("请输入您的密码：")
#
# # 2. 判断账号和密码是否全部正确，如果都正确，则登录成功
# if account == ok_account and password == ok_password:
#     print("登录成功！")
#
# # 3. 判断账号和密码是否有错误的，如果有任何一个错误，则登录失败，提示错误信息
# if account != ok_account or password != ok_password:
#     print("登录失败！")
#     print("账号或密码错误！")


# if ... else ... 案例：结合前面学习的输入输出及 if 条件判断的知识，完成登录功能的实现（正确账号和密码为 18888888888 / 666888）
# # 正确的账号和密码
# ok_account = "18888888888"
# ok_password = "666888"
#
# # 1. 接收用户输入的账号和密码
# account = input("请输入您的账号：")
# password = input("请输入您的密码：")
#
# # 2. 判断账号和密码是否全部正确，如果都正确，则登录成功
# if account == ok_account and password == ok_password:
#     print("登录成功！")
# else:
#     print("登录失败！")
#     print("账号或密码错误！")

# 案例：根据用户输入的年份，判断这一年是闰年还是平年（非整百年份，且能被 4 整除的年份是闰年；整百年份，必须被 400 整除才是闰年）
# year = int(input("请输入需要判断的年份："))
#
# # 如果是 非整百年份，且能被 4 整除 就是闰年；整百年份，必须被 400 整除 也是闰年
# if (year % 100 != 0 and year % 4 == 0) or (year % 400 == 0):
#     print(f"{year} 是闰年")
# else:
#     print(f"{year} 是平年")


# if ... elif ... else ... 案例：根据用户输入的数字，判断数字是正数，还是负数，还是 0
# num = int(input("请输入数字："))
#
# if num > 0:
#     print(f"{num} 是一个正数")
# elif num < 0:
#     print(f"{num} 是一个负数")
# else:
#     print(f"{num} 是 0")


# 案例：根据输入的用户名和密码进行系统登录 - admin/666888、root/123456、me/987654
# username = input("请输入用户名：")
# password = input("请输入密码：")
#
# if username == "admin" and password == "666888":
#     print("登录成功")
# elif username == "root" and password == "123456":
#     print("登录成功")
# elif username == "me" and password == "987654":
#     print("登录成功")
# else:
#     print("登录失败，用户名或密码错误！")


"""
案例 - 三角形类型判断：根据输入的三条边的边长（正整数），判定是等边三角形、等腰三角形、普通三角形，还是不能构成三角形。
  1. 构成三角形的条件：两边之和大于第三边
  2. 三角形判定规则：
      三条边都相等：等边三角形
      两条边相等：等腰三角形
      三条边都不相等：普通三角形
"""
# 1. 接收输入的三角形三条边的边长
a = int(input("请输入第一条边的边长："))
b = int(input("请输入第二条边的边长："))
c = int(input("请输入第三条边的边长："))

# 2. 判断三角形的类型
if a + b > c and a + c > b and b + c > a:   # 条件成立，构成三角形
    # pass    # pass 是一个空语句，起到语法占位的作用
    if a == b and b == c:
        print(f"{a}、{b}、{c} 这三个边长构成等边三角形")
    elif a == b or b == c or a == c:
        print(f"{a}、{b}、{c} 这三个边长构成等腰三角形")
    else:
        print(f"{a}、{b}、{c} 这三个边长构成普通三角形")
else:
    print(f"{a}、{b}、{c} 这三个边长不能构成三角形！")
