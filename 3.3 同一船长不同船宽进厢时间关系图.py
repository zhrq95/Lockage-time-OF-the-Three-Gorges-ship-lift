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


x4 = []
x5 = []
x20 = []
# 船长
for i in range(nrows1):
    if i == 0:
        continue
    x4.append(table1.row_values(i)[4:5])
print(x4)
# 船宽
for i in range(nrows1):
    if i == 0:
        continue
    x5.append(table1.row_values(i)[5:6])
print(x5)
# 进厢 + 出厢 时间
for i in range(nrows1):
    if i == 0:
        continue
    x20.append(table1.row_values(i)[20:21])
print(x20)

js11,js12,js13,js14,js15 = 0,0,0,0,0
sum11,sum12,sum13,sum14,sum15 = 0,0,0,0,0
js21,js22,js23,js24,js25 = 0,0,0,0,0
sum21,sum22,sum23,sum24,sum25 = 0,0,0,0,0
js31,js32,js33,js34,js35 = 0,0,0,0,0
sum31,sum32,sum33,sum34,sum35 = 0,0,0,0,0
js41,js42,js43,js44,js45 = 0,0,0,0,0
sum41,sum42,sum43,sum44,sum45 = 0,0,0,0,0
for m5,i5 in enumerate(x5):
    if 14<=i5[0]<=14.5:
        if 80<=x4[m5][0]<=85:
            sum11 = sum11 + x20[m5][0]
            js11 = js11 +1
        elif 85<x4[m5][0]<=95:
            sum12 = sum12 + x20[m5][0]
            js12 = js12 +1
        elif 95<x4[m5][0]<=100:
            sum13 = sum13 + x20[m5][0]
            js13 = js13 +1
        elif 100<x4[m5][0]<=105:
            sum14 = sum14 + x20[m5][0]
            js14 = js14 +1
        elif 105<x4[m5][0]<=110:
            sum15 = sum15 + x20[m5][0]
            js15 = js15 +1
    if 14.5<i5[0]<=15.5:
        if 80<=x4[m5][0]<=85:
            sum21 = sum21 + x20[m5][0]
            js21 = js21 +1
        elif 85<x4[m5][0]<=95:
            sum22 = sum22 + x20[m5][0]
            js22 = js22 +1
        elif 95<x4[m5][0]<=100:
            sum23 = sum23 + x20[m5][0]
            js23 = js23 +1
        elif 100<x4[m5][0]<=105:
            sum24 = sum24 + x20[m5][0]
            js24 = js24 +1
        elif 105<x4[m5][0]<=110:
            sum25 = sum25 + x20[m5][0]
            js25 = js25 +1
    if 15.5<i5[0]<=16.5:
        if 80<=x4[m5][0]<=85:
            sum31 = sum31 + x20[m5][0]
            js31 = js31 +1
        elif 85<x4[m5][0]<=95:
            sum32 = sum32 + x20[m5][0]
            js32 = js32 +1
        elif 95<x4[m5][0]<=100:
            sum33 = sum33 + x20[m5][0]
            js33 = js33 +1
        elif 100<x4[m5][0]<=105:
            sum34 = sum34 + x20[m5][0]
            js34 = js34 +1
        elif 105<x4[m5][0]<=110:
            sum35 = sum35 + x20[m5][0]
            js35 = js35 +1
    if 16.5<i5[0]<=17.5:
        if 80<=x4[m5][0]<=85:
            sum41 = sum41 + x20[m5][0]
            js41 = js41 +1
        elif 85<x4[m5][0]<=95:
            sum42 = sum42 + x20[m5][0]
            js42 = js42 +1
        elif 95<x4[m5][0]<=100:
            sum43 = sum43 + x20[m5][0]
            js43 = js43 +1
        elif 100<x4[m5][0]<=105:
            sum44 = sum44 + x20[m5][0]
            js44 = js44 +1
        elif 105<x4[m5][0]<=110:
            sum45 = sum45 + x20[m5][0]
            js45 = js45 +1

print([js11, js12, js13, js14, js15])
print([js21, js22, js23, js24, js25])
print([js31, js32, js33, js34, js35])
print([js41, js42, js43, js44, js45])


x1 = [85, 95, 100]
x2 = [85, 95, 100]
x3 = [85, 95, 100, 105]
x4 = [85, 95, 100, 105, 110]

y1 = [sum11/js11, sum12/js12, 0]
y2 = [0, sum22/js22, 0]
y3 = [sum31/js31, sum32/js32, sum33/js33, sum34/js34]
y4 = [sum41/js41, 0, sum43/js43, sum44/js44, sum45/js45]


plt.plot(x1, y1, label="小于80m", linestyle = '--')
plt.plot(x2, y2, label="小于10m", linestyle = '--')
plt.plot(x3, y3, label="小于10m", linestyle = '--')
plt.plot(x4, y4, label="小于10m", linestyle = '--')



plt.xlabel("船长 L(m) "+"（注：20代表耗时在(20,30]min间)")
plt.ylabel('用时 t(min)\n')
plt.title('船长与进厢时间关系图(上行)\n')

new_ticks = [85, 95, 100, 105, 110]
plt.xticks(new_ticks)
#plt.yticks(fontsize=18)
plt.legend(loc='upper right',ncol=2)
plt.savefig("同一船长、不同船宽用时均值(上行).jpg", dpi=200)
plt.show()
