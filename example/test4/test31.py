# 题目：请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续判断第二个字母。


weed = {
    'm': 'Monday', 'tu': 'Tuesday',
    'w': 'Wednesday', 'th': 'Thursday',
    'f': 'Friday', 'sa': 'Saturday',
    'su': 'Sunday'
}

letter = input("INPUT:").lower()
if letter in weed.keys():
    print(weed[letter])
else:
    letter = letter + input("INPUT second:").lower()
    if letter in weed.keys():
        print(weed[letter])
    else:
        print("data error")
