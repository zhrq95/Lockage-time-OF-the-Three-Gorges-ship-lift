# 光滑曲线
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

x5 = []
x9 = []
for i in range(nrows1):
	if i == 0:
		continue
	x5.append(table1.row_values(i)[5:6])
print(x5)
for i in range(nrows1):
    if i == 0:
        continue
    x9.append(table1.row_values(i)[9:10])
print(x9)

dd = []
for t in range(0,54,3):
    cc = []
    for B in [11, 14, 16.3, 17.2]:
        js = 0
        for m5,i5 in enumerate(x5):
            if B == 11:
                if t == 50:
                    if (float(x5[m5][0])<=B) and (float(x9[m5][0])>t-3):
                        js = js + 1
                else:
                    if (float(x5[m5][0])<=B) and (float(x9[m5][0])>t-3 and float(x9[m5][0])<=t):
                        js = js + 1
            elif B == 17.2:
                if t == 50:
                    if (float(x5[m5][0])>=B-0.9 and float(x5[m5][0])<=B) and (float(x9[m5][0])>t-3):
                        js = js + 1
                else:
                    if (float(x5[m5][0])>=B-0.9 and float(x5[m5][0])<=B) and (float(x9[m5][0])>t-3 and float(x9[m5][0])<=t):
                        js = js + 1
            elif B == 16.3:
                if t == 50:
                    if (float(x5[m5][0]) >= B - 2.3 and float(x5[m5][0]) <= B) and (float(x9[m5][0]) > t - 3):
                        js = js + 1
                else:
                    if (float(x5[m5][0]) >= B - 2.3 and float(x5[m5][0]) <= B) and (float(x9[m5][0]) > t - 3 and float(x9[m5][0]) <= t):
                        js = js + 1
            elif B == 14:
                if t == 50:
                    if (float(x5[m5][0])>=B-3 and float(x5[m5][0])<=B) and (float(x9[m5][0])>t-3):
                        js = js + 1
                else:
                    if (float(x5[m5][0])>=B-3 and float(x5[m5][0])<=B) and (float(x9[m5][0])>t-3 and float(x9[m5][0])<=t):
                        js = js + 1

        cc.append(js)
    #print(cc)
    dd.append(cc)
dd = np.array(dd)
print(dd)

zxsum = np.sum(dd,axis=0)
hxsum = np.sum(dd,axis=1)
print(zxsum)

gl = dd/zxsum
gl = gl.T

print(sum(sum(gl)))

y0 = gl[0]*100
y1 = gl[1]*100
y2 = gl[2]*100
y3 = gl[3]*100


print(y0)


#plt.figure(figsize=(12.8,9.6))

x = list(range(0,54,3))
x = np.array(x)
xnew = np.linspace(x.min(), x.max(),200)
power_smooth0 = spline(x, y0, xnew)
power_smooth1 = spline(x, y1, xnew)
power_smooth2 = spline(x, y2, xnew)
power_smooth3 = spline(x, y3, xnew)

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
去负数(power_smooth3,3)
smooth3 = smooth

plt.plot(xnew, smooth0, label="不超过11m", linestyle = '-',color='g')
plt.plot(xnew, smooth1, label="11-14m", linestyle = '-',color='y')
plt.plot(xnew, smooth2, label="14-16.3m", linestyle = '-',color='black')
plt.plot(xnew, smooth3, label="超过16.3m", linestyle = '-',color='b')


plt.xlabel("用时 t(min)",fontsize=12)
plt.ylabel('概率密度 %',fontsize=12)
plt.title('船宽与进厢时间关系图(上行)\n',fontsize=15)

new_ticks = range(0,54,3)
plt.xticks(new_ticks,fontsize=12)
plt.yticks(fontsize=12)
plt.legend(loc='upper right',ncol=1)
plt.savefig("船宽与进厢时间关系图(上行).jpg", dpi=200)
plt.show()
