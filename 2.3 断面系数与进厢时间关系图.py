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

x20 = []
x9 = []
# 断面系数
for i in range(nrows1):
	if i == 0:
		continue
	x20.append(table1.row_values(i)[20:21])
print(x20)
# 进厢时间
for i in range(nrows1):
    if i == 0:
        continue
    x9.append(table1.row_values(i)[9:10])
print(x9)



js11,js12,js13,js14,js15,js16,js17,js18,js19,js110,js111,js112=0,0,0,0,0,0,0,0,0,0,0,0
js21,js22,js23,js24,js25,js26,js27,js28,js29,js210,js211,js212=0,0,0,0,0,0,0,0,0,0,0,0
js31,js32,js33,js34,js35,js36,js37,js38,js39,js310,js311,js312=0,0,0,0,0,0,0,0,0,0,0,0

for m20,i20 in enumerate(x20):
    if i20[0]<=1.4:
        if 0<x9[m20][0]<=5:
            js11 = js11 + 1
        elif 5<x9[m20][0]<=10:
            js12 = js12 + 1
        elif 10<x9[m20][0]<=15:
            js13 = js13 + 1
        elif 15<x9[m20][0]<=20:
            js14 = js14 + 1
        elif 20<x9[m20][0]<=25:
            js15 = js15 + 1
        elif 25 < x9[m20][0] <= 30:
            js16 = js16 + 1
        elif 30 < x9[m20][0] <= 35:
            js17 = js17 + 1
        elif 35 < x9[m20][0] <= 40:
            js18 = js18 + 1
        elif 40 < x9[m20][0] <= 45:
            js19 = js19 + 1
        elif 45 < x9[m20][0] <= 50:
            js110 = js110 + 1
        elif 50 < x9[m20][0] <= 55:
            js111 = js111 + 1
        elif 55 < x9[m20][0] <= 60:
            js112 = js112 + 1
    elif 1.4<=i20[0]<=1.5:
        if 0<x9[m20][0]<=5:
            js21 = js21 + 1
        elif 5<x9[m20][0]<=10:
            js22 = js22 + 1
        elif 10<x9[m20][0]<=15:
            js23 = js23 + 1
        elif 15<x9[m20][0]<=20:
            js24 = js24 + 1
        elif 20<x9[m20][0]<=25:
            js25 = js25 + 1
        elif 25 < x9[m20][0] <= 30:
            js26 = js26 + 1
        elif 30 < x9[m20][0] <= 35:
            js27 = js27 + 1
        elif 35 < x9[m20][0] <= 40:
            js28 = js28 + 1
        elif 40 < x9[m20][0] <= 45:
            js29 = js29 + 1
        elif 45 < x9[m20][0] <= 50:
            js210 = js210 + 1
        elif 50 < x9[m20][0] <= 55:
            js211 = js211 + 1
        elif 55 < x9[m20][0] <= 60:
            js212 = js212 + 1
    elif 1.5<=i20[0]:
        if 0 < x9[m20][0] <= 5:
            js31 = js31 + 1
        elif 5 < x9[m20][0] <= 10:
            js32 = js32 + 1
        elif 10 < x9[m20][0] <= 15:
            js33 = js33 + 1
        elif 15 < x9[m20][0] <= 20:
            js34 = js34+ 1
        elif 20 < x9[m20][0] <= 25:
            js35 = js35 + 1
        elif 25 < x9[m20][0] <= 30:
            js36 = js36 + 1
        elif 30 < x9[m20][0] <= 35:
            js37 = js37 + 1
        elif 35 < x9[m20][0] <= 40:
            js38 = js38 + 1
        elif 40 < x9[m20][0] <= 45:
            js39 = js39 + 1
        elif 45 < x9[m20][0] <= 50:
            js310 = js310 + 1
        elif 50 < x9[m20][0] <= 55:
            js311 = js311 + 1
        elif 55 < x9[m20][0] <= 60:
            js312 = js312 + 1

print([js11, js12, js13, js14, js15, js16, js17, js18, js19, js110, js111,js112])
print([js21, js22, js23, js24, js25, js26, js27, js28, js29, js210, js211,js212])
print([js31, js32, js33, js34, js35, js36, js37, js38, js39, js310, js311,js312])

x1 = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
x2 = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
x3 = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]

js1 = js11 + js12 + js13 + js14 + js15 + js16 + js17 + js18 +js19 +js110 +js111 + js112
js2 = js21 + js22 + js23 + js24 + js25 + js26 + js27 + js28 +js29 +js210 +js211 + js212
js3 = js31 + js32 + js33 + js34 + js35 + js36 + js37 + js38 +js39 +js310 +js311 + js312

y1 = [100*js11/js1, 100*js12/js1, 100*js13/js1, 100*js14/js1, 100*js15/js1, 100*js16/js1, 100*js17/js1, 100*js18/js1, 100*js19/js1, 100*js110/js1]
y2 = [100*js21/js2, 100*js22/js2, 100*js23/js2, 100*js24/js2, 100*js25/js2, 100*js26/js2, 100*js27/js2, 100*js28/js2, 100*js29/js2, 100*js210/js2]
y3 = [100*js31/js3, 100*js32/js3, 100*js33/js3, 100*js34/js3, 100*js35/js3, 100*js36/js3, 100*js37/js3, 100*js38/js3, 100*js39/js3, 100*js310/js3]



x1 = np.array(x1)
x2 = np.array(x2)
x3 = np.array(x3)

xnew1 = np.linspace(x1.min(), x1.max(), 300)
xnew2 = np.linspace(x2.min(), x2.max(), 300)
xnew3 = np.linspace(x3.min(), x3.max(), 300)

power_smooth0 = spline(x1, y1, xnew1)
power_smooth1 = spline(x2, y2, xnew2)
power_smooth2 = spline(x3, y3, xnew3)



def 去负数(power_smooth, num):
    global smooth
    smooth =[]
    for i in power_smooth:
        if i >= 0:
            smooth.append(i)
        else:
            i = 0
            smooth.append(i)
去负数(power_smooth0,0)
smooth0 = smooth
去负数(power_smooth1,1)
smooth1 = smooth
去负数(power_smooth2,2)
smooth2 = smooth



plt.plot(xnew1, smooth0, label="不超过1.4", linestyle = '-')
plt.plot(xnew2, smooth1, label="1.4-1.5", linestyle = '-')
plt.plot(xnew3, smooth2, label="大于1.5", linestyle = '-',lw=3.5,color='r')


plt.xlabel("进厢用时 t(min)", fontsize=12)
plt.ylabel('概率密度 %', fontsize=12)
plt.title('断面系数与进厢时间关系图(上行)\n', fontsize=15)

new_ticks = [5, 10, 15, 20, 25, 30, 35, 40, 45]
plt.xticks(new_ticks)
plt.yticks(fontsize=12)
plt.legend(loc='upper right',ncol=1)
plt.savefig("进厢 — 各断面系数时间关系图(上行).jpg", dpi=200)
plt.show()


