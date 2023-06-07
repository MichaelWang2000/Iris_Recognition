import numpy as np
import cv2
import pylab
from matplotlib import pyplot as plt


def outerCircle(img, inner):
    """
    外圆检测，需要先进行内圆检测
    :param img: cv2.imread() numpy.ndarrdy
    :param inner: 调用innerCircle()的返回值，瞳孔霍夫圆参数 numpy.ndarray [x, y, r]
    :return: 虹膜外边缘霍夫圆参数 numpy.ndarray [x, y, r]
    """

    # 该行代码通过numpy数组的切片操作获取图像中包含圆的部分。具体地，使用切片操作“[(inner[1] - inner[2]): (inner[1] + inner[2]), :]”选择图像中以圆心y坐标为中心，半径为inner[2]的区域，以及所有的图像通道。
    # 其中，切片“[(inner[1] - inner[2]): (inner[1] + inner[2]), :]”表示选择图像中以inner[1]为中心，inner[2]为半径的水平区域，并选择所有通道的像素值。
    # 提取出包含圆的部分图像，并将其赋值给变量clip_img, clip_img的形状为(inner[2]*2, W, C)。
    clip_img = img[(inner[1] - inner[2]): (inner[1] + inner[2]), :]
    # 对clip_img 进行直方均衡化，平衡分配0-255的像素
    clip_img = cv2.equalizeHist(clip_img)
    # 对输入的图像进行高斯模糊操作，使得图像变得更加平滑，以便于后续的图像处理。
    clip_img = cv2.GaussianBlur(clip_img, (9, 9), 0)
    # 中值平滑medianBlur() 消除图片传输过程中的噪声，方便我们进行处理
    clip_img = cv2.medianBlur(clip_img, 9)

    # 参数minRadius2.0和maxRadius4可根据内外圆半径比值大小进行调节
    circles = cv2.HoughCircles(clip_img, cv2.HOUGH_GRADIENT, 2, 5,
                               param1=30, param2=20, minRadius=int(inner[2] * 2.0), maxRadius=int(inner[2] * 4))
    circles = np.int16(np.around(circles))
    circles[0, :, 1] += inner[1] - inner[2]

    "该段代码通过计算内部圆与所有候选圆心之间的距离，来找到最佳的候选圆心。具体地，代" \
    "码首先创建一个长度为圆数目N的、元素均为0的numpy数组distance。接着，使用enumerate函数遍历circles中的所有圆，" \
    "并使用np.linalg.norm函数计算内部圆心坐标(inner[0], inner[1])与当前圆心坐标(value[0], value[1])之间的欧几里得距离，并将结果存储在distance数组的相应位置中。" \
    "因此，当循环结束后，distance数组的每个元素表示内部圆心与该位置对应圆心之间的欧几里得距离。" \
    "接下来，代码使用np.argmin函数来找到distance数组中距离内部圆心最近的圆心，然后将对应的圆心赋值给变量best_fit。" \
    "具体地，np.argmin函数返回distance数组中最小元素的索引，然后circles[0][最小索引]即为对应的最佳圆心。" \
    "因此，该段代码最终找到距离内部圆心最近的候选圆心，即最佳的拟合圆心，并将其赋值给变量best_fit。"
    distance = np.zeros(len(circles[0]))
    for index, value in enumerate(circles[0, :]):
        distance[index] = np.linalg.norm(np.array((inner[0], inner[1])) - np.array((value[0], value[1])))
    best_fit = circles[0][np.argmin(distance)]
    return best_fit
