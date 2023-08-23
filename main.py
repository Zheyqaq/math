import matplotlib.pyplot as plt
import pandas as pd
import time
nums = 0


def draw(lsss: list, nums):
    plt.plot(range(len(lsss)), lsss)
    plt.xlabel("Len")
    plt.ylabel("height")
    plt.figure(figsize=(640, 480))
    plt.savefig(f"{nums}lss.jpg")
    nums += 1


level = pd.read_excel("./data/附件1_工件1的测量数据.xlsx")
z = level.z
result = []
lens = 0
zlist = list(z)
lentap = []
lentaps = []
R = []
for i in range(len(zlist)):
    if i + 1 >= len(zlist):
        break
    if zlist[i] > -1.77571:
        if len(lentap) != 0:
            if min(lentap) < -2.3:
                draw(lentap, nums)
                result.append(len(lentap))
                lentaps.append(lentap)
        lentap.clear()
        continue
    else:
        lentap.append(zlist[i])

draw(R, nums)

for i in lentaps:
    time.sleep(5)
    draw(i,nums)