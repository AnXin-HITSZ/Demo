# ---------------------------- 字典 -> key 不能重复（如果重复，后面的值会覆盖前面的值）、key 必须得是不可变类型（str / int / float / tuple） ----------------------------
# # 定义字典
# dict1 = {"student1": 670, "student2": 608, "student3": 580, "student4": 688}
#
# print(dict1)
# print(type(dict1))
#
# # key 必须得是不可变类型（str / int / float / tuple），不能是 list、set、dict
# dict2 = {0: 670, 1.5: 608, (1, 2): 580, ('A', 'B'): 688}
# print(dict2)
#
# # 访问
# print(dict1["student2"])    # 获取
#
# dict1["student2"] = 688
# print(dict1)


# ---------------------------- 字典 常见操作 ----------------------------
# dict1 = {"student1": 670, "student2": 608, "student3": 580, "student4": 688}
# print(dict1)
#
# # 添加 - key 不存在就是添加
# dict1["student5"] = 550
# print(dict1)
#
# # 修改 - key 存在就是修改
# dict1["student5"] = 620
# print(dict1)
#
# # 查询
# print(dict1["student5"])    # 根据 key 获取 value
# print(dict1.get("student5"))    # 根据 key 获取 value
#
# print(dict1.keys()) # 获取所有的 key
# print(dict1.values())   # 获取所有的 value
# print(dict1.items())    # 获取所有的键值对 key: value
#
# # 删除
# score = dict1.pop("student3")
# print(score)
# print(dict1)
#
# del dict1["student4"]
# print(dict1)
#
# # 遍历
# for k in dict1.keys():
#     print(f"{k}: {dict1[k]}")
#
# for item in dict1.items():
#     print(f"{item[0]}: {item[1]}")
#
# for k, v in dict1.items():
#     print(f"{k}: {v}")


"""
案例：
    购物车管理系统
"""
shopping_cart = {}
menu = """
########## 购物车系统 ##########
#        1. 添加购物车         #
#        2. 修改购物车         #
#        3. 删除购物车         #
#        4. 查询购物车         #
#        5. 退出购物车         #
##############################
"""
print("欢迎使用购物车管理系统！")

while True:
    # 1. 制作菜单
    print(menu)

    # 2. 执行的具体操作
    choice = input("请选择要执行的操作（1 - 5）：")

    match choice:
        case "1":  # 添加购物车
            goods_name = input("请输入商品名称：")
            goods_price = float(input("请输入商品价格："))
            goods_num = int(input("请输入商品数量："))

            # 如果商品存在，则不执行添加，提示信息
            if goods_name in shopping_cart:
                print("该商品已存在，请重新选择！")
            else:
                shopping_cart[goods_name] = {"price": goods_price, "num": goods_num}
                print("商品添加完毕！")

        case "2":  # 修改购物车
            goods_name = input("请输入要修改的商品名称：")
            # 如果商品不存在，则提示错误信息，重新选择
            if goods_name not in shopping_cart:
                print("该商品不存在，请重新选择！")
                continue

            goods_price = float(input("请输入商品的最新价格："))
            goods_num = int(input("请输入商品的最新数量："))
            shopping_cart[goods_name] = {"price": goods_price, "num": goods_num}
            print("商品修改完毕！")

        case "3":  # 删除购物车
            goods_name = input("请输入要删除的商品名称：")

            # 如果商品不存在，则提示错误信息，重新选择
            if goods_name not in shopping_cart:
                print("该商品不存在，请重新选择！")
            else:
                del shopping_cart[goods_name]
                print("商品删除完毕！")

        case "4":  # 查询购物车
            for goods_name in shopping_cart.keys():
                goods_info = shopping_cart[goods_name]
                print(f"商品名称：{goods_name}，商品价格：{goods_info['price']}，商品数量：{goods_info['num']}")
        case "5":  # 退出购物车
            print("Bye ~")
            break
        case _:  # 匹配其他所有情况
            print("非法操作！")
