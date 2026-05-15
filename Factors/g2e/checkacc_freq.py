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

l0=0
l5=0
l10=0
l50=0
l100=0
l500=0
g500=0

TP0=0
TP5=0
TP10=0
TP50=0
TP100=0
TP500=0
TP500l=0

for freq in correctZs:
    if freq==0:
        l0+=1
        TP0+=1
    elif freq<10:
        l5+=1
        TP5+=1
    elif freq<20:
        l10+=1
        TP10+=1
    # elif freq<50:
    #     l50+=1
    #     TP50+=1
    elif freq<100:
        l100+=1
        TP100+=1
    elif freq<500:
        l500+=1
        TP500+=1
    else:
        g500+=1
        TP500l+=1

for freq in failureZs:
    if freq==0:
        l0+=1
    elif freq<10:
        l5+=1
    elif freq<20:
        l10+=1
    # elif freq<50:
    #    l50+=1
    elif freq<100:
        l100+=1
    elif freq<500:
        l500+=1
    else:
        g500+=1

print(TP0/l0,l0)
print(TP5/l5,l5)
print(TP10/l10,l10)
#print(TP50/l50,l50)
print(TP100/l100,l100)
print(TP500/l500,l500)
print(TP500l/g500,g500)