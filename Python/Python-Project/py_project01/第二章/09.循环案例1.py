"""
案例 1：根据输入的用户名密码执行登录操作，具体要求如下：
    1. 正确的用户名和密码为 admin/666888、root/123456、me/987654
    2. 输入用户名和密码进行登录，直到登录成功，程序结束运行；如果登录失败，则继续输入用户名和密码进行登录
    3. 输入的用户名和密码不能为空
    4. 登录成功：输出 “登录成功！”
    5. 登录失败：输出 “用户名或密码错误，请重新输入！”

关键字：
    break：只能够出现在循环中，表示结束、跳出循环的含义（break 跳出循环时，while 后面的 else 中的代码将不会执行）
    continue：只能够出现在循环中，表示中断本次循环，直接进入下一次循环
"""

while True:
    # 1. 接收输入的用户名和密码
    username = input("请输入正确的用户名：")
    password = input("请输入正确的密码：")

    # 2. 校验：输入的用户名和密码不能为空
    if username == "" or password == "":
        print("输入的用户名和密码不能为空！")
        continue    # 结束当前循环，直接进入下一轮循环

    # 3. 判断用户名和密码的正确性，执行登录操作
    if username == "admin" and password == "666888":
        print("登录成功！")
        break   # 跳出循环
    elif username == "root" and password == "123456":
        print("登录成功！")
        break  # 跳出循环
    elif username == "me" and password == "987654":
        print("登录成功！")
        break  # 跳出循环
    else:
        print("用户名或密码错误，请重新输入！")
