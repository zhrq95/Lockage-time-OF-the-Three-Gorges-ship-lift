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

x4 = []
x5 = []
x9 = []
for i in range(nrows1):
	if i == 0:
		continue
	x4.append(table1.row_values(i)[4:5])
print(x4)
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
for t in range(0,50,10):
    cc = []
    for L in [90,100,110]:
        js = 0
        for m4,i4 in enumerate(x4):
            if t == 40:
                if (L-10<float(x4[m4][0])<=L) and (16<float(x5[m4][0])<=17.2) and (float(x9[m4][0])>t):
                    js = js + 1
            else:
                if (L-10<float(x4[m4][0])<=L) and (16<float(x5[m4][0])<=17.2) and (t<float(x9[m4][0])<=t+10):
                    js = js + 1

        cc.append(js)
    #print(cc)
    dd.append(cc)
dd = np.array(dd)
print(dd)

zxsum = np.sum(dd,axis=0)
hxsum = np.sum(dd,axis=1)
print(zxsum)

gl = dd/zxsum/3
gl = gl.T

print(sum(sum(gl)))

y0 = gl[0]*100
y1 = gl[1]*100
y2 = gl[2]*100




print(y0)



#plt.figure(figsize=(12.8,9.6))

x = list(range(0,50,10))
x = np.array(x)
xnew = np.linspace(x.min(), x.max(), 300)
power_smooth0 = spline(x, y0, xnew)
power_smooth1 = spline(x, y1, xnew)
power_smooth2 = spline(x, y2, xnew)


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





plt.plot(xnew, smooth0, label="船宽:(16,17.2]；船长:(80,90]", linestyle = '--')
plt.plot(xnew, smooth1, label="船宽:(16,17.2]；船长:(90,100]", linestyle = '--')
plt.plot(xnew, smooth2, label="船宽:(16,17.2]；船长:(100,110]", linestyle = '--')



plt.xlabel("耗时 t(min) "+"（注：20代表耗时在(20,30]min间)")
plt.ylabel('概率密度 %\n')
plt.title('船长*宽与进厢时间关系图2(上行)\n')

new_ticks = range(0,50,10)
plt.xticks(new_ticks)
#plt.yticks(fontsize=18)
plt.legend(loc='upper left',ncol=1)
plt.savefig("(16，17.2]船长x宽与进厢时间关系图(上行).jpg", dpi=200)
plt.show()
