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

js11,js12,js13,js14= 0,0,0,0
sum11,sum12,sum13,sum14= 0,0,0,0
js21,js22,js23,js24= 0,0,0,0
sum21,sum22,sum23,sum24 = 0,0,0,0
js31,js32,js33,js34= 0,0,0,0
sum31,sum32,sum33,sum34= 0,0,0,0
js41,js42,js43,js44= 0,0,0,0
sum41,sum42,sum43,sum44 = 0,0,0,0
js51,js52,js53,js54= 0,0,0,0
sum51,sum52,sum53,sum54= 0,0,0,0
js61,js62,js63,js64=0,0,0,0
sum61,sum62,sum63,sum64 = 0,0,0,0
for m4,i4 in enumerate(x4):
    if 80<=i4[0]<=85:
        if 14<=x5[m4][0]<=14.5:
            sum11 = sum11 + x20[m4][0]
            js11 = js11 +1
        elif 14.5<x5[m4][0]<=15.5:
            sum12 = sum12 + x20[m4][0]
            js12 = js12 +1
        elif 15.5<x5[m4][0]<=16.5:
            sum13 = sum13 + x20[m4][0]
            js13 = js13 +1
        elif 16.5<x5[m4][0]<=17.2:
            sum14 = sum14 + x20[m4][0]
            js14 = js14 +1
    if 85<=i4[0]<=90:
        if 14<=x5[m4][0]<=14.5:
            sum21 = sum21 + x20[m4][0]
            js21 = js21 +1
        elif 14.5<x5[m4][0]<=15.5:
            sum22 = sum22 + x20[m4][0]
            js22 = js22 +1
        elif 15.5<x5[m4][0]<=16.5:
            sum23 = sum23 + x20[m4][0]
            js23 = js23 +1
        elif 16.5<x5[m4][0]<=17.2:
            sum24 = sum24 + x20[m4][0]
            js24 = js24 +1
    if 90<=i4[0]<=95:
        if 14<=x5[m4][0]<=14.5:
            sum31 = sum31 + x20[m4][0]
            js31 = js31 +1
        elif 14.5<x5[m4][0]<=15.5:
            sum32 = sum32 + x20[m4][0]
            js32 = js32 +1
        elif 15.5<x5[m4][0]<=16.5:
            sum33 = sum33 + x20[m4][0]
            js33 = js33 +1
        elif 16.5<x5[m4][0]<=17.2:
            sum34 = sum34 + x20[m4][0]
            js34 = js34 +1
    if 95<=i4[0]<=100:
        if 14<=x5[m4][0]<=14.5:
            sum41 = sum41 + x20[m4][0]
            js41 = js41 +1
        elif 14.5<x5[m4][0]<=15.5:
            sum42 = sum42 + x20[m4][0]
            js42 = js42 +1
        elif 15.5<x5[m4][0]<=16.5:
            sum43 = sum43 + x20[m4][0]
            js43 = js43 +1
        elif 16.5<x5[m4][0]<=17.2:
            sum44 = sum44 + x20[m4][0]
            js44 = js44 +1
    if 100<=i4[0]<=105:
        if 14<=x5[m4][0]<=14.5:
            sum51 = sum51 + x20[m4][0]
            js51 = js51 +1
        elif 14.5<x5[m4][0]<=15.5:
            sum52 = sum52 + x20[m4][0]
            js52 = js52 +1
        elif 15.5<x5[m4][0]<=16.5:
            sum53 = sum53 + x20[m4][0]
            js53 = js53 +1
        elif 16.5<x5[m4][0]<=17.2:
            sum54 = sum54 + x20[m4][0]
            js54 = js54 +1
    if 105<=i4[0]<=110:
        if 14<=x5[m4][0]<=14.5:
            sum61 = sum61 + x20[m4][0]
            js61 = js61 +1
        elif 14.5<x5[m4][0]<=15.5:
            sum62 = sum62 + x20[m4][0]
            js62 = js62 +1
        elif 15.5<x5[m4][0]<=16.5:
            sum63 = sum63 + x20[m4][0]
            js63 = js63 +1
        elif 16.5<x5[m4][0]<=17.2:
            sum64 = sum64 + x20[m4][0]
            js64 = js64 +1


print([js11, js12, js13, js14])
print([js21, js22, js23, js24])
print([js31, js32, js33, js34])
print([js41, js42, js43, js44])
print([js51, js52, js53, js54])
print([js61, js62, js63, js64])

x = [14.5, 15.5, 16.5, 17.2]
x1 = [14.5,       16.5, 17.2]
x2 = [14.5, 15.5, 16.5      ]
x3 = [      15.5, 16.5      ]
x4 = [            16.5, 17.2]
x5 = [            16.5, 17.2]
x6 = [            16.5, 17.2]






y1 = [sum11/js11, sum13/js13, sum14/js14]
y2 = [sum21/js21, sum22/js22, sum23/js23]
y3 = [sum32/js32, sum33/js33]
y4 = [sum43/js43, sum44/js44]
y5 = [sum53/js53, sum54/js54]
y6 = [sum63/js63, sum64/js64]

plt.plot(x1, y1, label="(80,85]m", linestyle = '--')
plt.plot(x2, y2, label="(85,90]m", linestyle = '--')
plt.plot(x3, y3, label="(90,95]m", linestyle = '--')
plt.plot(x4, y4, label="(95,100]m", linestyle = '--')
plt.plot(x5, y5, label="(100,105]m", linestyle = '--')
plt.plot(x6, y6, label="(105,110]m", linestyle = '--')


plt.xlabel("船宽 B(m)")
plt.ylabel('用时 t(min)\n')
plt.title('同一船宽、不同船长用时均值(上行)\n')

new_ticks = [14.5, 15.5, 16.5, 17.2]
plt.xticks(new_ticks)
#plt.yticks(fontsize=18)
plt.legend(loc='upper left',ncol=2)
plt.savefig("同一船宽、不同船长用时均值(上行).jpg", dpi=200)
plt.show()
