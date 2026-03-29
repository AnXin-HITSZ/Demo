# while 循环：打印 10 遍 “人生苦短，我用 Python ~”
#
# i = 0
# while i < 10:
#     print("人生苦短，我用 Python ~")
#     i += 1
# else:
#     print("循环正常结束")

# while 案例：计算 1 - 100 之间所有偶数的累加之和
total = 0   # 记录累加之和
i = 1   # 循环开始的数字

while i <= 100:
    if i % 2 == 0:  # 偶数
        total += i
    i += 1

print(f"1 - 100 之间的偶数的累加之和：{total}")
