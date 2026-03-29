score = int(input("请输入您的考试成绩："))

if score >= 85:
    print("成绩等级：优秀")
elif score >= 60 and score < 85:
    print("成绩等级：及格")
else:
    print("成绩等级：不及格")
