# 题目：一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？

# x+100=n^2 and x+100+168=m^2
# (m+n)(m-n)=168
# 设i=m+n,j=m-n .可得 i*j=168 and m=(i+j)/2 and n=(i-j)/2
# 得到i和j都是偶数，j>=2 ,2<=i<=168/2


for i in range(2, 85):
    if 168 % i == 0:
        j = 168 / i
        if i > j and (i + j) % 2 == 0 and (i - j) % 2 == 0:
            m = (i + j) / 2
            n = (i - j) / 2
            x = n * n - 100
            print(x)
