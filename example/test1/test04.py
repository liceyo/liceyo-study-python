# 题目：输入某年某月某日，判断这一天是这一年的第几天？

year = int(input("年:"))
month = int(input("月:"))
day = int(input("日:"))
# 每月天数
monthDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# 判断闰年
if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
    monthDays[1] = 29
else:
    monthDays[1] = 28
# 累加月
totalDays = 0
if 0 < month <= 12:
    for md in range(0, month - 1):
        totalDays += monthDays[md]
else:
    print("error-month")
# 加上天
if day <= monthDays[month - 1]:
    totalDays += day
else:
    print("error-day")
print("it is the %dth day." % totalDays)
