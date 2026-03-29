total = int(input("请输入用电度数："))

if total <= 2880:
    sum = total * 0.4883
elif total >= 2880 and total <= 4800:
    sum = 2880 * 0.4883 + (total - 2880) * 0.5383
else:
    sum = 2880 * 0.4883 + (4800 - 2880) * 0.5383 + (total - 4800) * 0.7883

print(f"计算电费为：{sum} 元")
