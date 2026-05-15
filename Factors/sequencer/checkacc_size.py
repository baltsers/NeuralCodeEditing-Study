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

l75=0
l100=0
l125=0
l150=0
l175=0
l200=0
g200=0

TP75=0
TP100=0
TP125=0
TP150=0
TP175=0
TP200=0
TP200l=0

for prog_len in correctXs:
    # if prog_len<75:
    #     TP75+=1
    #     l75+=1
    if prog_len<100:
        TP100+=1
        l100+=1
    elif prog_len<125:
        TP125+=1
        l125+=1
    elif prog_len<150:
        TP150+=1
        l150+=1
    elif prog_len<175:
        TP175+=1
        l175+=1
    elif prog_len<200:
        TP200+=1
        l200+=1
    else:
        TP200l+=1
        g200+=1

for prog_len in failureXs:
    # if prog_len<75:
    #     l75+=1
    if prog_len<100:
        l100+=1
    elif prog_len<125:
        l125+=1
    elif prog_len<150:
        l150+=1
    elif prog_len<175:
        l175+=1
    elif prog_len<200:
        l200+=1
    else:
        g200+=1

#print(TP75/l75,l75)
print(TP100/l100,l100)
print(TP125/l125,l125)
print(TP150/l150,l150)
print(TP175/l175,l175)
print(TP200/l200,l200)
print(TP200l/g200,g200)
