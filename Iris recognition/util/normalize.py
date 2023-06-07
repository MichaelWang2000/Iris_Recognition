import numpy as np


def normalize(image, x_iris, y_iris, r_iris, x_pupil, y_pupil, r_pupil,
              radpixels, angulardiv):
    """
    Description:
        通过将圆形区域展开为恒定尺寸的矩形块来规格化虹膜区域。
    Input:
        image		- Input iris image.
        x_iris		- x-coordinate of the circle defining the iris boundary.
        y_iris		- y-coordinate of the circle defining the iris boundary.
        r_iris		- Radius of the circle defining the iris boundary.
        x_pupil		- x-coordinate of the circle defining the pupil boundary.
        y_pupil		- y-coordinate of the circle defining the pupil boundary.
        r_pupil		- Radius of the circle defining the pupil boundary.
        radpixels	- Radial resolution (vertical dimension).
        angulardiv	- Angular resolution (horizontal dimension).
    Output:
        polar_array	- Normalized form of the iris region.
        polar_noise	- Normalized form of the noise region.
    """
    radiuspixels = radpixels + 2
    angledivisions = angulardiv - 1

    # 将被用来对极坐标半径值进行离散化，并计算每个离散化半径下的平均边缘强度。
    r = np.arange(radiuspixels)
    # 用来对极坐标角度值进行离散化，并计算每个离散化角度下的平均边缘强度。 方便我们之后处理获取像素坐标和像素值
    theta = np.linspace(0, 2 * np.pi, angledivisions + 1)

    # 瞳孔中心和虹膜中心是不一样的所以需要计算
    ox = x_pupil - x_iris
    oy = y_pupil - y_iris

    if ox <= 0:
        sgn = -1
    elif ox > 0:
        sgn = 1

    if ox == 0 and oy > 0:
        sgn = 1

    a = np.ones(angledivisions + 1) * (ox ** 2 + oy ** 2)

    # Need to do something for ox = 0
    if ox == 0:
        phi = np.pi / 2
    else:
        phi = np.arctan(oy / ox)

    b = sgn * np.cos(np.pi - phi - theta)

    # 计算虹膜周围的半径作为角度的函数
    r = np.sqrt(a) * b + np.sqrt(a * b ** 2 - (a - r_iris ** 2))
    r = np.array([r - r_pupil])

    rmat = np.dot(np.ones([radiuspixels, 1]), r)

    rmat = rmat * np.dot(np.ones([angledivisions + 1, 1]),
                         np.array([np.linspace(0, 1, radiuspixels)])).transpose()
    rmat = rmat + r_pupil

    # 排除瞳孔虹膜边界和虹膜边缘的值
    # 因为这些可能不对应于虹膜区域中的区域并且会引入噪声。
    # 也就是说，不要把外环当作虹膜数据。
    rmat = rmat[1: radiuspixels - 1, :]

    # 计算圆形虹膜区域周围每个数据点的笛卡尔位置
    xcosmat = np.dot(np.ones([radiuspixels - 2, 1]), np.array([np.cos(theta)]))
    xsinmat = np.dot(np.ones([radiuspixels - 2, 1]), np.array([np.sin(theta)]))

    xo = rmat * xcosmat
    yo = rmat * xsinmat

    xo = x_pupil + xo
    xo = np.round(xo).astype(int)
    coords = np.where(xo >= image.shape[1])
    xo[coords] = image.shape[1] - 1
    coords = np.where(xo < 0)
    xo[coords] = 0

    yo = y_pupil - yo
    yo = np.round(yo).astype(int)
    coords = np.where(yo >= image.shape[0])
    yo[coords] = image.shape[0] - 1
    coords = np.where(yo < 0)
    yo[coords] = 0

    # 通过将强度值提取到归一化极坐标表示中
    # interpolation
    # x,y = np.meshgrid(np.arange(image.shape[1]), np.arange(image.shape[0]))
    # f = interpolate.interp2d(x, y, image, kind='linear')
    # polar_array = f(xo, yo)
    # polar_array = polar_array / 255

    polar_array = image[yo, xo]
    polar_array = polar_array / 255

    # 使用polar_array中NaN的位置创建噪波阵列
    polar_noise = np.zeros(polar_array.shape)
    coords = np.where(np.isnan(polar_array))
    polar_noise[coords] = 1

    # 去掉孤立点，写出圆形图案
    image[yo, xo] = 255

    # 获取环绕虹膜的像素坐标
    x, y = circlecoords([x_iris, y_iris], r_iris, image.shape)
    image[y, x] = 255

    # 获取瞳孔周围圆周的像素坐标
    xp, yp = circlecoords([x_pupil, y_pupil], r_pupil, image.shape)
    image[yp, xp] = 255

    # 在执行功能编码之前替换NaN
    coords = np.where((np.isnan(polar_array)))
    polar_array2 = polar_array
    polar_array2[coords] = 0.5
    avg = np.sum(polar_array2) / (polar_array.shape[0] * polar_array.shape[1])
    polar_array[coords] = avg

    return polar_array, polar_noise.astype(bool)


def circlecoords(c, r, imgsize, nsides=600):
    """
    Description:
        根据圆心和半径找出圆的坐标。
    Input:
        c   	- Centre of the circle.
        r  		- Radius of the circle.
        imgsize - Size of the image that the circle will be plotted onto.
        nsides 	- Number of sides of the convex-hull bodering the circle
                  (default as 600).
    Output:
        x,y     - Circle coordinates.
    """
    a = np.linspace(0, 2 * np.pi, 2 * nsides + 1)
    xd = np.round(r * np.cos(a) + c[0])
    yd = np.round(r * np.sin(a) + c[1])

    #  去掉大于图像的值
    xd2 = xd
    coords = np.where(xd >= imgsize[1])
    xd2[coords[0]] = imgsize[1] - 1
    coords = np.where(xd < 0)
    xd2[coords[0]] = 0

    yd2 = yd
    coords = np.where(yd >= imgsize[0])
    yd2[coords[0]] = imgsize[0] - 1
    coords = np.where(yd < 0)
    yd2[coords[0]] = 0

    x = np.round(xd2).astype(int)
    y = np.round(yd2).astype(int)
    return x, y
