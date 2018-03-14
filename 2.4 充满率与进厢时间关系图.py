'''
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
# 充满率
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



js11,js12,js13,js14,js15,js16,js17,js18,js19,js110=0,0,0,0,0,0,0,0,0,0
js21,js22,js23,js24,js25,js26,js27,js28,js29,js210=0,0,0,0,0,0,0,0,0,0
js31,js32,js33,js34,js35,js36,js37,js38,js39,js310=0,0,0,0,0,0,0,0,0,0
js41,js42,js43,js44,js45,js46,js47,js48,js49,js410=0,0,0,0,0,0,0,0,0,0

for m20,i20 in enumerate(x20):
    if i20[0]<=0.6:
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
        elif 25<x9[m20][0]<=30:
            js16 = js16 + 1
        elif 30<x9[m20][0]<=35:
            js17 = js17 + 1
        elif 35<x9[m20][0]<=40:
            js18 = js18 + 1
        elif 40<x9[m20][0]<=45:
            js19 = js19 + 1
        elif 45<x9[m20][0]<=50:
            js110 = js110 + 1
    elif 0.6<i20[0]<=0.7:
        if 0 < x9[m20][0] <= 5:
            js21 = js21 + 1
        elif 5 < x9[m20][0] <= 10:
            js22 = js22 + 1
        elif 10 < x9[m20][0] <= 15:
            js23 = js23 + 1
        elif 15 < x9[m20][0] <= 20:
            js24 = js24+ 1
        elif 20 < x9[m20][0] <= 25:
            js25 = js25 + 1
        elif 25 < x9[m20][0] <= 30:
            js26 = js26 + 1
        elif 30 < x9[m20][0] <= 35:
            js27 = js27 + 1
        elif 35 < x9[m20][0] <= 40:
            js28 = js28+ 1
        elif 40 < x9[m20][0] <= 45:
            js29 = js29 + 1
        elif 45 < x9[m20][0] <= 50:
            js210 = js210 + 1
    elif 0.7 < i20[0] <= 0.8:
        if 0 < x9[m20][0] <= 5:
            js31 = js31 + 1
        elif 5 < x9[m20][0] <= 10:
            js32 = js32 + 1
        elif 10 < x9[m20][0] <= 15:
            js33 = js33 + 1
        elif 15 < x9[m20][0] <= 20:
            js34 = js34 + 1
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
    elif 0.8< i20[0]:
        if 0 < x9[m20][0] <= 5:
            js41 = js41 + 1
        elif 5 < x9[m20][0] <= 10:
            js42 = js42 + 1
        elif 10 < x9[m20][0] <= 15:
            js43 = js43 + 1
        elif 15 < x9[m20][0] <= 20:
            js44 = js44 + 1
        elif 20 < x9[m20][0] <= 25:
            js45 = js45 + 1
        elif 25 < x9[m20][0] <= 30:
            js46 = js46 + 1
        elif 30 < x9[m20][0] <= 35:
            js47 = js47 + 1
        elif 35 < x9[m20][0] <= 40:
            js48 = js48 + 1
        elif 40 < x9[m20][0] <= 45:
            js49 = js49 + 1
        elif 45 < x9[m20][0] <= 50:
            js410 = js410 + 1

print([js11, js12, js13, js14, js15, js16, js17, js18, js19, js110])
print([js21, js22, js23, js24, js25, js26, js27, js28, js29, js210])
print([js31, js32, js33, js34, js35, js36, js37, js38, js39, js310])
print([js41, js42, js43, js44, js45, js46, js47, js48, js49, js410])

x1 = [5, 10, 15, 20, 25, 30, 35, 40, 45]
x2 = [5, 10, 15, 20, 25, 30, 35, 40, 45]
x3 = [15, 20, 25, 30, 35, 40, 45]
x4 = [25, 30, 35, 40, 45]

js1 = js11 + js12 + js13 + js14 + js15 + js16 + js17 +js18 + js19 + js110
js2 = js21 + js22 + js23 + js24 + js25 + js26 + js27 +js28 + js29 + js210
js3 = js31 + js32 + js33 + js34 + js35 + js36 + js37 +js38 + js39 + js310
js4 = js41 + js42 + js43 + js44 + js45 + js46 + js47 +js48 + js49 + js410

y1 = [100*js11/js1, 100*js12/js1, 100*js13/js1, 100*js14/js1, 100*js15/js1, 100*js16/js1, 100*js17/js1, 100*js18/js1, 100*js19/js1]
y2 = [100*js21/js2, 100*js22/js2, 100*js23/js2, 100*js24/js2, 100*js25/js2, 100*js26/js2, 100*js27/js2, 100*js28/js2, 100*js29/js2]
y3 = [100*js33/js3, 100*js34/js3, 100*js35/js3, 100*js36/js3, 100*js37/js3, 100*js38/js3, 100*js39/js3]
y4 = [100*js45/js4, 100*js46/js4, 100*js47/js4, 100*js48/js4, 100*js49/js4]

plt.plot(x1, y1, label="小于0.6", linestyle = '--')
plt.plot(x2, y2, label="(0.6,0.7]", linestyle = '--')
plt.plot(x3, y3, label="(0.7,0.8]", linestyle = '--')
plt.plot(x4, y4, label="大于0.8", linestyle = '--')

plt.xlabel("用时 t(min)")
plt.ylabel('概率密度 %\n')
plt.title('充满率与进厢时间关系图(上行进厢)\n')

new_ticks = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
plt.xticks(new_ticks)
#plt.yticks(fontsize=18)
plt.legend(loc='upper right',ncol=1)
plt.savefig("进厢 — 充满率时间关系图(上行).jpg", dpi=200)
plt.show()
'''


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
# 充满率
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



js11,js12,js13,js14,js15,js16,js17,js18,js19,js110 = 0,0,0,0,0,0,0,0,0,0
js111,js112,js113,js114,js115,js116,js117 = 0,0,0,0,0,0,0

js21,js22,js23,js24,js25,js26,js27,js28,js29,js210=0,0,0,0,0,0,0,0,0,0
js211,js212,js213,js214,js215,js216,js217 = 0,0,0,0,0,0,0

js31,js32,js33,js34,js35,js36,js37,js38,js39,js310=0,0,0,0,0,0,0,0,0,0
js311,js312,js313,js314,js315,js316,js317 = 0,0,0,0,0,0,0

js41,js42,js43,js44,js45,js46,js47,js48,js49,js410=0,0,0,0,0,0,0,0,0,0
js411,js412,js413,js414,js415,js416,js417 = 0,0,0,0,0,0,0

js51,js52,js53,js54,js55,js56,js57,js58,js59,js510=0,0,0,0,0,0,0,0,0,0
js511,js512,js513,js514,js515,js516,js517 = 0,0,0,0,0,0,0

js61,js62,js63,js64,js65,js66,js67,js68,js69,js610=0,0,0,0,0,0,0,0,0,0
js611,js612,js613,js614,js615,js616,js617 = 0,0,0,0,0,0,0

js71,js72,js73,js74,js75,js76,js77,js78,js79,js710=0,0,0,0,0,0,0,0,0,0
js711,js712,js713,js714,js715,js716,js717 = 0,0,0,0,0,0,0

for m20,i20 in enumerate(x20):
    if i20[0]<=0.6:
        if 0<x9[m20][0]<=3:
            js11 = js11 + 1
        elif 3<x9[m20][0]<=6:
            js12 = js12 + 1
        elif 6<x9[m20][0]<=9:
            js13 = js13 + 1
        elif 9<x9[m20][0]<=12:
            js14 = js14 + 1
        elif 12<x9[m20][0]<=15:
            js15 = js15 + 1
        elif 15<x9[m20][0]<=18:
            js16 = js16 + 1
        elif 18<x9[m20][0]<=21:
            js17 = js17 + 1
        elif 21<x9[m20][0]<=24:
            js18 = js18 + 1
        elif 24<x9[m20][0]<=27:
            js19 = js19 + 1
        elif 27<x9[m20][0]<=30:
            js110 = js110 + 1
        elif 30<x9[m20][0]<=33:
            js111 = js111 + 1
        elif 33<x9[m20][0]<=36:
            js112 = js112 + 1
        elif 36<x9[m20][0]<=39:
            js113 = js113 + 1
        elif 39<x9[m20][0]<=42:
            js114 = js114 + 1
        elif 42<x9[m20][0]<=45:
            js115 = js115 + 1
        elif 45<x9[m20][0]<=48:
            js116 = js116 + 1
        elif 48<x9[m20][0]<=51:
            js117 = js117 + 1
    elif 0.6<i20[0]<=0.65:
        if 0<x9[m20][0]<=3:
            js21 = js21 + 1
        elif 3<x9[m20][0]<=6:
            js22 = js22 + 1
        elif 6<x9[m20][0]<=9:
            js23 = js23 + 1
        elif 9<x9[m20][0]<=12:
            js24 = js24 + 1
        elif 12<x9[m20][0]<=15:
            js25 = js25 + 1
        elif 15<x9[m20][0]<=18:
            js26 = js26 + 1
        elif 18<x9[m20][0]<=21:
            js27 = js27 + 1
        elif 21<x9[m20][0]<=24:
            js28 = js28 + 1
        elif 24<x9[m20][0]<=27:
            js29 = js29 + 1
        elif 27<x9[m20][0]<=30:
            js210 = js210 + 1
        elif 30<x9[m20][0]<=33:
            js211 = js211 + 1
        elif 33<x9[m20][0]<=36:
            js212 = js212 + 1
        elif 36<x9[m20][0]<=39:
            js213 = js213 + 1
        elif 39<x9[m20][0]<=42:
            js214 = js214 + 1
        elif 42<x9[m20][0]<=45:
            js215 = js215 + 1
        elif 45<x9[m20][0]<=48:
            js216 = js216 + 1
        elif 48<x9[m20][0]<=51:
            js217 = js217 + 1
    elif 0.65 < i20[0] <= 0.7:
        if 0<x9[m20][0]<=3:
            js31 = js31 + 1
        elif 3<x9[m20][0]<=6:
            js32 = js32 + 1
        elif 6<x9[m20][0]<=9:
            js33 = js33 + 1
        elif 9<x9[m20][0]<=12:
            js34 = js34 + 1
        elif 12<x9[m20][0]<=15:
            js35 = js35 + 1
        elif 15<x9[m20][0]<=18:
            js36 = js36 + 1
        elif 18<x9[m20][0]<=21:
            js37 = js37 + 1
        elif 21<x9[m20][0]<=24:
            js38 = js38 + 1
        elif 24<x9[m20][0]<=27:
            js39 = js39 + 1
        elif 27<x9[m20][0]<=30:
            js310 = js310 + 1
        elif 30<x9[m20][0]<=33:
            js311 = js311 + 1
        elif 33<x9[m20][0]<=36:
            js312 = js312 + 1
        elif 36<x9[m20][0]<=39:
            js313 = js313 + 1
        elif 39<x9[m20][0]<=42:
            js314 = js314 + 1
        elif 42<x9[m20][0]<=45:
            js315 = js315 + 1
        elif 45<x9[m20][0]<=48:
            js316 = js316 + 1
        elif 48<x9[m20][0]<=51:
            js317 = js317 + 1
    elif 0.7< i20[0]<0.75:
        if 0<x9[m20][0]<=3:
            js41 = js41 + 1
        elif 3<x9[m20][0]<=6:
            js42 = js42 + 1
        elif 6<x9[m20][0]<=9:
            js43 = js43 + 1
        elif 9<x9[m20][0]<=12:
            js44 = js44 + 1
        elif 12<x9[m20][0]<=15:
            js45 = js45 + 1
        elif 15<x9[m20][0]<=18:
            js46 = js46 + 1
        elif 18<x9[m20][0]<=21:
            js47 = js47 + 1
        elif 21<x9[m20][0]<=24:
            js48 = js48 + 1
        elif 24<x9[m20][0]<=27:
            js49 = js49 + 1
        elif 27<x9[m20][0]<=30:
            js410 = js410 + 1
        elif 30<x9[m20][0]<=33:
            js411 = js411 + 1
        elif 33<x9[m20][0]<=36:
            js412 = js412 + 1
        elif 36<x9[m20][0]<=39:
            js413 = js413 + 1
        elif 39<x9[m20][0]<=42:
            js414 = js414 + 1
        elif 42<x9[m20][0]<=45:
            js415 = js415 + 1
        elif 45<x9[m20][0]<=48:
            js416 = js416 + 1
        elif 48<x9[m20][0]<=51:
            js417 = js417 + 1
    elif 0.75 < i20[0] < 0.80:
        if 0<x9[m20][0]<=3:
            js51 = js51 + 1
        elif 3<x9[m20][0]<=6:
            js52 = js52 + 1
        elif 6<x9[m20][0]<=9:
            js53 = js53 + 1
        elif 9<x9[m20][0]<=12:
            js54 = js54 + 1
        elif 12<x9[m20][0]<=15:
            js55 = js55 + 1
        elif 15<x9[m20][0]<=18:
            js56 = js56 + 1
        elif 18<x9[m20][0]<=21:
            js57 = js57 + 1
        elif 21<x9[m20][0]<=24:
            js58 = js58 + 1
        elif 24<x9[m20][0]<=27:
            js59 = js59 + 1
        elif 27<x9[m20][0]<=30:
            js510 = js510 + 1
        elif 30<x9[m20][0]<=33:
            js511 = js511 + 1
        elif 33<x9[m20][0]<=36:
            js512 = js512 + 1
        elif 36<x9[m20][0]<=39:
            js513 = js513 + 1
        elif 39<x9[m20][0]<=42:
            js514 = js514 + 1
        elif 42<x9[m20][0]<=45:
            js515 = js515 + 1
        elif 45<x9[m20][0]<=48:
            js516 = js516 + 1
        elif 48<x9[m20][0]<=51:
            js517 = js517 + 1
    elif 0.80 < i20[0] < 0.85:
        if 0<x9[m20][0]<=3:
            js61 = js61 + 1
        elif 3<x9[m20][0]<=6:
            js62 = js62 + 1
        elif 6<x9[m20][0]<=9:
            js63 = js63 + 1
        elif 9<x9[m20][0]<=12:
            js64 = js64 + 1
        elif 12<x9[m20][0]<=15:
            js65 = js65 + 1
        elif 15<x9[m20][0]<=18:
            js66 = js66 + 1
        elif 18<x9[m20][0]<=21:
            js67 = js67 + 1
        elif 21<x9[m20][0]<=24:
            js68 = js68 + 1
        elif 24<x9[m20][0]<=27:
            js69 = js69 + 1
        elif 27<x9[m20][0]<=30:
            js610 = js610 + 1
        elif 30<x9[m20][0]<=33:
            js611 = js611 + 1
        elif 33<x9[m20][0]<=36:
            js612 = js612 + 1
        elif 36<x9[m20][0]<=39:
            js613 = js613 + 1
        elif 39<x9[m20][0]<=42:
            js614 = js614 + 1
        elif 42<x9[m20][0]<=45:
            js615 = js615 + 1
        elif 45<x9[m20][0]<=48:
            js616 = js616 + 1
        elif 48<x9[m20][0]<=51:
            js617 = js617 + 1
    elif 0.85 <= i20[0]:
        if 0<x9[m20][0]<=3:
            js71 = js71 + 1
        elif 3<x9[m20][0]<=6:
            js72 = js72 + 1
        elif 6<x9[m20][0]<=9:
            js73 = js73 + 1
        elif 9<x9[m20][0]<=12:
            js74 = js74 + 1
        elif 12<x9[m20][0]<=15:
            js75 = js75 + 1
        elif 15<x9[m20][0]<=18:
            js76 = js76 + 1
        elif 18<x9[m20][0]<=21:
            js77 = js77 + 1
        elif 21<x9[m20][0]<=24:
            js78 = js78 + 1
        elif 24<x9[m20][0]<=27:
            js79 = js79 + 1
        elif 27<x9[m20][0]<=30:
            js710 = js710 + 1
        elif 30<x9[m20][0]<=33:
            js711 = js711 + 1
        elif 33<x9[m20][0]<=36:
            js712 = js712 + 1
        elif 36<x9[m20][0]<=39:
            js713 = js713 + 1
        elif 39<x9[m20][0]<=42:
            js714 = js714 + 1
        elif 42<x9[m20][0]<=45:
            js715 = js715 + 1
        elif 45<x9[m20][0]<=48:
            js716 = js716 + 1
        elif 48<x9[m20][0]<=51:
            js717 = js717 + 1

print([js11, js12, js13, js14, js15, js16, js17, js18, js19, js110, js111, js112, js113, js114, js115, js116, js117])
print([js21, js22, js23, js24, js25, js26, js27, js28, js29, js210, js211, js212, js213, js214, js215, js216, js217])
print([js31, js32, js33, js34, js35, js36, js37, js38, js39, js310, js311, js312, js313, js314, js315, js316, js317])
print([js41, js42, js43, js44, js45, js46, js47, js48, js49, js410, js411, js412, js413, js414, js415, js416, js417])
print([js51, js52, js53, js54, js55, js56, js57, js58, js59, js510, js511, js512, js513, js514, js515, js516, js517])
print([js61, js62, js63, js64, js65, js66, js67, js68, js69, js610, js611, js612, js613, js614, js615, js616, js617])
print([js71, js72, js73, js74, js75, js76, js77, js78, js79, js710, js711, js712, js713, js714, js715, js716, js717])


x1 = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51]
x2 = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51]
x3 = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51]
x4 = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51]
x5 = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51]
x6 = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51]
x7 = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51]

js1 = js11 + js12 + js13 + js14 + js15 + js16 + js17 +js18 + js19 + js110 + js111 + js112 + js113 + js114 + js115 + js116 + js117
js2 = js21 + js22 + js23 + js24 + js25 + js26 + js27 +js28 + js29 + js210 + js211 + js212 + js213 + js214 + js215 + js216 + js217
js3 = js31 + js32 + js33 + js34 + js35 + js36 + js37 +js38 + js39 + js310 + js311 + js312 + js313 + js314 + js315 + js316 + js317
js4 = js41 + js42 + js43 + js44 + js45 + js46 + js47 +js48 + js49 + js410 + js411 + js412 + js413 + js414 + js415 + js416 + js417
js5 = js51 + js52 + js53 + js54 + js55 + js56 + js57 +js58 + js59 + js510 + js511 + js512 + js513 + js514 + js515 + js516 + js517
js6 = js61 + js62 + js63 + js64 + js65 + js66 + js67 +js68 + js69 + js610 + js611 + js612 + js613 + js614 + js615 + js616 + js617
js7 = js71 + js72 + js73 + js74 + js75 + js76 + js77 +js78 + js79 + js710 + js711 + js712 + js713 + js714 + js715 + js716 + js717

y1 = [100*js11/js1, 100*js12/js1, 100*js13/js1, 100*js14/js1, 100*js15/js1, 100*js16/js1, 100*js17/js1, 100*js18/js1, 100*js19/js1, 100*js110/js1, 100*js111/js1, 100*js112/js1, 100*js113/js1, 100*js114/js1, 100*js115/js1, 100*js116/js1, 100*js117/js1]
y2 = [100*js21/js2, 100*js22/js2, 100*js23/js2, 100*js24/js2, 100*js25/js2, 100*js26/js2, 100*js27/js2, 100*js28/js2, 100*js29/js2, 100*js210/js2, 100*js211/js2, 100*js212/js2, 100*js213/js2, 100*js214/js2, 100*js215/js2, 100*js216/js2, 100*js217/js2]
y3 = [100*js31/js3, 100*js32/js3, 100*js33/js3, 100*js34/js3, 100*js35/js3, 100*js36/js3, 100*js37/js3, 100*js38/js3, 100*js39/js3, 100*js310/js3, 100*js311/js3, 100*js312/js3, 100*js313/js3, 100*js314/js3, 100*js315/js3, 100*js316/js3, 100*js317/js3]
y4 = [100*js41/js4, 100*js42/js4, 100*js43/js4, 100*js44/js4, 100*js45/js4, 100*js46/js4, 100*js47/js4, 100*js48/js4, 100*js49/js4, 100*js410/js4, 100*js411/js4, 100*js412/js4, 100*js413/js4, 100*js414/js4, 100*js415/js4, 100*js416/js4, 100*js417/js4]
y5 = [100*js51/js5, 100*js52/js5, 100*js53/js5, 100*js54/js5, 100*js55/js5, 100*js56/js5, 100*js57/js5, 100*js58/js5, 100*js59/js5, 100*js510/js5, 100*js511/js5, 100*js512/js5, 100*js513/js5, 100*js514/js5, 100*js515/js5, 100*js516/js5, 100*js517/js5]
y6 = [100*js61/js6, 100*js62/js6, 100*js63/js6, 100*js64/js6, 100*js65/js6, 100*js66/js6, 100*js67/js6, 100*js68/js6, 100*js69/js6, 100*js610/js6, 100*js611/js6, 100*js612/js6, 100*js613/js6, 100*js614/js6, 100*js615/js6, 100*js616/js6, 100*js617/js6]
y7 = [100*js71/js7, 100*js72/js7, 100*js73/js7, 100*js74/js7, 100*js75/js7, 100*js76/js7, 100*js77/js7, 100*js78/js7, 100*js79/js7, 100*js710/js7, 100*js711/js7, 100*js712/js7, 100*js713/js7, 100*js714/js7, 100*js715/js7, 100*js716/js7, 100*js717/js7]

x1 = np.array(x1)
x2 = np.array(x2)
x3 = np.array(x3)
x4 = np.array(x4)
x5 = np.array(x5)
x6 = np.array(x6)
x7 = np.array(x7)

xnew1 = np.linspace(x1.min(), x1.max(), 300)
xnew2 = np.linspace(x2.min(), x2.max(), 300)
xnew3 = np.linspace(x3.min(), x3.max(), 300)
xnew4 = np.linspace(x4.min(), x4.max(), 300)
xnew5 = np.linspace(x5.min(), x5.max(), 300)
xnew6 = np.linspace(x6.min(), x6.max(), 300)
xnew7 = np.linspace(x7.min(), x7.max(), 300)

power_smooth0 = spline(x1, y1, xnew1)
power_smooth1 = spline(x2, y2, xnew2)
power_smooth2 = spline(x3, y3, xnew3)
power_smooth3 = spline(x4, y4, xnew4)
power_smooth4 = spline(x5, y5, xnew5)
power_smooth5 = spline(x6, y6, xnew6)
power_smooth6 = spline(x7, y7, xnew7)

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
去负数(power_smooth4,4)
smooth4 = smooth
去负数(power_smooth5,5)
smooth5 = smooth
去负数(power_smooth6,6)
smooth6 = smooth




plt.plot(xnew1, smooth0, label="小于0.6", linestyle = '-')
plt.plot(xnew2, smooth1, label="60%-65%", linestyle = '-')
plt.plot(xnew3, smooth2, label="65%-70%", linestyle = '-')
plt.plot(xnew4, smooth3, label="70%-75%", linestyle = '-')
plt.plot(xnew5, smooth4, label="75%-80%", linestyle = '-')
plt.plot(xnew6, smooth5, label="80%-85%", linestyle = '-')
plt.plot(xnew7, smooth6, label="大于85%", linestyle = '-')

plt.xlabel("用时 t(min)",fontsize=12)
plt.ylabel('概率密度 %',fontsize=12)
plt.title('充满率与进厢时间关系图(上行)\n',fontsize=15)

new_ticks = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51]
plt.xticks(new_ticks,fontsize=12)
plt.yticks(fontsize=12)
plt.legend(loc='upper left',ncol=1)
plt.savefig("进厢 — 充满率时间关系图(上行).jpg", dpi=200)
plt.show()


