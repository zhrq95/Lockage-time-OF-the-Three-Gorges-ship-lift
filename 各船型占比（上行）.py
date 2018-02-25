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

#船型
x2 = []
for i in range(nrows1):
	if i == 0:
		continue
	x2.append(table1.row_values(i)[2:3])
print(x2)

js0, js1, js2, js3, js4 = 0, 0, 0, 0, 0 

for m,i in enumerate(x2):
    if i == ['客船']:
        js0 = js0 + 1
        sum = sum + 1
    elif i == ['商品车滚装船']:
        js1 = js1 + 1
        sum = sum + 1
    elif i == ['集装箱船']:
        js2 = js2 + 1
        sum = sum + 1
    elif i == ['货船']:
        js3 = js3 + 1
        sum = sum + 1
    elif i == ['小船']:
        js4 = js4 + 1
        sum = sum + 1

print(js0)
print(js1)
print(js2)
print(js3)
print(js4)
print(sum)

data = {
    '客船':(round(100*js0/sum, 2),  '#7199cf'),
    '商品车滚装船':(round(100*js1/sum, 2), '#7199cf'),
    '集装箱船': (round(100*js2/sum, 2), '#7199cf'),
    '货船': (round(100*js3/sum, 2), '#7199cf'),
    '其他': (round(100*js4/sum, 2), '#7199cf'),
}

船型 = data.keys()
比例= [x[0] for x in data.values()]
fontsizes = [x[1] for x in data.values()]

labels = ['{}:{}'.format(cx, str(bl)+'%') for cx, bl in zip(船型, 比例)]

fig, ax1 = plt.subplots(figsize=(6.4, 6.4))
ax1.set_title('各船型所占比例（上行）',fontsize='18')

ax1.pie(比例, labels=labels , shadow=True)

plt.savefig('各船型占比（上行）.jpg')
plt.show()