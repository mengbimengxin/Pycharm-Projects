# 引入库
import matplotlib.pyplot as plt
import numpy as np

# 各已知参数
# 基圆半径（mm）
r0 = 45
# 滚子半径（mm）
rr = 6
# 偏距（mm）
e = 10
# 行程（mm）
h = 50
# 推程运动角（°）
p0 = 120
# 远休止角（°）
p1 = 90
# 回程运动角（°）
p2 = 90
# 近休止角（°）
p3 = 60

s0 = np.sqrt(np.square(r0) - np.square(e))


# 推程运动规律
def S(p):
    if p >= 0 and p <= p0:
        s = h * (1.0 - np.cos(np.pi * p / p0)) / 2
        ds_dp = h * np.pi / (2 * p0 * np.pi / 180) * np.sin(np.pi * p / p0)
    elif p > p0 and p < p0 + p1:
        s = h
        ds_dp = 0
    elif p >= p0 + p1 and p <= p0 + p1 + (p2 / 2):
        s = h - (2 * h * np.square(p - p0 - p1) / np.square(p2))
        ds_dp = (-4 * h * (p - p0 - p1)) / (np.square(p2) * np.pi / 180)
    elif p > p0 + p1 + (p2 / 2) and p <= p0 + p1 + p2:
        s = (2 * h * np.square(p2 - p + p0 + p1)) / np.square(p2)
        ds_dp = (-4 * h * (p2 - p + p0 + p1)) / (np.square(p2) * np.pi / 180)
    else:
        s = 0
        ds_dp = 0
    alpa = np.abs(np.arctan((ds_dp - e) / (np.sqrt(r0 ** 2 - e ** 2) + s))) * 180 / np.pi
    return s, ds_dp, alpa


res_s = []
res_x = []
res_y = []
res_x1 = []
res_y1 = []
res_x2 = []
res_y2 = []
res_alpa = []

for i in np.arange(0, 360 + 1, 1):
    s, ds_dp, alpa = S(i)

    # 理论轮廓坐标
    x = (s0 + s) * np.sin(i * np.pi / 180) + e * np.cos(i * np.pi / 180)
    y = (s0 + s) * np.cos(i * np.pi / 180) - e * np.sin(i * np.pi / 180)

    # 实际轮廓坐标
    dx_dp = (ds_dp - e) * np.sin(i * np.pi / 180) + (s0 + s) * np.cos(i * np.pi / 180)
    dy_dp = (ds_dp - e) * np.cos(i * np.pi / 180) - (s0 + s) * np.sin(i * np.pi / 180)
    R = np.sqrt(dx_dp ** 2 + dy_dp ** 2)
    sin = dx_dp / R
    cos = -dy_dp / R
    x1 = x - rr * cos
    y1 = y - rr * sin

    # 外等距曲线坐标
    x2 = x + rr * cos
    y2 = y + rr * sin

    res_s.append(round(s, 3))
    res_x.append(round(x, 3))
    res_y.append(round(y, 3))
    res_x1.append(round(x1, 3))
    res_y1.append(round(y1, 3))
    res_x2.append(round(x2, 3))
    res_y2.append(round(y2, 3))
    res_alpa.append(round(alpa, 3))

    # 滚子坐标
    if i % 10 == 0:
        theta = np.arange(0, 2 * np.pi, np.pi / 180)
        c = x + rr * np.cos(theta)
        d = y + rr * np.sin(theta)
        plt.figure(1, figsize=(10, 10), dpi=80)
        plt.plot(c, d, "r-")

# 推程最大压力角
alpa_max = max(res_alpa[0:p0])
i_max = res_alpa.index(alpa_max)

print("推程最大压力角alpa_max", alpa_max, "凸轮转角", i_max)
print("推杆行程s", res_s[::10])
print("理论轮廓坐标值x", res_x[::10])
print("理论轮廓坐标值y", res_y[::10])
print("实际轮廓坐标值x1", res_x1[::10])
print("实际轮廓坐标值y1", res_y1[::10])
print("实际轮廓坐标值x2", res_x2[::10])
print("实际轮廓坐标值y2", res_y2[::10])
print("压力角alpa", res_alpa[::10])
# print(len(res_x), len(res_y))

# 偏距圆
theta1 = np.arange(0, 2 * np.pi, np.pi / 180)
a = e * np.cos(theta1)
b = e * np.sin(theta1)

# 基圆
theta2 = np.arange(0, 2 * np.pi, np.pi / 180)
a1 = r0 * np.cos(theta2)
b1 = r0 * np.sin(theta2)

# 绘图
plt.figure(1, figsize=(10, 10), dpi=80)
# 获取当前坐标轴对象
ax = plt.gca()
# 将垂直坐标刻度置于左边框
ax.yaxis.set_ticks_position('left')
# 将水平坐标刻度置于底边框
ax.xaxis.set_ticks_position('bottom')
# 将左边框置于数据坐标原点
ax.spines['left'].set_position(('data', 0))
# 将底边框置于数据坐标原点
ax.spines['bottom'].set_position(('data', 0))
# 将右边框和顶边框设置成无色
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# 偏距圆与基圆轮廓线
plt.plot(a, b, "r-")
plt.plot(a1, b1, "g-")
# 理论轮廓线
plt.plot(res_x, res_y)
# 实际轮廓线
plt.plot(res_x1, res_y1)
# 外等距曲线
plt.plot(res_x2, res_y2)

# 推杆行程图
plt.figure(2, figsize=(10, 10), dpi=80)
ax1 = plt.gca()
# 将垂直坐标刻度置于左边框
ax1.yaxis.set_ticks_position('left')
# 将水平坐标刻度置于底边框
ax1.xaxis.set_ticks_position('bottom')
# 将左边框置于数据坐标原点
ax1.spines['left'].set_position(('data', 0))
# 将底边框置于数据坐标原点
ax1.spines['bottom'].set_position(('data', 0))
# 将右边框和顶边框设置成无色
ax1.spines['right'].set_color('none')
ax1.spines['top'].set_color('none')
plt.xlabel("°")
plt.ylabel("mm")
plt.plot(res_s)

plt.show()
