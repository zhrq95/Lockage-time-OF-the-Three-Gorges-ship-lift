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
x4 = []

#船型
for i in range(nrows1):
	if i == 0:
		continue
	x2.append(table1.row_values(i)[2:3])
print(x2)
# 船长
for i in range(nrows1):
    if i == 0:
        continue
    x4.append(table1.row_values(i)[4:5])
print(x4)

def 船长占比(船型, 船长):
    js = 0
    zs = 0
    global 占比
    占比 = 0
    for m,i in enumerate(x2):
        if i == [船型]:
            zs = zs + 1
            if x4[m][0]>船长[0] and x4[m][0]<=船长[1]:
                js = js + 1
    占比 = js/zs
船长占比('客船', [40,50])
客船_40_50 = 占比
船长占比('客船', [80,90])
客船_80_90 = 占比
船长占比('客船', [100,110])
客船_100_110 = 占比


船长占比('商品车滚装船', [80,90])
商品车滚装船_80_90 = 占比
船长占比('商品车滚装船', [90,100])
商品车滚装船_90_100 = 占比
船长占比('商品车滚装船', [100,110])
商品车滚装船_100_110 = 占比

船长占比('集装箱船', [79,90])
集装箱船_80_90 = 占比
船长占比('集装箱船', [90,100])
集装箱船_90_100 = 占比
船长占比('集装箱船', [100,110])
集装箱船_100_110 = 占比

船长占比('货船', [50,60])
货船_50_60 = 占比
船长占比('货船', [60,70])
货船_60_70 = 占比
船长占比('货船', [70,80])
货船_70_80 = 占比
船长占比('货船', [80,90])
货船_80_90 = 占比
船长占比('货船', [90,100])
货船_90_100 = 占比

船长占比('小船', [10,20])
小船_10_20 = 占比
船长占比('小船', [20,30])
小船_20_30 = 占比
船长占比('小船', [30,40])
小船_30_40 = 占比
船长占比('小船', [40,50])
小船_40_50 = 占比

x = np.arange(5)
fig, ax1 = plt.subplots()


# 客船
ax1.bar(0-0.2, 100*客船_40_50, 0.2)
plt.text(0-0.2, 100*客船_40_50 + 0.5, '%.2f' % (100*客船_40_50), ha='center', va='bottom', fontsize='10')
plt.text(0-0.2, -1, '(40,\n50]', ha='center', va='top', fontsize='10')

ax1.bar(0, 100*客船_80_90, 0.2)
plt.text(0, 100*客船_80_90 + 0.5, '%.2f' % (100*客船_80_90), ha='center', va='bottom', fontsize='10')
plt.text(0, -1, '(80,\n90]', ha='center', va='top', fontsize='10')

ax1.bar(0+0.2, 100*客船_100_110, 0.2)
plt.text(0+0.2, 100*客船_100_110 + 0.5, '%.2f' % (100*客船_100_110), ha='center', va='bottom', fontsize='10')
plt.text(0+0.2, -1, '(100,\n110]', ha='center', va='top', fontsize='10')

# 商品车滚装船
ax1.bar(1-0.2, 100*商品车滚装船_80_90, 0.2)
plt.text(1-0.2, 100*商品车滚装船_80_90 + 0.5, '%.2f' % (100*商品车滚装船_80_90), ha='center', va='bottom', fontsize='10')
plt.text(1-0.2, -1, '(80,\n90]', ha='center', va='top', fontsize='10')

ax1.bar(1, 100*商品车滚装船_90_100, 0.2)
plt.text(1, 100*商品车滚装船_90_100 + 0.5, '%.2f' % (100*商品车滚装船_90_100), ha='center', va='bottom', fontsize='10')
plt.text(1, -1, '(90,\n100]', ha='center', va='top', fontsize='10')

ax1.bar(1+0.2, 100*商品车滚装船_100_110, 0.2)
plt.text(1+0.2, 100*商品车滚装船_100_110 + 0.5, '%.2f' % (100*商品车滚装船_100_110), ha='center', va='bottom', fontsize='10')
plt.text(1+0.2, -1, '(100,\n110]', ha='center', va='top', fontsize='10')

# 集装箱船
ax1.bar(2-0.2, 100*集装箱船_80_90, 0.2)
plt.text(2-0.2, 100*集装箱船_80_90 + 0.5, '%.2f' % (100*集装箱船_80_90), ha='center', va='bottom', fontsize='10')
plt.text(2-0.2, -1, '(80,\n90]', ha='center', va='top', fontsize='10')

ax1.bar(2, 100*集装箱船_90_100, 0.2)
plt.text(2, 100*集装箱船_90_100 + 0.5, '%.2f' % (100*集装箱船_90_100), ha='center', va='bottom', fontsize='10')
plt.text(2, -1, '(90,\n100]', ha='center', va='top', fontsize='10')

ax1.bar(2+0.2, 100*集装箱船_100_110, 0.2)
plt.text(2+0.2, 100*集装箱船_100_110 + 0.5, '%.2f' % (100*集装箱船_100_110), ha='center', va='bottom', fontsize='10')
plt.text(2+0.2, -1, '(100,\n110]', ha='center', va='top', fontsize='10')

# 货船
ax1.bar(3-0.4, 100*货船_50_60, 0.2)
plt.text(3-0.4, 100*货船_50_60 + 0.5, '%.2f' % (100*货船_50_60), ha='center', va='bottom', fontsize='10')
plt.text(3-0.4, -1, '(50,\n60]', ha='center', va='top', fontsize='10')

ax1.bar(3-0.2, 100*货船_60_70, 0.2)
plt.text(3-0.2, 100*货船_60_70 + 0.5, '%.2f' % (100*货船_60_70), ha='center', va='bottom', fontsize='10')
plt.text(3-0.2, -1, '(60,\n70]', ha='center', va='top', fontsize='10')

ax1.bar(3, 100*货船_70_80, 0.2)
plt.text(3, 100*货船_70_80 + 3, '%.2f' % (100*货船_70_80), ha='center', va='bottom', fontsize='10')
plt.text(3, -1, '(70,\n80]', ha='center', va='top', fontsize='10')

ax1.bar(3+0.2, 100*货船_80_90, 0.2)
plt.text(3+0.2, 100*货船_80_90 + 0.5, '%.2f' % (100*货船_80_90), ha='center', va='bottom', fontsize='10')
plt.text(3+0.2, -1, '(80,\n90]', ha='center', va='top', fontsize='10')

ax1.bar(3+0.4, 100*货船_90_100, 0.2)
plt.text(3+0.4, 100*货船_90_100 + 0.5, '%.2f' % (100*货船_90_100), ha='center', va='bottom', fontsize='10')
plt.text(3+0.4, -1, '(90,\n100]', ha='center', va='top', fontsize='10')


# 小船
ax1.bar(4-0.3, 100*小船_10_20, 0.2)
plt.text(4-0.3, 100*小船_10_20 + 0.5, '%.2f' % (100*小船_10_20), ha='center', va='bottom', fontsize='10')
plt.text(4-0.3, -1, '(10,\n20]', ha='center', va='top', fontsize='10')

ax1.bar(4-0.1, 100*小船_20_30, 0.2)
plt.text(4-0.1, 100*小船_20_30 + 0.5, '%.2f' % (100*小船_20_30), ha='center', va='bottom', fontsize='10')
plt.text(4-0.1, -1, '(20,\n30]', ha='center', va='top', fontsize='10')

ax1.bar(4+0.1, 100*小船_30_40, 0.2)
plt.text(4+0.1, 100*小船_30_40 + 0.5, '%.2f' % (100*小船_30_40), ha='center', va='bottom', fontsize='10')
plt.text(4+0.1, -1, '(30,\n40]', ha='center', va='top', fontsize='10')

ax1.bar(4+0.3, 100*小船_40_50, 0.2)
plt.text(4+0.3, 100*小船_40_50 + 0.5, '%.2f' % (100*小船_40_50), ha='center', va='bottom', fontsize='10')
plt.text(4+0.3, -1, '(40,\n50]', ha='center', va='top', fontsize='10')



plt.title('不同船型各船长范围数量占比（上行）\n')

plt.xticks(x, ('\n\n客船', '\n\n商品车滚装船', '\n\n集装箱船', '\n\n货船', '\n\n其他'),fontsize='12')
plt.ylabel('百分比 %\n')
# plt.legend(loc = 'upper left')
plt.tight_layout()
plt.savefig("不同船型各船长范围数量占比（上行）.jpg", dpi=200,fontsize='12')
plt.show()