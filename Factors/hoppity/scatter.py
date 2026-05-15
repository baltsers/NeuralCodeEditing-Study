import matplotlib.pyplot as plt
import numpy as np

import pdb

f1=open('statistics_true_3d.csv')
f2=open('statistics_false_3d.csv')

correctXs=[]
correctYs=[]
correctZs=[]
correctSize=[]

corrects=f1.readlines()
for correct in corrects:
    correctXs.append(int(correct.split(',')[1]))
    correctYs.append(int(correct.split(',')[2]))
    correctZs.append(int(correct.split(',')[3]))
    # if int(correct.split(',')[1]) in correctXs and int(correct.split(',')[2]) in correctYs:
    #     correctSize[correctXs.index(int(correct.split(',')[1]))]+=1
    # else:
    #     correctXs.append(int(correct.split(',')[1]))
    #     correctYs.append(int(correct.split(',')[2]))
    #     correctSize.append(1)
    

failureXs=[]
failureYs=[]
failureZs=[]
failureSize=[]

failures=f2.readlines()
for failure in failures:
    failureXs.append(int(failure.split(',')[1]))
    failureYs.append(int(failure.split(',')[2]))
    failureZs.append(int(failure.split(',')[3]))
    # if int(failure.split(',')[1]) in failureXs and int(failure.split(',')[2]) in failureYs:
    #     failureSize[failureXs.index(int(failure.split(',')[1]))]+=1
    # else:
    #     failureXs.append(int(failure.split(',')[1]))
    #     failureYs.append(int(failure.split(',')[2]))
    #     failureSize.append(1)


fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')

ax.scatter(failureXs,failureYs,failureZs,marker='.',color='red',alpha=0.1)
ax.scatter(correctXs,correctYs,correctZs,marker='.',color='green',alpha=0.5)

#ax.plot(failureXs,failureYs,'.',color='red')
#ax.invert_yaxis()
ax.set_xlabel('Program Length')
ax.set_ylabel('Edit Length')
ax.set_zlabel('Pattern Frequency in the training set')
plt.show()