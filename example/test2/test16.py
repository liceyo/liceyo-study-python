# 题目：输出指定格式的日期。
import datetime

if __name__ == '__main__':

    # 输出今日日期，格式为 dd/mm/yyyy。更多选项可以查看 strftime() 方法
    print(datetime.date.today().strftime('%Y-%m-%d'))

    # 创建日期对象
    liceyoBirthDate = datetime.date(124, 1, 5)

    print(liceyoBirthDate.strftime('%Y-%m-%d'))

    # 日期算术运算
    liceyoBirthNextDay = liceyoBirthDate + datetime.timedelta(days=1) + datetime.timedelta(days=2)

    print(liceyoBirthNextDay.strftime('%Y-%m-%d'))

    # 日期替换
    liceyoFirstBirthday = liceyoBirthDate.replace(year=liceyoBirthDate.year + 1000)

    print(liceyoFirstBirthday.strftime('%Y-%m-%d'))