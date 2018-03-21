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


x21 = []
x20 = []
# 船长/船宽
for i in range(nrows1):
    if i == 0:
        continue
    x21.append(table1.row_values(i)[21:22])
print(x21)
# 进厢 + 出厢 时间
for i in range(nrows1):
    if i == 0:
        continue
    x20.append(table1.row_values(i)[20:21])
print(x20)

sum1,sum2,sum3,sum4,sum5,sum6,sum7,sum8=0,0,0,0,0,0,0,0
js1,js2,js3,js4,js5,js6,js7,js8=0,0,0,0,0,0,0,0

sum9,sum10,sum11,sum12,sum13,sum14,sum15,sum16=0,0,0,0,0,0,0,0
js9,js10,js11,js12,js13,js14,js15,js16=0,0,0,0,0,0,0,0

for m21,i21 in enumerate(x21):
    if 0<i21[0]<=0.5:
        sum1 = sum1 + x20[m21][0]
        js1 = js1 + 1
    elif 0.5<i21[0]<=1:
        sum2 = sum2 + x20[m21][0]
        js2 = js2 + 1
    elif 1<i21[0]<=1.5:
        sum3 = sum3 + x20[m21][0]
        js3 = js3 + 1
    elif 1.5<i21[0]<=2:
        sum4 = sum4 + x20[m21][0]
        js4 = js4 + 1
    elif 2<i21[0]<=2.5:
        sum5 = sum5 + x20[m21][0]
        js5 = js5 + 1
    elif 2.5<i21[0]<=3:
        sum6 = sum6 + x20[m21][0]
        js6 = js6 + 1
    elif 3<i21[0]<=3.5:
        sum7 = sum7 + x20[m21][0]
        js7 = js7 + 1
    elif 3.5<i21[0]<=4:
        sum8 = sum8 + x20[m21][0]
        js8 = js8 + 1
    elif 4<i21[0]<=4.5:
        sum9 = sum9+ x20[m21][0]
        js9 = js9 + 1
    elif 4.5<i21[0]<=5:
        sum10 = sum10 + x20[m21][0]
        js10 = js10 + 1
    elif 5<i21[0]<=5.5:
        sum11 = sum11 + x20[m21][0]
        js11 = js11 + 1
    elif 5.5<i21[0]<=6:
        sum12 = sum12 + x20[m21][0]
        js12 = js12 + 1
    elif 6<i21[0]<=6.5:
        sum13 = sum13 + x20[m21][0]
        js13 = js13 + 1
    elif 6.5<i21[0]<=7:
        sum14 = sum14 + x20[m21][0]
        js14 = js14 + 1
    elif 7<i21[0]<=7.5:
        sum15 = sum15 + x20[m21][0]
        js15 = js15 + 1
    elif 7.5<i21[0]<=8:
        sum16 = sum16 + x20[m21][0]
        js16 = js16 + 1



print([js1,js2,js3,js4,js5,js6,js7,js8,js9,js10,js11,js12,js13,js14,js15,js16])

x = [4, 4.5, 5, 5.5, 6, 6.5]

y = [sum8/js8, sum9/js9, sum10/js10, sum11/js11, sum12/js12, sum13/js13]
plt.plot(x, y, linestyle = '--')




plt.xlabel("L/B")
plt.ylabel('进出厢平均用时 t(min)\n')
plt.title('L/B与进出厢平均用时关系图(上行)\n')

new_ticks = [3.5, 4, 4.5, 5, 5.5, 6, 6.5]
plt.xticks(new_ticks)
#plt.yticks(fontsize=18)
plt.legend(loc='upper left',ncol=1)
plt.savefig("L除B(上行).jpg", dpi=200)
plt.show()
