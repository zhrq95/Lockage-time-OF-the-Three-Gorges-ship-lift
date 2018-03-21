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


x=[]
y=[]
for i in x21:
    x.append(i[0])
for i in x20:
    y.append(i[0])
plt.scatter(x, y)




plt.xlabel("L/B")
plt.ylabel('进出厢平均用时 t(min)\n')
plt.title('L/B与进出厢平均用时散点图(上行)\n')

new_ticks = range(2,8,1)
plt.xticks(new_ticks)
#plt.yticks(fontsize=18)
plt.legend(loc='upper left',ncol=1)
plt.savefig("L除B散点(上行).jpg", dpi=200)
plt.show()
