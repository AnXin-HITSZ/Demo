total = int(input("请输入您的购物车的商品总额："))

if total >= 500:
    print(f"实际应付的金额为：{total * 0.8}")
elif total < 500 and total >= 300:
    print(f"实际应付的金额为：{total * 0.9}")
elif total < 300 and total >= 100:
    print(f"实际应付的金额为：{total * 0.95}")
else:
    print(f"实际应付的金额为：{total}")
