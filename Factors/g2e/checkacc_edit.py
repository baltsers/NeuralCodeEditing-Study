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
TP5=0
TP10=0
TP25=0
TP50=0
#TP100=0
#TP30=0
TP50l=0
l5=0
l10=0
l25=0
l50=0
l100=0
#l30=0
g50=0
for edit_len in correctYs:
    if edit_len<4:
        TP5+=1
        l5+=1
    elif edit_len<10:
        TP10+=1
        l10+=1
    elif edit_len<40:
        TP25+=1
        l25+=1
    elif edit_len<100:
        TP50+=1
        l50+=1
    # elif edit_len<100:
    #     TP100+=1
    #     l100+=1
    # elif edit_len<25:
    #     TP25+=1
    #     l25+=1
    # elif edit_len<30:
    #     TP30+=1
    #     l30+=1
    else:
        TP50l+=1
        g50+=1

for edit_len in failureYs:
    if edit_len<4:
        l5+=1
    elif edit_len<10:
        l10+=1
    elif edit_len<40:
        l25+=1
    elif edit_len<100:
        l50+=1
    # elif edit_len<100:
    #     l100+=1
    # elif edit_len<25:
    #     l25+=1
    # elif edit_len<30:
    #     l30+=1
    else:
        g50+=1

print(TP5/l5,l5)
print(TP10/l10,l10)
print(TP25/l25,l25)
print(TP50/l50,l50)
# print(TP100/l100,l100)
#print(TP25/l25,l25)
#print(TP30/l30,l30)
print(TP50l/g50,g50)