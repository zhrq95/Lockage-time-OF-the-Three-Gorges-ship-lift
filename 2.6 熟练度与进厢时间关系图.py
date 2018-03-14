import xlrd
import xlwt
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import spline
matplotlib.rcParams['font.sans-serif'] = ['SimHei']

Workbook = xlrd.open_workbook('a.xlsx')
wbk = xlwt.Workbook()
c = wbk.add_sheet('c',cell_overwrite_ok=True)
table1 = Workbook.sheets()[0]
nrows1 = table1.nrows

x9 = []
x16 = []
#进厢
for i in range(nrows1):
	if i == 0:
		continue
	x9.append(table1.row_values(i)[9:10])
print(x9)
# 出厢
for i in range(nrows1):
    if i == 0:
        continue
    x16.append(table1.row_values(i)[16:17])
print(x16)



x = np.array([0,  1, 2,  3])
fig, ax1 = plt.subplots()

# 2016.12进厢
ax1.bar(0-0.1, x9[0][0], 0.2, color='g',label = "进厢")
plt.text(0-0.1, x9[0][0] + 0.5, '%.2f' % ( x9[0][0]), ha='center', va='bottom', fontsize='8')
# 2016.12出厢
ax1.bar(0+0.1, x16[0][0], 0.2,color='r',label = "出厢")
plt.text(0+0.1, x16[0][0] + 0.5, '%.2f' % ( x16[0][0]), ha='center', va='bottom', fontsize='8')

# 2017.1进厢
ax1.bar(1-0.1, x9[1][0], 0.2, color='g')
plt.text(1-0.1, x9[1][0] + 0.5, '%.2f' % ( x9[1][0]), ha='center', va='bottom', fontsize='8')
# 2017.1出厢
ax1.bar(1+0.1, x16[1][0], 0.2,color='r')
plt.text(1+0.1, x16[1][0] + 0.5, '%.2f' % ( x16[1][0]), ha='center', va='bottom', fontsize='8')

# 2017.2进厢
ax1.bar(2-0.1, x9[2][0], 0.2, color='g')
plt.text(2-0.1, x9[2][0] + 0.5, '%.2f' % ( x9[2][0]), ha='center', va='bottom', fontsize='8')
# 2017.2出厢
ax1.bar(2+0.1, x16[2][0], 0.2,color='r')
plt.text(2+0.1, x16[2][0] + 0.5, '%.2f' % ( x16[2][0]), ha='center', va='bottom', fontsize='8')

# 2017.3进厢
ax1.bar(3-0.1, x9[3][0], 0.2, color='g')
plt.text(3-0.1, x9[3][0] + 0.5, '%.2f' % ( x9[3][0]), ha='center', va='bottom', fontsize='8')
# 2017.3出厢
ax1.bar(3+0.1, x16[3][0], 0.2,color='r')
plt.text(3+0.1, x16[3][0] + 0.5, '%.2f' % ( x16[3][0]), ha='center', va='bottom', fontsize='8')


plt.title('（兴晟05）通行频次与船舶进出厢历时(上行)\n')

plt.xticks(x, ('\n2016.11', '\n2017.1', '\n2017.1','\n2017.7'))
plt.ylabel('用时 t(min)\n')
plt.legend(loc = 'upper left')
plt.tight_layout()
plt.savefig("熟练度 - 兴晟05.jpg", dpi=200)
plt.show()
