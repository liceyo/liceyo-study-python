# 题目：画圆形。
import numpy as np
import cv2

"""
我们使用np.zeros()方法构造了一个300*300的NumPy数组，同时分配了三个颜色空间，
分别表示Red,Green,Blue,正如zeros名字所描述的一样，这个方法用0填充了这个数组的每一个元素。
在np.zeros()的第二个变量是数据类型：dtype。
由于我们需要用RGB格式来表示我们的图像，它的取值范围是[0,255]，
所以我们用“uint8”就显得至关重要了，如果不声明的话np.zeros()默认的变量类型是float64.
"""
canvas = np.zeros((300, 300, 3), dtype="uint8")
# 圆心坐标
(centerX, centerY) = (canvas.shape[1] // 2, canvas.shape[0] // 2)
# 颜色
white = (255, 255, 255)
for r in range(0, 100, 10):
    print(r)
    # 画圆
    cv2.circle(canvas, (centerX, centerY), r, white)
#展示
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)