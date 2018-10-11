# 随机圆

import numpy as np
import cv2

canvas = np.zeros((500, 500, 3), dtype="uint8")
for i in range(0, 80):
    radius = np.random.randint(5, high=200)
    color = np.random.randint(0, high=256, size=(3,))  # 这种的无法作为color使用
    r = np.random.randint(0, high=256)
    g = np.random.randint(0, high=256)
    b = np.random.randint(0, high=256)
    pt = np.random.randint(0, high=500, size=(2,))
    cv2.circle(canvas, tuple(pt), radius, (r, g, b),-1)

cv2.imshow("Canvas", canvas)
cv2.waitKey(0)
