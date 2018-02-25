import xlrd
import xlwt
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import spline
matplotlib.rcParams['font.sans-serif'] = ['SimHei']

Workbook = xlrd.open_workbook('上行.xlsx')
wbk = xlwt.Workbook()
c = wbk.add_sheet('c',cell_overwrite_ok=True)
table1 = Workbook.sheets()[0]
nrows1 = table1.nrows

x2 = []
x5 = []
#船型
for i in range(nrows1):
	if i == 0:
		continue
	x2.append(table1.row_values(i)[2:3])
print(x2)
# 船宽
for i in range(nrows1):
    if i == 0:
        continue
    x5.append(table1.row_values(i)[5:6])
print(x5)

def 船宽占比(船型, 船宽):
    js = 0
    zs = 0
    global 占比
    占比 = 0
    for m,i in enumerate(x2):
        if i == [船型]:
            zs = zs + 1
            if x5[m][0]>船宽[0] and x5[m][0]<=船宽[1]:
                js = js + 1
    占比 = js/zs

船宽占比('客船', [8,10])
客船_8_10 = 占比
船宽占比('客船', [10,12])
客船_10_12 = 占比
船宽占比('客船', [14,16])
客船_14_16 = 占比
船宽占比('客船', [16,18])
客船_16_18 = 占比

船宽占比('商品车滚装船', [14,16])
商品车滚装船_14_16 = 占比
船宽占比('商品车滚装船', [16, 18])
商品车滚装船_16_18 = 占比

船宽占比('集装箱船', [12,14])
集装箱船_12_14 = 占比
船宽占比('集装箱船', [14,16])
集装箱船_14_16 = 占比
船宽占比('集装箱船', [16,18])
集装箱船_16_18 = 占比

船宽占比('货船', [8,10])
货船_8_10 = 占比
船宽占比('货船', [10,12])
货船_10_12 = 占比
船宽占比('货船', [12,14])
货船_12_14 = 占比
船宽占比('货船', [14,16])
货船_14_16 = 占比
船宽占比('货船', [16,18])
货船_16_18 = 占比

船宽占比('小船', [3.9,6])
小船_4_6 = 占比
船宽占比('小船', [6,8])
小船_6_8 = 占比
船宽占比('小船', [8,10])
小船_8_10 = 占比

x = np.arange(5)
fig, ax1 = plt.subplots()

# 客船
ax1.bar(0-0.3, 100*客船_8_10, 0.2)
plt.text(0-0.3, 100*客船_8_10 + 0.5, '%.2f' % (100*客船_8_10), ha='center', va='bottom', fontsize='10')
plt.text(0-0.3, -1, '(8,\n10]', ha='center', va='top', fontsize='10')

ax1.bar(0-0.1, 100*客船_10_12, 0.2)
plt.text(0-0.1, 100*客船_10_12 + 0.5, '%.2f' % (100*客船_10_12), ha='center', va='bottom', fontsize='10')
plt.text(0-0.1, -1, '(10,\n12]', ha='center', va='top', fontsize='10')

ax1.bar(0+0.1, 100*客船_14_16, 0.2)
plt.text(0+0.1, 100*客船_14_16 + 0.5, '%.2f' % (100*客船_14_16), ha='center', va='bottom', fontsize='10')
plt.text(0+0.1, -1, '(14,\n16]', ha='center', va='top', fontsize='10')

ax1.bar(0+0.3, 100*客船_16_18, 0.2)
plt.text(0+0.3, 100*客船_16_18 + 0.5, '%.2f' % (100*客船_16_18), ha='center', va='bottom', fontsize='10')
plt.text(0+0.3, -1, '(16,\n17.2]', ha='center', va='top', fontsize='10')

# 商品车滚装船
ax1.bar(1-0.1, 100*商品车滚装船_14_16, 0.2)
plt.text(1-0.1, 100*商品车滚装船_14_16 + 0.5, '%.2f' % (100*商品车滚装船_14_16), ha='center', va='bottom', fontsize='10')
plt.text(1-0.1, -1, '(14,\n16]', ha='center', va='top', fontsize='10')

ax1.bar(1+0.1, 100*商品车滚装船_16_18, 0.2)
plt.text(1+0.1, 100*商品车滚装船_16_18 + 0.5, '%.2f' % (100*商品车滚装船_16_18), ha='center', va='bottom', fontsize='10')
plt.text(1+0.1, -1, '(16,\n17.2]', ha='center', va='top', fontsize='10')

# 集装箱船
ax1.bar(2-0.2, 100*集装箱船_12_14, 0.2)
plt.text(2-0.2, 100*集装箱船_12_14 + 0.5, '%.2f' % (100*集装箱船_12_14), ha='center', va='bottom', fontsize='10')
plt.text(2-0.2, -1, '(12,\n14]', ha='center', va='top', fontsize='10')

ax1.bar(2, 100*集装箱船_14_16, 0.2)
plt.text(2, 100*集装箱船_14_16 + 0.5, '%.2f' % (100*集装箱船_14_16), ha='center', va='bottom', fontsize='10')
plt.text(2, -1, '(14,\n16]', ha='center', va='top', fontsize='10')

ax1.bar(2+0.2, 100*集装箱船_16_18, 0.2)
plt.text(2+0.2, 100*集装箱船_16_18 + 0.5, '%.2f' % (100*集装箱船_16_18), ha='center', va='bottom', fontsize='10')
plt.text(2+0.2, -1, '(16,\n17.2]', ha='center', va='top', fontsize='10')

# 货船
ax1.bar(3-0.4, 100*货船_8_10, 0.2)
plt.text(3-0.4, 100*货船_8_10 + 0.5, '%.2f' % (100*货船_8_10), ha='center', va='bottom', fontsize='10')
plt.text(3-0.4, -1, '(8,\n10]', ha='center', va='top', fontsize='10')

ax1.bar(3-0.2, 100*货船_10_12, 0.2)
plt.text(3-0.2, 100*货船_10_12 + 0.5, '%.2f' % (100*货船_10_12), ha='center', va='bottom', fontsize='10')
plt.text(3-0.2, -1, '(10,\n12]', ha='center', va='top', fontsize='10')

ax1.bar(3, 100*货船_12_14, 0.2)
plt.text(3, 100*货船_12_14 + 0.5, '%.2f' % (100*货船_12_14), ha='center', va='bottom', fontsize='10')
plt.text(3, -1, '(12,\n14]', ha='center', va='top', fontsize='10')

ax1.bar(3+0.2, 100*货船_14_16, 0.2)
plt.text(3+0.2, 100*货船_14_16 + 0.5, '%.2f' % (100*货船_14_16), ha='center', va='bottom', fontsize='10')
plt.text(3+0.2, -1, '(14,\n16]', ha='center', va='top', fontsize='10')

ax1.bar(3+0.4, 100*货船_16_18, 0.2)
plt.text(3+0.4, 100*货船_16_18 + 0.5, '%.2f' % (100*货船_16_18), ha='center', va='bottom', fontsize='10')
plt.text(3+0.4, -1, '(16,\n17.2]', ha='center', va='top', fontsize='10')


# 小船
ax1.bar(4-0.2, 100*小船_4_6, 0.2)
plt.text(4-0.2, 100*小船_4_6 + 0.5, '%.2f' % (100*小船_4_6), ha='center', va='bottom', fontsize='10')
plt.text(4-0.2, -1, '(4,\n6]', ha='center', va='top', fontsize='10')

ax1.bar(4, 100*小船_6_8, 0.2)
plt.text(4, 100*小船_6_8 + 0.5, '%.2f' % (100*小船_6_8), ha='center', va='bottom', fontsize='10')
plt.text(4, -1, '(6,\n8]', ha='center', va='top', fontsize='10')

ax1.bar(4+0.2, 100*小船_8_10, 0.2)
plt.text(4+0.2, 100*小船_8_10 + 0.5, '%.2f' % (100*小船_8_10), ha='center', va='bottom', fontsize='10')
plt.text(4+0.2, -1, '(8,\n10]', ha='center', va='top', fontsize='10')




plt.title('不同船型各船宽范围数量占比（上行）\n')

plt.xticks(x, ('\n\n客船', '\n\n商品车滚装船', '\n\n集装箱船', '\n\n货船', '\n\n其他'),fontsize='12')
plt.ylabel('百分比 %\n',fontsize='12')
# plt.legend(loc = 'upper left')
plt.tight_layout()
plt.savefig("不同船型各船宽范围数量占比（上行）.jpg", dpi=200,fontsize='12')
plt.show()