from PIL import Image
import cv2
import numpy as np
import matplotlib.pyplot as plt
import math

'''
    取RGB 4个点RGB三层最大的， 有点类似神经网络cnn中的池化层
    具体效果具体不太清楚
'''

src_img = np.array(Image.open('./img1.jpg'))
srcH, srcW, channel = src_img.shape[0], src_img.shape[1], src_img.shape[2]

dstH = dstW = 500
dst_img = np.zeros((dstH, dstW, channel), np.uint8)

for i in range(dstH-1):
    for j in range(dstW-1):
        x = i * (srcH/dstH)
        y = j * (srcW/dstW)

        x1, y1 = math.floor(x), math.floor(y) # (0,0)
        x2, y2 = math.floor(x), math.ceil(y) # (0, 1)
        x3, y3 = math.ceil(x), math.floor(y) # (1, 0)
        x4, y4 = math.ceil(x), math.ceil(y) # (1, 1)

        _0 = max(src_img[x1, y1][0], src_img[x2, y2][0], src_img[x3, y3][0], src_img[x4, y4][0])
        _1 = max(src_img[x1, y1][1], src_img[x2, y2][1], src_img[x3, y3][1], src_img[x4, y4][1])
        _2 = max(src_img[x1, y1][2], src_img[x2, y2][2], src_img[x3, y3][2], src_img[x4, y4][2])
        dst_img[i, j][0], dst_img[i, j][1], dst_img[i, j][2] = _0, _1, _2

dst_img = Image.fromarray(np.uint8(dst_img))
dst_img.save('./max.jpg')

