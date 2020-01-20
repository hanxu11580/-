from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import math

def weights(x, x1, y, y1):
    '''
    :param x: 小数成分的x
    :param x1: 咱们生成的4个整数坐标
    :param y: y
    :param y1:
    :return: 权重
    '''
    weight = abs(x-x1) * abs(y-y1)
    return weight



src_img = np.array(Image.open('./img1.jpg'))
srcH, srcW, channel = src_img.shape[0], src_img.shape[1], src_img.shape[2]

dstH = dstW = 2048
dst_img = np.zeros((dstH, dstW, channel), np.uint8)

for i in range(dstH-1):
    for j in range(dstW-1):
        # 在这查了一下 需要对齐，不然会出现黑线，可以看图片2Linear_interpolation这个图片就是有黑线的
        # 具体原因我也有点懵这 T_T
        x = (i+0.5) * (srcH/dstH)-0.5
        y = (j+0.5) * (srcW/dstW)-0.5

        # 现在获取原图周围4个点 math.ceil向上取整， math.floor向下取整
        # 现在假如(x,y)=(0.75, 0.75)这样的像素点是无法取到的，我们取下面4个原图的坐标，作为插值坐标
        x1, y1 = math.floor(x), math.floor(y) # 这是取到的是原图的(0,0)
        x2, y2 = math.floor(x), math.ceil(y) # (0, 1)
        x3, y3 = math.ceil(x), math.floor(y) # (1, 0)
        x4, y4 = math.ceil(x), math.ceil(y) # (1, 1)
        # 这样权重就为：W = abs(x-x1)*abs(y-y1),这里我定义一个函数用于计算权重
        w1 = weights(x, x1, y, y1)
        w2 = weights(x, x2, y, y2)
        w3 = weights(x, x3, y, y3)
        w4 = weights(x, x4, y, y4)
        # 下面则是我们生成图坐标对应4个点乘以对应权重的之和
        dst_img[i, j] = w1*src_img[x1, y1] + w2*src_img[x2, y2] + w3*src_img[x3, y3] + w4*src_img[x4, y4]
dst_img = Image.fromarray(np.uint8(dst_img))
dst_img.save('./我是双线性放大图最后结果.jpg')



# 这是2个图在一行，方便对比
# plt.subplot(1, 2, 1)
# plt.imshow(src_img)
# plt.subplot(1, 2, 2)
# plt.imshow(dst_img)
# plt.show()
