from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# def near_img(img_path):

src_img = np.array(Image.open('./img1.jpg'))
srcH, srcW, channel = src_img.shape[0], src_img.shape[1], src_img.shape[2]

dstH = dstW = 2048
dst_img = np.zeros((dstH, dstW, channel), np.uint8)
for i in range(dstH):
    for j in range(dstW):
        srcX = round(i * (srcH/dstH)) #取到的小数直接四舍五入
        srcY = round(j * (srcW/dstW))

        dst_img[i, j] = src_img[srcX, srcY]

dst_img = Image.fromarray(np.uint8(dst_img))
dst_img.save('./near_interpolation.jpg')

# plt.subplot(1, 2, 1)
# plt.imshow(src_img)
# plt.subplot(1, 2, 2)
# plt.imshow(dst_img)
# plt.show()

# 这个邻近插值 出来的图片很垃圾 - - ！
# 出现好多的小方块（也就是锯齿） 放弃这个方法了

