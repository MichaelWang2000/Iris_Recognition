import numpy as np
import cv2


def innerCircle(img):
    """
    内圆检测
    :param img: cv2.imread() numpy.ndarrdy
    :return: 瞳孔霍夫圆参数 numpy.ndarray [x, y, r]
    """

    # 中值平滑medianBlur() 消除图片传输过程中的噪声，方便我们进行处理
    img = cv2.medianBlur(img, 11)

    # 简单阈值函数 将我们传入的img 最小阀值为50，最大为255 按照cv2.THRESH_BINARY 的处理方式进行。 方式：超过阈值50即全部变化为255
    ret, img = cv2.threshold(img, 50, 255, cv2.THRESH_BINARY)

    # kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (20, 20))
    # img = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

    # img = cv2.bitwise_not(img)
    # kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (20, 20))
    # img = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

    # 霍夫曼圆检测 可以通过更改param1和param2的参数来更加精准的判断圆的位置 返回值为每个圆的(圆心横坐标，圆心纵坐标，半径)
    circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 2, 5,
                               param1=110, param2=20, minRadius=20, maxRadius=130)
    # 将获取到的圆的数据，进行四舍五入为整数，并将其转化为int16数据格式
    circles = np.int16(np.around(circles))

    "这行代码假设circles是一个numpy数组，它的形状是(N, 1, 3)，其中N表示圆的数量。" \
    "该数组的第一维表示每个圆，第二维包含单个圆的信息，第三维是每个圆的属性，其中第三个元素表示圆的半径。" \
    "该行代码将circles数组中第一个圆的半径增加3。具体地，使用索引“[0,:,:]”选择第一个圆，" \
    "然后使用索引“2”选择该圆的半径，并使用“+=3”将其增加3。因此，该行代码将修改circles" \
    "数组的内容，使得第一个圆的半径增加了3。"
    circles[0, :, 2] += 3

    # 返回一个包含三个元素的numpy数组，它表示第一个圆的信息。
    return circles[0][0]
