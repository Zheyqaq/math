import matplotlib.pyplot as plt
import pandas as pd


def draw(lsss: list):
    plt.plot(range(len(lsss)), lsss)
    plt.xlabel("Len")
    plt.ylabel("height")
    plt.show()
    plt.figure(figsize=(640, 480))
    result.append(len(lentap))


level = pd.read_excel("./data/附件1_工件1的测量数据.xlsx")
# print(level)
# x = level.x
z = level.z
result = []
lens = 0
zlist = list(z)
lentap = []
R = []
for i in range(len(zlist)):
    if i + 1 >= len(zlist):
        break
    if zlist[i] > -1.77571:
        if len(lentap) != 0:
            if min(lentap) < -2.3:
                draw(lentap)
        lentap.clear()
        continue
    else:
        lentap.append(zlist[i])

draw(R)
